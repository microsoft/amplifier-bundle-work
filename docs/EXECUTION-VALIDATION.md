# Managed execution composition validation

This opt-in behavior composes managed Bash, approved programmatic dispatch and real web retrieval. The root and Anchors preset include it; the smaller work-local overlay retains its existing scope. Providers, selected models and reasoning settings are preserved.

Maintained sources track `main`. Tested revisions below are evidence, not source pins. Publication depends on the required managed Bash and truthful web changes reaching their configured sources. Context checkpoint persistence additionally depends on context-managed support and a host checkpoint store.

## Implementation evidence

- Bash upstream PR22: managed process handles, ownership, bounded cursor reads, stdin under existing policy, cancellation/actual exit, no pretend live handle after owner death. 196 tests passed and12 platform-dependent cases skipped.
- tool-exec PR1 merged: bounded isolated JavaScript process; nested host permissions/hooks and attributable receipts. 37 module tests passed.
- loop-live PR7 and PR8 merged: opt-in approved dispatch and persisted task continuation guard. Combined65 tests passed. Ordinary tool execution remains unchanged when the option is off.
- Web upstream PR21: real DDGS search, bounded attributable fetch, explicit empty/failure/truncation and no synthetic fallback.54 tests plus upstream Python3.11-3.13 CI passed.
- Context-managed upstream PR4: exact prefix/config-bound persisted boundary checkpoints;17 focused tests passed. Original history and actual tool output remain the host's authority.

Actual Foundation composition verifies root and Anchors loading from unrelated working directories and provider/tool preservation in the lightweight overlay. These tests do not call a model or prove rendering quality.

## Actual Unified model acceptance

An isolated Unified server with Chromium and the existing configured Terra model was exercised with explicitly reviewed local module overrides. The model completed three nested Bash calls and a sum of51, with three successful authoritative call receipts. It started a managed process, read its actual output/exit, created a required question answered through the real UI, and received that answer. Selected conversation, unsent draft and reconnect state were preserved. Real web fetch succeeded.

Search succeeded in one run and timed out explicitly in a subsequent run. The successful-search run encountered a JavaScript output-shape assumption after the underlying tool calls had succeeded; guidance and tool description now explain structured tool output. There is no claim that one complete run passed every check. No mock search result was used as evidence. Approval denial and cancellation passed real AmplifierSession fixtures; additional live UI approval/stop acceptance remains with the host integration.

The same12 underlying calls produced215531 direct output bytes (37080 cl100k tokens) versus3980 selected-output/receipt bytes (1207 tokens). This measures bounded result presentation, not model latency, task quality or a general speedup.

## Release boundary

The behavior alone does not supply concurrent UI, durable questions, task/worker records, native desktop capture, artifact rendering or user account connectivity. It discovers those shared host actions when available. No uncertain mutation is replayed automatically. Physical-device and live account checks are recorded separately by consuming hosts. Full host release acceptance remains open.
