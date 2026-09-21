# Managed execution composition validation

This opt-in behavior composes managed Bash, tool-exec and real web retrieval without selecting or configuring an orchestrator. The complete Work root and Anchors preset include it and opt their loop into approved programmatic dispatch. The smaller work-local overlay provides context and transcript retrieval; work-session is the separate loop-selecting composition. Providers, selected models and reasoning settings are preserved.

Maintained sources track `main`. Tested revisions below are evidence, not source pins. Publication depends on the required managed Bash and truthful web changes reaching their configured sources. Context checkpoint persistence additionally depends on context-managed support and a host checkpoint store.

## Implementation evidence

- Bash upstream PR22: managed process handles, ownership, bounded cursor reads, stdin under existing policy, cancellation/actual exit, no pretend live handle after owner death. 196 tests passed and12 platform-dependent cases skipped.
- tool-exec PR1 merged: bounded isolated JavaScript process; nested host permissions/hooks and attributable receipts. 37 module tests passed.
- loop-live PR7 and PR8 merged: opt-in approved dispatch and persisted task continuation guard. Combined65 tests passed. Ordinary tool execution remains unchanged when the option is off.
- Web upstream PR21: real DDGS search, bounded attributable fetch, explicit empty/failure/truncation and no synthetic fallback.54 tests plus upstream Python3.11-3.13 CI passed.
- Context-managed upstream PR4: exact prefix/config-bound persisted boundary checkpoints, including repeated compaction with retained reminders;306 module tests passed. Isolated live host acceptance passed30 checks with four real compactions and restart restoration. Original history and actual tool output remain the host's authority.

After merging Work PR7, all 37 composition, skills, artifact-helper and source-policy tests pass in a fresh environment with Foundation 829e4d8 and skills 85bc17ab. Both work-skills and work-execution includes remain present. Actual Foundation composition verifies root and Anchors loading from unrelated working directories and provider/tool preservation in the lightweight overlay. These tests do not call a model or prove rendering quality.

## Actual Unified model acceptance

An isolated Unified server with Chromium and the existing configured Terra model was exercised with explicitly reviewed local module overrides. The model completed three nested Bash calls and a sum of51, with three successful authoritative call receipts. It started a managed process, read its actual output/exit, created a required question answered through the real UI, and received that answer. Selected conversation, unsent draft and reconnect state were preserved. Real web fetch succeeded.

Search succeeded in one run and timed out explicitly in a subsequent run. The successful-search run encountered a JavaScript output-shape assumption after the underlying tool calls had succeeded; guidance and tool description now explain structured tool output. There is no claim that one complete run passed every check. No mock search result was used as evidence. Subsequent real Chromium/worker acceptance verified nested Deny and Allow receipts, absence of the denied effect, and Stop terminating the managed process with exit -15. Separate attributed runs verified persistent Python/Node cells and the real model reusing browser-created state to produce a visible saved artifact. [Host evidence](https://github.com/bkrabach/amplifier-unified/blob/feat/work-parity-integration/docs/validation/live-controls-acceptance.md) preserves each run and its limits.

The same12 underlying calls produced215531 direct output bytes (37080 cl100k tokens) versus3980 selected-output/receipt bytes (1207 tokens). This measures bounded result presentation, not model latency, task quality or a general speedup.

## Release boundary

The behavior alone does not supply concurrent UI, durable questions, task/worker records, native desktop capture, artifact rendering or user account connectivity. It discovers those shared host actions when available. No uncertain mutation is replayed automatically. Physical-device and live account checks are recorded separately by consuming hosts. Full host release acceptance remains open.

## Work session-root reconciliation

The candidate incorporates Work main `2cc9f0a`, retaining its complete
`bundles/work-session.yaml` composition and all 33 skills. Managed execution stays
in both Work and Anchors roots; `programmatic_dispatch` is configured by those
roots. The reusable behaviors preserve a consumer's orchestrator, and the
standalone session composition keeps its existing loop defaults.

The unchanged development lock resolves Foundation
`829e4d8e71cfd8ba1813812bf50f90319db9aa40` and tool-skills
`85bc17abec044e7feb8589beddec3e425317c52f`. An isolated environment using that lock
passes all 41 composition, source-policy, skills and artifact-helper tests. Tests
include both complete roots, all three behavior overlays, and standalone session
loading from an unrelated directory. No provider call was made.

The actual `behavior-hygiene-validation` command from Foundation recipe revision
`fe1c19b584bc9ed8803078d299a34ce2b4b4df95` reports zero errors and two warnings:
work-execution contributes approximately 620 context tokens against a 500-token
warning threshold, and declares three tools against a two-tool warning threshold.
The operating guidance and tool group remain intact; these warnings are retained
in the validation receipt. This composition result does not establish current
all-main module execution or host release acceptance.
