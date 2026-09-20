#!/usr/bin/env python3
"""Render an Office file or PDF without changing the source. Requires external tools."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def executable(variable, default):
    value = os.environ.get(variable) or shutil.which(default)
    if not value or not Path(value).is_file():
        raise RuntimeError(f'Missing {default}; install it or set {variable} to its executable')
    return value


def render(source, destination):
    source = Path(source).resolve(strict=True)
    destination = Path(destination).resolve()
    if source.suffix.lower() not in {'.docx', '.pptx', '.xlsx', '.pdf'}:
        raise ValueError('Supported inputs: DOCX, PPTX, XLSX, PDF')
    poppler = executable('WORK_PDFTOPPM', 'pdftoppm')
    office = executable('WORK_SOFFICE', 'soffice') if source.suffix.lower() != '.pdf' else None
    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError('Render destination must be empty; use a new QA directory')
    with tempfile.TemporaryDirectory(prefix='work-render-') as temporary:
        staging = Path(temporary)
        if office:
            subprocess.run([office, f'-env:UserInstallation={(staging / "profile").as_uri()}',
                            '--headless', '--convert-to', 'pdf', '--outdir', str(staging),
                            str(source)], check=True, capture_output=True, text=True, timeout=120)
            pdf = staging / f'{source.stem}.pdf'
            if not pdf.is_file() or not pdf.stat().st_size:
                raise RuntimeError('Office conversion produced no PDF')
        else:
            pdf = source
        target = destination / 'render.pdf'
        if target == source:
            raise ValueError('Output must not overwrite the input')
        shutil.copyfile(pdf, target)
        subprocess.run([poppler, '-png', '-r', '120', str(target), str(destination / 'page')],
                       check=True, capture_output=True, text=True, timeout=120)
    images = sorted(destination.glob('page-*.png'))
    if not images:
        raise RuntimeError('PDF rasterizer produced no page images')
    return {'source': str(source), 'pdf': str(target), 'pages': [str(p) for p in images],
            'visual_inspection': 'required'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source')
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(render(args.source, args.output_dir), indent=2))
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        parser.exit(1, f'Render failed: {error}\n')
