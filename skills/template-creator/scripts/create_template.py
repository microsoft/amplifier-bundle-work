#!/usr/bin/env python3
"""Package a permitted local reference as an Amplifier template; never overwrite."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

KINDS = {'.docx': ('document', 'documents'), '.pptx': ('presentation', 'presentations'),
         '.xlsx': ('spreadsheet', 'spreadsheets'), '.pdf': ('pdf', 'pdf'),
         '.png': ('image', 'imagegen'), '.txt': ('message', None)}


def create(reference, name, description, destination, preview=None):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        raise ValueError('Name must be a lowercase hyphenated identifier of at most 64 characters')
    if not description.strip() or len(description) > 800:
        raise ValueError('Provide a nonempty description of at most 800 characters')
    reference = Path(reference).expanduser()
    if reference.is_symlink():
        raise ValueError('Reference symlinks are not accepted')
    reference = reference.resolve(strict=True)
    kind, author = KINDS.get(reference.suffix.lower(), (None, None))
    if kind is None or not reference.is_file():
        raise ValueError('Unsupported reference type')
    if preview:
        preview = Path(preview).expanduser()
        if preview.is_symlink() or preview.suffix.lower() != '.png' or not preview.is_file():
            raise ValueError('Preview must be a regular PNG file')
        if not preview.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError('Preview is not a PNG')
    name = name if name.startswith('artifact-template-') else f'artifact-template-{name}'
    if len(name) > 64:
        raise ValueError('Final prefixed name exceeds 64 characters')
    folder = Path(destination).expanduser().resolve() / name
    folder.parent.mkdir(parents=True, exist_ok=True)
    folder.mkdir()  # Atomic refusal of existing destinations, including symlinks.
    try:
        (folder / 'assets').mkdir()
        retained = folder / 'assets' / f'reference{reference.suffix.lower()}'
        shutil.copyfile(reference, retained)
        manifest = {'schemaVersion': 1, 'kind': kind, 'reference': str(retained.relative_to(folder)),
                    'referenceSha256': hashlib.sha256(retained.read_bytes()).hexdigest()}
        if preview:
            shutil.copyfile(preview, folder / 'assets' / 'preview.png')
            manifest['preview'] = 'assets/preview.png'
        (folder / 'artifact-template.json').write_text(json.dumps(manifest, indent=2) + '\n')
        route = f'Load `{author}` and follow its template workflow.' if author else 'Draft the requested message using the reference structure and voice.'
        body = f'''---
name: {name}
description: {json.dumps(description)}
user-invocable: true
---

# {name.removeprefix('artifact-template-').replace('-', ' ').title()}

Read `${{SKILL_DIR}}/artifact-template.json`; resolve resource paths inside this
skill directory and verify the reference hash. {route}
Copy the retained reference to the workspace and preserve the original.
Follow the reference's layout and formatting unless the user requests a change.
Populate it only with provided or verified facts; leave missing inputs explicit.
For Office/PDF output, render and inspect the result before delivery. Check
requested edits and template fidelity separately. Report any unsupported native
features; do not claim a cloud import or live-application edit from a local file.
'''
        (folder / 'SKILL.md').write_text(body)
    except BaseException:
        shutil.rmtree(folder)
        raise
    return {'name': name, 'directory': str(folder), 'manifest': manifest}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ('reference', 'name', 'description', 'destination'):
        parser.add_argument(f'--{field}', required=True)
    parser.add_argument('--preview')
    args = parser.parse_args()
    try:
        print(json.dumps(create(**vars(args)), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f'Template creation failed: {error}\n')
