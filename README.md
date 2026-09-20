# Amplifier Work

A small, provider-neutral bundle for working with a live Amplifier host. It
combines background delegation, visible boundary compaction, transcript retrieval,
and filesystem, shell, and search tools. The host supplies credentials, approvals,
canonical history, live input, and presentation.

This repository and the loop dependency are private during development. Normal
GitHub access is required. No credentials are included in the bundle.

## Select the bundle

Use this source as a conversation's root bundle:

```text
git+https://github.com/bkrabach/amplifier-bundle-work@main#subdirectory=bundle.md
```

The bundle and its module sources follow `main`, so host ecosystem updates can
advance them together. Hosts should stage and validate updates before activation
and retain the installed revisions for rollback. A local checkout can also be
selected by its absolute `bundle.md` path.

The root contributes eight tool modules, including `apply_patch`, `delegate`,
`read_transcript`, managed `bash`, `tool_exec`, `web_search` and `web_fetch`.
Modules may expose more than one callable tool.
It does not select a provider, model, or reasoning effort. Other capabilities
must be composed explicitly.

## Extend an existing bundle

Compose the behavior last to retain the existing provider and tool configuration:

```yaml
includes:
  - bundle: <your-existing-bundle>
  - bundle: git+https://github.com/bkrabach/amplifier-bundle-work@main#subdirectory=behaviors/work-local.yaml
```

The behavior changes the loop/context and adds transcript retrieval. It does not
install the root's filesystem, shell, search, or delegate tools. Its sources also follow `main` through the host ecosystem updater.

## Behavior and boundaries

- Eligible `delegate` calls run in the background only with `async: true`.
  A pending receipt is not a completed result; `live_job` provides result and
  cancellation controls. Waiting can wake for user input.
- The root enables self-delegation with `agent: self` and excludes recursive
  delegation from children. Four pending jobs is a per-loop limit.
- On hosts that support effective model inheritance, children follow the parent's
  selected model and reasoning settings unless an explicit override applies.
- Context preparation pauses at a request boundary for a continuation summary,
  configured to trigger at 70% of the budget and target 1,500 summary tokens.
  Recent work and pending operation references remain available. Original admitted
  history belongs to the host and can be retrieved with `read_transcript`.
- The host owns actual concurrency, event delivery, and recovery. A finite host
  stays finite; this bundle alone does not create a concurrent user interface.
- Patch editing reuses the existing filesystem bundle's patch module. Its native
  operation schema also works as a function tool for other providers. Hosts must
  apply their shared write policy to both filesystem and patch tools; the portable
  module itself defaults to the session workspace and follows symlinks before
  checking its configured allow/deny lists. Adding a tool is not permission to
  bypass a denied write.
- Conversation search, application actions, skills, artifacts, and worker controls
  are discovered from the host when present. The root does not emulate those
  application services or assume every host supplies them.

The root and Anchors preset also include `behaviors/work-execution.yaml`. It
opts into managed Bash handles and approved programmatic dispatch, and configures
real DDGS web search. The lightweight `work-local.yaml` overlay remains limited
to the loop, context and transcript tool; include `work-execution.yaml` after it
when these additional tools are wanted. Existing tool safety policies still apply.
Raw interpreter stdin requires an unrestricted trusted host policy. Managed
processes do not provide PTY support or survive owner death as live handles.

Programmatic JavaScript runs in a fresh bounded process and calls only through
normal tool permissions, with attributable call receipts. It cannot delegate,
run background calls or retain variables. Durable operation records, asynchronous
questions, saved task state and derived compaction persistence are optional host
services discovered through shared actions. Unknown effects are never replayed.
This composition alone is not evidence of ChatGPT output-quality parity.

This change requires the managed-process, truthful-web and approved-dispatch
upstream changes to be merged before publication. Draft integration uses reviewed
local overrides; maintained sources stay on `main`. Tested revision receipts are
evidence, never source pins. See `docs/EXECUTION-VALIDATION.md` for acceptance state.

## Ownership and validation

This bundle owns composition and operating guidance. Its runtime dependencies
own execution and context policy; consuming applications own their integration
and acceptance tests. Composition tests verify loading from an unrelated working
directory and preservation of existing providers/tools by the behavior overlay.

```sh
uv sync --locked --group dev
uv run --no-sync pytest -q
```

No provider calls are made by these tests. For initial Amplifier setup, see
[the ecosystem entry point](https://github.com/microsoft/amplifier).

## Anchors + Work preset

Use `presets/anchors-work.md` as a root to retain Anchors tools, agents, and
principles while applying Work execution and managed context:

```text
git+https://github.com/bkrabach/amplifier-bundle-work@main#subdirectory=presets/anchors-work.md
```

Register it as `anchors-work` in a consuming host. This preset follows the Anchors root on `main` and composes the Work behavior last. Anchors still owns its
transitive dependencies and routing policy; the preset does not freeze every
Anchors dependency or force worker models to match the parent. Configured host
providers and policies remain in effect.
