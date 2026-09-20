---
name: template-creator
description: Create or update a reusable Amplifier artifact template skill from a permitted reference document, deck, workbook, image, or message.
compatibility: "Python 3.11+ and Amplifier load_skill; matching authoring skill for Office/PDF/image references; renderer and image reader for visual QA."
user-invocable: true
---

# Template Creator

Create a self-contained Amplifier skill with a retained reference and a manifest.
This uses Amplifier filesystem discovery, not a Codex gallery or plugin cache.

1. Identify the exact reference and whether this is creation or an explicitly
   requested update. For cloud references, use a real authorized export tool;
   do not store account credentials or guess a download URL. Confirm the user
   can reuse the reference before redistributing it. Preserve the original.
2. Choose `.amplifier/skills/artifact-template-<name>` in the project or the
   user's requested destination. Do not overwrite an existing skill by default.
3. For DOCX/PPTX/XLSX/PDF, load the corresponding authoring skill and render a
   representative first page/slide/sheet. Inspect the preview for readability.
   For images retain the original; for a message retain exact UTF-8 text and
   make a preview only if a suitable renderer is available.
4. Run `${SKILL_DIR}/scripts/create_template.py` with `--reference`, `--name`,
   `--description`, and `--destination` (the parent skills folder). Optionally
   pass a verified `--preview`. The helper writes the reference, SHA-256,
   `artifact-template.json`, and an Amplifier `SKILL.md`, refuses overwrite, and
   rejects symlink inputs. Read its JSON result and verify the resulting files.
5. Load the new skill through `load_skill` and exercise it on a disposable copy.
   For updates, identify the exact destination, preserve unaffected resources,
   update the manifest hash if the reference changes, and rerender its preview.

Keep layout and content responsibilities explicit: the retained reference controls
format where the user gives no contrary instruction; user sources control facts.
Template creation does not authorize cloud publication or integration installation.
