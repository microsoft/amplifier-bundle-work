---
name: presentations
description: Create or edit editable PowerPoint PPTX slides and Google Slides-bound decks. Use for presentations, slide layouts, speaker notes, and template-based decks.
compatibility: "Amplifier with filesystem and process tools; python-pptx; LibreOffice and Poppler for rendering; image-reading capability for visual QA."
user-invocable: true
---

# Presentations

Read `${SKILL_DIR}/../_shared/artifacts.md`. Use `python-pptx` for portable PPTX
authoring. It is a different engine from OpenAI's private artifact-tool runtime;
do not execute that runtime's examples as if the APIs were interchangeable.

1. Define the audience, decision, story, slide count, and source material. Write
   an outline with one main claim per slide, supported by actual evidence.
2. Inspect any existing deck's slide size, masters, layouts, fonts, objects,
   notes, charts, and embedded resources. Work on a copy. Retain native editable
   text, shapes, tables, and charts rather than rasterizing entire slides.
3. Build a consistent grid, title hierarchy, restrained palette, and readable
   type scale. Keep all objects within the slide. Prefer charts and diagrams
   when they explain a comparison or relationship; label axes and cite data.
4. For edits, change the requested objects while preserving unrelated content.
   Do not rebuild a complex deck through a library that cannot preserve its
   animations, media, SmartArt, or chart behavior; use a capable native adapter
   or report the specific limitation before destructive conversion.
5. Reopen the PPTX to verify slide count, text, notes, chart data, and object
   bounds. Render every slide, inspect full-size images, fix overlap and clipping,
   and render affected slides again. XML bounds alone do not catch text overflow.
6. Return the PPTX, plus a PDF only when requested. A Google Slides request needs
   a verified connector import; a local deck alone does not complete that step.
