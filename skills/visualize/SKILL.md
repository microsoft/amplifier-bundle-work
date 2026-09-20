---
name: visualize
description: Build interactive HTML explanations, charts, simulations, comparisons, and UI mockups. Use when a visual helps understanding; use artifact skills for Office deliverables.
user-invocable: true
---

# Visualize

Choose a visual that explains the user's question: a labelled comparison,
timeline, diagram, simulation, or focused mockup. Prefer interaction only when
it makes a meaningful variable or consequence easier to understand. State units,
assumptions, and data sources; do not invent measurements or scores.

Create standalone HTML in the task workspace. Include its CSS, JavaScript, and
data locally. Do not assume framework globals, external CDNs, host styles, or
`window.openai` APIs. Use responsive layout, readable labels, keyboard-operable
controls, visible focus, sufficient contrast, and a text equivalent of key data.
Test initial state, control changes, reset when provided, small widths, and
empty/boundary values. Do not use color as the only encoding.

Read `${SKILL_DIR}/references/unified.md` when the host exposes `app_control`.
Publish through its discovered canvas schema and check the returned result.
Use persistent canvas apps for iterative shared-state work when available and
simple HTML snapshots for a standalone visual. Keep user selections visible to
the agent through the supported bridge; do not promise unsupported follow-up
messages, persistence, or automatic turn initiation.

Without a canvas, return a link to the standalone HTML. Inspect in an available
browser and verify behavior before reporting visual acceptance. File creation,
publication, successful rendering, and correct interaction are separate claims.
