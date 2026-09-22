"""Portable package behavior; external rendering is exercised separately."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re

import pytest

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


creator = load('template_creator', 'skills/template-creator/scripts/create_template.py')
renderer = load('artifact_renderer', 'skills/_shared/render.py')


def test_template_retains_reference_and_refuses_overwrite(tmp_path):
    source = tmp_path / 'message.txt'
    source.write_text('Dear team,\nExact source wording.\n')
    result = creator.create(source, 'team-update', 'Reuse the team update format.', tmp_path / 'skills')
    folder = Path(result['directory'])
    retained = folder / result['manifest']['reference']
    assert retained.read_bytes() == source.read_bytes()
    assert result['manifest']['referenceSha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert 'name: artifact-template-team-update' in (folder / 'SKILL.md').read_text()
    with pytest.raises(FileExistsError):
        creator.create(source, 'team-update', 'Changed', tmp_path / 'skills')
    assert retained.read_bytes() == source.read_bytes()


@pytest.mark.parametrize('name', ['../escape', 'Bad Name', 'x/elsewhere', 'x' * 65])
def test_template_rejects_invalid_names(tmp_path, name):
    source = tmp_path / 'file.txt'
    source.write_text('reference')
    with pytest.raises(ValueError): creator.create(source, name, 'Description', tmp_path / 'skills')
    assert not (tmp_path / 'skills').exists()


def test_template_refuses_symlink_input_and_fake_preview(tmp_path):
    source = tmp_path / 'file.txt'
    source.write_text('reference')
    link = tmp_path / 'link.txt'
    link.symlink_to(source)
    with pytest.raises(ValueError): creator.create(link, 'example', 'Description', tmp_path / 'skills')
    preview = tmp_path / 'preview.png'
    preview.write_text('not png')
    with pytest.raises(ValueError): creator.create(source, 'example', 'Description', tmp_path / 'skills', preview)
    assert not (tmp_path / 'skills').exists()


def test_every_shipped_template_has_a_real_unchanged_reference():
    manifests = sorted((ROOT / 'skills').glob('*/artifact-template.json'))
    assert len(manifests) == 20
    for path in manifests:
        manifest = json.loads(path.read_text())
        reference = (path.parent / manifest['reference']).resolve()
        assert reference.is_relative_to(path.parent.resolve())
        assert reference.is_file()
        assert hashlib.sha256(reference.read_bytes()).hexdigest() == manifest['referenceSha256']
        if 'preview' in manifest:
            assert (path.parent / manifest['preview']).read_bytes().startswith(b'\x89PNG\r\n\x1a\n')


def test_render_reports_missing_dependency_without_claiming_success(tmp_path, monkeypatch):
    source = tmp_path / 'input.pdf'
    source.write_bytes(b'%PDF-1.7\n')
    monkeypatch.setenv('WORK_PDFTOPPM', str(tmp_path / 'missing'))
    with pytest.raises(RuntimeError, match='Missing pdftoppm'):
        renderer.render(source, tmp_path / 'qa')
    assert not (tmp_path / 'qa').exists()


def test_explicit_skill_directory_resources_resolve_in_shipped_collection():
    for skill in (ROOT / 'skills').glob('*/SKILL.md'):
        for relative in re.findall(r'\$\{SKILL_DIR\}/([^`\s]+)', skill.read_text()):
            resource = (skill.parent / relative).resolve()
            assert resource.is_relative_to((ROOT / 'skills').resolve())
            assert resource.exists(), (skill, relative)


@pytest.mark.parametrize('extension', ['.jpg', '.jpeg', '.webp', '.md'])
def test_template_supported_reference_extensions(tmp_path, extension):
    source = tmp_path / f'reference{extension}'
    source.write_bytes(b'retained-reference')
    result = creator.create(source, 'sample', 'Sample format', tmp_path / 'skills')
    retained = Path(result['directory']) / result['manifest']['reference']
    assert retained.read_bytes() == source.read_bytes()



def test_render_orders_double_digit_pages_numerically(tmp_path, monkeypatch):
    source = tmp_path / 'input.pdf'
    source.write_bytes(b'%PDF-1.7\n')
    destination = tmp_path / 'qa'
    monkeypatch.setattr(renderer, 'executable', lambda *args: '/fixture/pdftoppm')
    def rasterize(*args, **kwargs):
        for number in range(1, 13):
            (destination / f'page-{number}.png').write_bytes(b'PNG')
    monkeypatch.setattr(renderer.subprocess, 'run', rasterize)
    result = renderer.render(source, destination)
    assert [Path(path).stem for path in result['pages']] == [f'page-{n}' for n in range(1, 13)]
    assert result['visual_inspection'] == 'required'
