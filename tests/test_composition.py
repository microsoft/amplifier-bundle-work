"""Real Foundation composition; no provider calls in ordinary tests."""
from pathlib import Path

import pytest

import amplifier_foundation as foundation
ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.asyncio
async def test_root_loads_from_an_unrelated_workspace(tmp_path, monkeypatch):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    bundle = await foundation.load_bundle(str(ROOT / "bundle.md"), strict=True)
    plan = bundle.to_mount_plan()
    assert plan["session"]["context"]["config"]["engine"] == "boundary"
    assert {tool["module"] for tool in bundle.tools} >= {"tool-delegate", "tool-transcript", "tool-bash", "tool-apply-patch"}
    patch = next(tool for tool in bundle.tools if tool["module"] == "tool-apply-patch")
    assert '@main#' in patch['source']
    assert patch['config'] == {'engine': 'native'}
    assert not bundle.providers
    assert "agent: self" in bundle.instruction
    assert plan['session']['orchestrator']['config']['programmatic_dispatch'] is True
    bash = next(tool for tool in bundle.tools if tool['module'] == 'tool-bash')
    assert bash['config']['managed_processes'] is True
    assert bash['config']['managed_stdin'] is True
    assert {'tool-exec', 'tool-web'} <= {tool['module'] for tool in bundle.tools}
    web = next(tool for tool in bundle.tools if tool['module'] == 'tool-web')
    assert web['config']['search_engine'] == 'ddgs'


@pytest.mark.asyncio
async def test_overlay_preserves_provider_and_unrelated_tools(tmp_path, monkeypatch):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    base = foundation.Bundle(name="configured", providers=[{"module": "provider-test", "config": {"default_model": "chosen"}}],
                             tools=[{"module": "tool-extra"}], session={"orchestrator": {"module": "existing-loop"}, "context": {"module": "context-simple"}})
    overlay = await foundation.load_bundle(str(ROOT / "behaviors/work-local.yaml"), strict=True)
    result = base.compose(overlay)
    assert result.providers == base.providers
    assert result.session["context"]["module"] == "context-managed"
    assert {tool["module"] for tool in result.tools} == {"tool-extra", "tool-transcript"}
    assert result.session["orchestrator"] == base.session["orchestrator"]


@pytest.mark.asyncio
async def test_local_session_is_complete_without_an_enclosing_root(tmp_path, monkeypatch):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    bundle = await foundation.load_bundle(str(ROOT / "bundles/work-session.yaml"), strict=True)
    assert bundle.session["context"]["module"] == "context-managed"
    assert bundle.session["orchestrator"] == {
        "module": "loop-live",
        "source": "git+https://github.com/microsoft/amplifier-module-loop-live@main",
        "config": {"background_delegate": False, "background_tools": ["delegate"],
                   "max_background_jobs": 4, "inherit_effective_model": True},
    }
    assert {tool["module"] for tool in bundle.tools} == {"tool-transcript"}
    assert not bundle.providers


@pytest.mark.asyncio
async def test_anchors_work_preserves_anchors_capabilities(tmp_path, monkeypatch):
    monkeypatch.setenv('AMPLIFIER_HOME', str(tmp_path / 'shared'))
    monkeypatch.chdir(tmp_path)
    bundle = await foundation.load_bundle(str(ROOT / 'presets/anchors-work.md'), strict=True)
    assert bundle.session['context']['module'] == 'context-managed'
    assert bundle.session['orchestrator']['module'] == 'loop-live'
    assert bundle.session['orchestrator']['config']['background_delegate'] is False
    assert bundle.session['orchestrator']['config']['programmatic_dispatch'] is True
    assert next(row for row in bundle.tools if row['module'] == 'tool-web')['config']['search_engine'] == 'ddgs'
    assert {row['module'] for row in bundle.tools} >= {'tool-web', 'tool-todo', 'tool-delegate', 'tool-transcript', 'tool-skills'}
    assert bundle.agents
    assert '@anchors:context/system.md' in bundle.instruction
    assert not bundle.providers


@pytest.mark.asyncio
@pytest.mark.parametrize("behavior", ["work-local", "work-skills", "work-execution", "work-images"])
async def test_reusable_behaviors_preserve_host_orchestrator(tmp_path, monkeypatch, behavior):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    base = foundation.Bundle(name="configured",
        providers=[{"module": "provider-test", "config": {"default_model": "chosen"}}],
        tools=[{"module": "tool-extra"}],
        session={"orchestrator": {"module": "existing-loop", "config": {
            "programmatic_dispatch": False, "host_setting": "preserved"}}})
    overlay = await foundation.load_bundle(str(ROOT / f"behaviors/{behavior}.yaml"), strict=True)
    assert "orchestrator" not in overlay.session
    composed = base.compose(overlay)
    assert composed.session["orchestrator"] == base.session["orchestrator"]
    assert composed.providers == base.providers
    assert "tool-extra" in {row["module"] for row in composed.tools}


@pytest.mark.asyncio
async def test_optional_images_preserve_provider_and_require_host_configuration(tmp_path, monkeypatch):
    monkeypatch.setenv('AMPLIFIER_HOME', str(tmp_path / 'shared'))
    monkeypatch.chdir(tmp_path)
    behavior = await foundation.load_bundle(str(ROOT / 'behaviors/work-images.yaml'), strict=True)
    assert not behavior.providers and not behavior.session
    assert {row['module'] for row in behavior.tools} == {'tool-image', 'tool-skills'}
    assert next(row for row in behavior.tools if row['module'] == 'tool-image') == {
        'module': 'tool-image',
        'source': 'git+https://github.com/microsoft/amplifier-bundle-imagegen@main#subdirectory=modules/tool-image',
        'config': {'backend': 'images', 'allow_paid': True}}
    root = await foundation.load_bundle(str(ROOT / 'bundle.md'), strict=True)
    assert 'tool-image' not in {row['module'] for row in root.tools}
    preset = await foundation.load_bundle(str(ROOT / 'presets/work-images.md'), strict=True)
    assert not preset.providers
    assert preset.session == root.session
    assert 'tool-image' in {row['module'] for row in preset.tools}
    skills = next(row for row in preset.tools if row['module'] == 'tool-skills')['config']['skills']
    assert skills == [
        '.amplifier/skills', '.agents/skills', '~/.amplifier/skills', '~/.agents/skills',
        '@work-skills:skills', '@imagegen:skills',
    ]
    assert preset.source_base_paths['imagegen'] == root.source_base_paths['imagegen']


@pytest.mark.asyncio
async def test_optional_images_preserve_existing_image_backend_choice(tmp_path, monkeypatch):
    monkeypatch.setenv('AMPLIFIER_HOME', str(tmp_path / 'shared'))
    behavior = await foundation.load_bundle(str(ROOT / 'behaviors/work-images.yaml'), strict=True)
    host = foundation.Bundle(name='host', tools=[{'module': 'tool-image', 'config': {
        'backend': 'selected-image-backend', 'allow_paid': False,
    }}])
    configured = behavior.compose(host)
    image = next(row for row in configured.tools if row['module'] == 'tool-image')
    assert image['config'] == {'backend': 'selected-image-backend', 'allow_paid': False}
