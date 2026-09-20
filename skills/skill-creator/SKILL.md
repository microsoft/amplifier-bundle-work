---
name: skill-creator
description: Create or update Amplifier skills with concise routing, portable resources, and actual loader validation. Use for reusable workflows and skill authoring.
user-invocable: true
---

# Skill Creator

Inspect the destination's conventions and existing skill before editing. When
available, load `skills-assist` for current Amplifier authoring guidance. Derive
the workflow from concrete user tasks; include instructions that change useful
decisions rather than repeating generic assistant behavior.

Use a unique lowercase hyphenated `name` and a concise `description` explaining
when to load the skill. Add `user-invocable: true` when a slash command is useful.
Keep interactive work inline. Use `context: fork` only for a bounded independent
task, and only with the current host's support. Fork `allowed-tools` uses module
IDs; omit it when the full parent tool surface is appropriate. Do not pin a
provider/model unless required by the user's requested capability.

Put essential steps and completion evidence in `SKILL.md`. Store conditional
detail in linked references, deterministic helpers in scripts, and reusable
output inputs in assets. Resolve resources relative to `skill_directory` or
`${SKILL_DIR}`; do not assume the caller's working directory.

Save to the authorized bundle or `.amplifier/skills/<name>` destination. Preserve
unrelated files and notices. Parse frontmatter, verify linked resources, load
through the actual `load_skill` tool, and test a realistic scenario including
missing optional capabilities. Report loader, execution, and visual checks
separately. Update an existing skill in place only when that target is requested.
