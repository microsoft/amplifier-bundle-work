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

For reproducible installations, replace `main` with a reviewed commit ID. The
bundle's runtime modules are already pinned to immutable commits. A local
checkout can also be selected by its absolute `bundle.md` path.

The root contributes five tools, including `delegate` and `read_transcript`.
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
install the root's filesystem, shell, search, or delegate tools. Use a reviewed
commit in place of `main` when pinning the composed configuration.

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

The profile does not add managed process input/output, a portable child registry,
durable compaction checkpoints, or a persistent asynchronous-question ledger.
It is an experimental composition, not evidence of ChatGPT quality parity.

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

Register it as `anchors-work` in a consuming host. This preset selects a reviewed
Anchors root revision and composes the Work behavior last. Anchors still owns its
transitive dependencies and routing policy; the preset does not freeze every
Anchors dependency or force worker models to match the parent. Configured host
providers and policies remain in effect.
