# Skill migration validation

Validation date: 2026-09-20. This is a summary of evidence, not a source pin.

## Package and artifacts

- Work suite: 33 tests passed with the optional artifact dependency group.
- Real Foundation/kernel/tool-skills tests discover and load all 33 skill bodies,
  with eager/deferred resolver registration, visibility enabled/disabled,
  unrelated working directories, and workspace/user/library precedence.
- Existing runtime/provider configuration and skill sources survive composition.
- Every retained reference hash and explicit skill resource path resolves.
- Template packaging preserves bytes and refuses collisions, invalid names,
  symlink references, and invalid preview signatures.
- All 20 original templates rendered through LibreOffice and Poppler into 53
  page images. Page overviews were visually inspected; a workbook header was
  also inspected at full resolution. These are baseline blank templates, not
  proof that arbitrary populated content fits.
- Six workbook examples calculated in LibreOffice with independently specified
  expected outputs, and saved files retained formulas. This includes budget
  variance, weighted pipeline, status counts, and a simplified three-statement
  balance check. No native Excel feature parity is claimed.
- DOCX and PPTX edit/readback tests preserve source assets; the deck keeps editable
  text objects. A generated PDF form round-trips a filled text field.
- Missing renderer dependency reports failure instead of claiming completion.

The optional artifact tests require the `artifacts` dependency group. Six real
calculation tests additionally require LibreOffice. Environments without those
dependencies skip the relevant tests; CI's minimal dev environment does not
establish artifact execution acceptance by itself.

## Actual host and browser

An isolated Unified 0.19.0 instance at
`6749dbe6980d8ad2111ef5f5a9a9200b94d8a086` loaded the original Work bundle path,
preserving Foundation namespace roots. Its actual prepared session loaded 33
Work skills plus the host's `amplifier-shell` skill. No provider was mounted and
no model calls occurred. No production configuration or conversation was used.

The mounted app-control tool created and inspected a persistent canvas app,
updated shared state, suppressed a duplicate retry, rejected a stale revision,
and preserved an unsent draft. Chromium passed five checks: visible artifact,
user interaction/state readback, same-tab revision, state/draft preservation
after reload, and absence of browser errors. The screenshot was visually
inspected. The isolated server was stopped after validation.

Resolved evidence revisions: tool-skills
`57f082c7b91147a53f476e28aa6aaa4b3e1d85a0`, Foundation
`3796a32351d32a93ccbb5e230c9ffe02964db42e`, host-selected loop-live
`de307c398facea5d4d656e14f84938a74b934ff2`. Work sources follow `main`; these
values identify what was exercised and do not constrain future updates.

## Limits

No broad model-driven skill benchmark, native live Excel control, image-provider
execution, cloud import, physical audio, or exact OpenAI asset fidelity was
tested. The optional adapter skills disclose these dependencies. The original
Work references and public-library workflows are replacements for workflow
categories, not a claim of full source implementation parity.
