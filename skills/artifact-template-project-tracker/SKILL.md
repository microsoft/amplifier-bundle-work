---
name: artifact-template-project-tracker
description: "Use the project tracker spreadsheet template."
compatibility: "Amplifier Work collection with the spreadsheets skill and its dependencies; renderer and image-reading capability for visual QA."
user-invocable: true
---

# Project Tracker

Read `${SKILL_DIR}/artifact-template.json`; resolve resource paths inside this
skill directory and verify the reference hash. Load `spreadsheets` and follow its template workflow.
Copy the retained reference to the workspace and preserve the original.
Follow the reference's layout and formatting unless the user requests a change.
Populate it only with provided or verified facts; leave missing inputs explicit.
For Office/PDF output, render and inspect the result before delivery. Check
requested edits and template fidelity separately. Report any unsupported native
features; do not claim a cloud import or live-application edit from a local file.

This is an original Work reference template. It does not reproduce the OpenAI template design or retained assets.
