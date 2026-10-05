# Managed execution composition validation

This opt-in behavior composes managed Bash, tool-exec and real web retrieval without selecting or configuring an orchestrator or context manager. The complete Work root and Anchors preset include it and opt their loop into approved programmatic dispatch. The smaller work-local overlay provides transcript retrieval only; work-session is the separate composition selecting both loop-live and context-managed. Providers, selected models and reasoning settings are preserved.

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

## Portable amp-dev and runtime-boundary migration

The new `bundles/work-amp-dev.md` composes `work:bundle.md` followed by
Foundation's `behaviors/amp-dev.yaml`. It includes neither Anchors nor the
Anchors + Work preset. The portable behavior owns the lean
`amp-dev:amplifier-dev-expert`, short ecosystem instruction, and Tester behavior
with its transitive DTU/Gitea capabilities; it selects no runtime.

Work's existing root instruction now lives unchanged in `context/system.md` and
is explicitly loaded by both Work roots. Context-manager selection moved from
`behaviors/work-local.yaml` into `bundles/work-session.yaml`; the former is
transcript-only and preserves both host runtimes. Complete roots/session
compositions choose runtime defaults, which applications may override.

Local qualification passes all **93 Work tests**, using the coordinated
Foundation candidate. Its **227 focused tests** also pass. Checks cover unrelated
working-directory loading, namespace and expert resolution, preservation of
Work's loop/context defaults and operating instruction, behavior overlays
preserving both consumer runtimes, and intended skill-source precedence.
Production prompt construction loads Work's instruction and ecosystem context
once and resolves the expert's spawn-only references. Module activation is mocked
in that prompt check; it is not a live provider or application result.
List-valued configuration accumulates parent-first, so a different include order
must not be described as a byte-identical mount plan without evidence.

The coordinated candidate was qualified in an isolated consuming host:
Work `0292a0457e5fe6c6ac0f03ea3c200f915b41b3b2` and Foundation
`98f4f82aeb3d422e9ff8778735d466606178d8bb`. The installed application and worker
Foundation provenance and ten bundle/resource hashes matched those candidates.
Trusted HTTPS, authenticated login, a real root response and a real amp-dev expert
spawn passed. The mounted root retained managed context and had no Anchors runtime
agents. A rendered browser created a Work amp-dev conversation, received a model
response and retained the conversation after reload. This checks the host's LAN-IP
endpoint, not routing from a separate physical LAN client. Immediate reload after
typing lost an unsent draft; reload after the normal save settled retained it.

Full bundle and agent recipes were also invoked on both repositories. The initial
Foundation bundle run stopped at an oversized shell argument; agent report
generation was cancelled. Work's local agent scan completed with zero agents
(not validation of composed external agents), and bundle analysis did not produce
a final report. Individual-manifest checks do not prove recursive composition.
A cause-specific large-payload transport correction passed 73 regression checks;
the corrected Foundation recipe reached final synthesis with a FAIL verdict.
It retained two existing context-budget errors and two compatibility-wrapper
resolution errors against cached remote Foundation rather than the candidate.
Its composition analysis timed out, so the completed recipe does not establish
full recursive coverage. The new amp-dev behavior and lean expert passed their
deterministic checks. Work's unfinished bundle run was not replayed; cancellation
was requested, without a confirmed terminal record. Missing build dependencies
and all retained warnings/errors remain explicit limitations.

The historical receipts above remain evidence for their recorded candidates.
These observations are bounded integration evidence, not complete host-release
acceptance or a claim that every validation recipe passed.

## Merged upstream and public-source qualification

Foundation [PR #439](https://github.com/microsoft/amplifier-foundation/pull/439)
was squash-merged as `ab87882027bc5cb3aa74a6f6de539560b2e4d264`. Its complete
tree matches the reviewed `7213f82` candidate, and seven enumerated Anchors/amp-dev
runtime-resource paths match the official CLI-qualified `319a6dc` candidate. The original
candidate commits remain historical evidence, not ancestors of the squash commit.
All six post-merge Linux/Windows Python 3.11–3.13 jobs passed in
[run 37360793685](https://github.com/microsoft/amplifier-foundation/actions/runs/37360793685).

Work `e9317ce2a9aa338d762f42e4346a47894bc1a07a` then passed all **93 tests**
in 48.43 seconds with Foundation's Python library from a worktree at that merge
commit via `PYTHONPATH`. A separate fresh
registry resolved the maintained `amplifier-foundation@main` behavior from public
GitHub to that exact merge commit; no candidate, mirror, or local include override
was used. Git hashes for the same seven runtime-resource paths matched the
CLI-qualified candidate.
Qualification used Linux Python 3.13 and core 2.0.1, with application source-store
and install overrides removed for the test process only.

The composed root preserves Work's `loop-live` / `context-managed` choices,
provider neutrality, root instruction, and four amp-dev capability agents, with
no Anchors runtime agents. This is library/composition qualification, not a new
live provider run. Maintained sources still track `main`; recorded revisions are
receipts, not pins. The failed/incomplete validation-recipe outcomes above remain
unchanged. Downstream PR CI must separately qualify its resolved latest sources.
