# Portable artifact workflow

These skills use public Python libraries and host capabilities. They do not
depend on an OpenAI package cache or the private artifact-tool runtime.

Resolve this directory from the `skill_directory` returned by `load_skill`.
Keep generated files in the user's workspace, normally `outputs/<task>/`.
Never write into an installed skill or dependency directory during ordinary use.
Use an existing suitable Python environment or provision a task-local one with
`uv venv` and `uv pip install --python <venv-python> python-docx python-pptx
openpyxl reportlab pypdf Pillow`. For development of this bundle,
`uv sync --group dev --group artifacts` installs the locked authoring libraries.
Do not assume installation has happened; verify imports first.

If the host advertises `app_control`, discover its current `runtime.` actions.
When `runtime.dependencies` is available, read its schema and request the
dependency report for the calling session before choosing executables. If its
schema offers import verification, request it and check the result for the
selected authoring interpreter. Keep host
and worker results separate: use the environment where the authoring command
will actually run. An absent worker is not evidence that its dependencies are
missing. Package metadata and executable version probes do not prove imports,
rendering, recalculation, or visual review; perform the required task checks.
Do not start an unrelated session merely to inspect its dependencies.

Read only what the task needs. Preserve originals; use a new output path unless
the user requests replacement. Start from a supplied template when its contents
and permitted use match the request. Do not invent business facts to fill slots.
Use specific titles, connected prose, readable text, and clearly labelled units.

## Rendering

The helper `render.py` beside this file converts DOCX, PPTX, or XLSX with
LibreOffice, then rasterizes PDF pages using Poppler. It also accepts PDFs.
Install these external tools through the host's normal dependency setup if
authorized. Set `WORK_SOFFICE` and `WORK_PDFTOPPM` to executable paths when they
are not on PATH. No Codex runtime path is built in.

```
python <shared-directory>/render.py <input-file> --output-dir <workspace>/qa
```

Inspect every newly created document page and slide, and every changed spreadsheet
view. Use an available image-reading tool. If the host exposes output attachment and
image-read actions, discover their current schemas, attach each rendered PNG,
and request the saved version's actual pixels using its identifier and digest.
Read the returned image content before making visual corrections. A successful
attachment alone is not image inspection; opening the path in a UI is not proof
the agent inspected it. Correct clipping, unreadable labels, overlap, broken
charts, empty pages, and missing fonts, then rerender affected output. A render
command succeeding does not establish visual quality. If no renderer or image
inspection capability is available, retain the artifact and explicitly report
that visual verification remains incomplete.

LibreOffice conversion can alter unsupported native Office features. For complex
existing files, inventory those features before choosing an editing engine. Do
not silently round-trip files containing unsupported elements or discard VBA,
embedded media, tracked changes, external links, or native sensitivity tables.
Use the intended Office engine when exact native behavior matters.

## Delivery and cloud services

Return the requested final file through ordinary Markdown links or the host's
artifact capability. Do not expose temporary render pages unless requested.
Do not emit Codex-specific citation, template-card, or follow-up directives.

For Google Docs/Slides/Sheets, discover a mounted authenticated connector and
read its real import/export schema. Author and validate the local Office file
first when that path suits the request, then import only with the user's
authorization. An XLSX/DOCX/PPTX file is not a native Google artifact. If import
is unavailable, deliver the local artifact and identify the unfinished cloud
step. Local skills do not transfer account credentials from another application.
