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
git+https://github.com/microsoft/amplifier-bundle-work@main#subdirectory=bundle.md
```

The bundle and its module sources follow `main`, so host ecosystem updates can
advance them together. Hosts should stage and validate updates before activation
and retain the installed revisions for rollback. A local checkout can also be
selected by its absolute `bundle.md` path.

The root contributes nine tool modules, including `apply_patch`, `delegate`,
`read_transcript`, `load_skill`, managed `bash`, `tool_exec`, `web_search` and `web_fetch`.
Modules may expose more than one callable tool.
It does not select a provider, model, or reasoning effort. Other capabilities
must be composed explicitly.

## Work + Amplifier development

Use the independent Work-based development root:

```text
git+https://github.com/microsoft/amplifier-bundle-work@main#subdirectory=bundles/work-amp-dev.md
```

Its exact includes are:

```yaml
includes:
  - bundle: work:bundle.md
  - bundle: git+https://github.com/microsoft/amplifier-foundation@main#subdirectory=behaviors/amp-dev.yaml
```

This is **Work + the portable amp-dev capability**, not Anchors + Work.
It includes neither Anchors nor `presets/anchors-work.md`. Work retains its
`loop-live` and `context-managed` defaults. Foundation's behavior adds the lean
`amp-dev:amplifier-dev-expert`, short ecosystem instructions, and the Tester
behavior with DTU/Gitea capabilities; it selects no orchestrator or context
manager. Applications may override the complete root's runtime defaults.

Both Work roots explicitly load `@work:context/system.md`, the unchanged
operating instruction shared at that path. Root bodies replace included bodies,
so the variant preserves Work's instruction rather than relying on include
fallback. The amp-dev context accumulates through its behavior and is not
repeated in either body.

Work is included first. List-valued tool configuration accumulates parent-first,
so Work skill sources precede sources contributed by the amp-dev dependency
chain; reversing the includes is not a byte-identical composition. Verify the
intended same-name skill precedence. Local composition and prompt-construction
qualification passes; an isolated host also passed authenticated HTTPS, real
root/expert execution and browser conversation reload checks.
See [execution validation](docs/EXECUTION-VALIDATION.md).

## Extend an existing bundle

Compose the behavior last to retain the existing provider and tool configuration:

```yaml
includes:
  - bundle: <your-existing-bundle>
  - bundle: git+https://github.com/microsoft/amplifier-bundle-work@main#subdirectory=behaviors/work-local.yaml
```

The behavior adds transcript retrieval while preserving both the host's
orchestrator and context manager. It does not install the root's filesystem,
shell, search, or delegate tools. Its sources follow `main` through the host
ecosystem updater.

To select Work's live loop **and** managed context, compose
`bundles/work-session.yaml` from your root instead. That session composition
includes the same transcript behavior and selects `loop-live` plus
`context-managed`. Work and Anchors + Work already use it; moving context
selection there leaves their declared runtime defaults unchanged. Existing
consumers of `behaviors/work-local.yaml` that relied on it to select managed
context must move that root include to `bundles/work-session.yaml`, or choose
their context manager explicitly in their own complete root. This migration does
not imply any behavior should choose a host runtime.

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
- Conversation search, application actions, artifact presentation, and worker controls
  are discovered from the host when present. The root does not emulate those
  application services or assume every host supplies them.

The root and Anchors preset also include `behaviors/work-execution.yaml`, which
adds managed Bash handles, `tool_exec`, and real DDGS web search. This behavior
preserves both the host's orchestrator and context manager. The complete Work and
Anchors roots enable approved programmatic dispatch through their orchestrator
configuration; other
compatible roots can explicitly opt in with `session.orchestrator.config.programmatic_dispatch: true`.
The standalone `bundles/work-session.yaml` keeps its existing loop defaults and
now owns managed-context selection. The lightweight `work-local.yaml` overlay is
transcript-only; include `work-execution.yaml` for the additional tools.
Existing tool safety policies still apply. Raw interpreter stdin requires an
unrestricted trusted host policy. Explicitly requested PTYs are supported on
POSIX hosts when the mounted Bash module and host policy permit them. Process
handles do not remain live after their owner exits; inspect retained operation
evidence rather than replaying an uncertain effect.

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

## Work skill library

The root and Anchors + Work preset include 33 on-demand skills: documents, PDF,
presentations, spreadsheets, live Excel guidance, visualization, template creation,
integration management, five core authoring/research/image workflows, and 20
original reference templates. Use `load_skill` or a host's `/skill-name` support.
Work owns 32 skill bodies; the canonical
[imagegen bundle](https://github.com/microsoft/amplifier-bundle-imagegen) supplies
the remaining `imagegen` skill through its skill-only behavior. The default Work
root does not mount an image generator. The library is discovered through bundle
namespaces from any workspace.
Project and personal skills with the same name take precedence.
Within each scope, native `.amplifier/skills` precedes shared `.agents/skills`;
both project directories precede both personal directories. See the
[Agent Skills integration notes](docs/AGENT-SKILLS.md) for format and testing
boundaries.

These are **original Amplifier implementations of the workflow categories** in
the inspected OpenAI installation, not copies of its proprietary packages.
The document package explicitly restricts extraction and redistribution, and
the default-template plugin is marked proprietary. No source helper scripts,
private artifact-tool runtime, or retained OpenAI template assets are included.
The 20 templates are newly authored Work references with different designs and
models. See [migration scope and limitations](docs/OPENAI-SKILLS.md) and the
[complete source-to-target manifest](migration/openai-skills.json).

Compose only the skills behavior to add the library to another root:

```yaml
includes:
  - bundle: <existing-bundle>
  - bundle: git+https://github.com/microsoft/amplifier-bundle-work@main#subdirectory=behaviors/work-skills.yaml
```

This behavior follows current ecosystem branches and preserves existing
runtime, provider, and agent configuration while accumulating skill sources.
`work-local.yaml` is the transcript-only behavior; `bundles/work-session.yaml`
selects both the loop and context manager.

Office/PDF authoring uses optional public Python dependencies. For a new setup,
first resolve current Amplifier dependencies and retain its private receipt:

```sh
python3 scripts/resolve_amplifier_latest.py --mode latest --project . \
  --evidence /absolute/private/new-work-artifact-resolution
uv sync --locked --group dev --group artifacts
```

For normal skill use, an agent can use an existing suitable environment or set
up a task-local environment following the skill instructions. Rendering also
requires LibreOffice and Poppler on PATH (or `WORK_SOFFICE` and `WORK_PDFTOPPM`
executable paths). Loading a skill does not install these dependencies.
Image generation, live Excel, web research, and native cloud imports require
corresponding mounted host capabilities. Work supplies no account credentials.

Unified can open standalone HTML snapshots or persistent canvas apps through
its discovered `app_control` actions. The optional visualization host reference
documents this path without adding an application dependency to Work.


## Ownership and validation

This bundle owns composition and operating guidance. Its runtime dependencies
own execution and context policy; consuming applications own their integration
and acceptance tests. Composition tests verify loading from an unrelated working
directory and preservation of existing providers/tools by the behavior overlay.

```sh
python3 scripts/resolve_amplifier_latest.py --mode latest --project . \
  --evidence /absolute/private/new-work-development-resolution
uv sync --locked --group dev
uv run --no-sync pytest -q
```

The resolver refreshes Amplifier dependencies, including transitive packages,
before recording the lock used by the test environment. It preserves the old
lock as evidence. To reproduce a prior qualification, select its recorded lock
and use `--mode replay` instead. See [latest dependency resolution](docs/LATEST-RESOLUTION.md)
for receipt contents and boundaries.

For a coordinated local imagegen candidate, set `WORK_IMAGEGEN_BUNDLE` to its
absolute checkout path when running pytest. This explicit test-only include
override exercises its real manifests and skill without changing maintained
sources. Without it, tests resolve the canonical imagegen bundle on `main`; that
source must be accessible.

No provider calls are made by these tests. For initial Amplifier setup, see
[the ecosystem entry point](https://github.com/microsoft/amplifier).

## Anchors + Work preset

Use `presets/anchors-work.md` as a root to retain Anchors tools, agents, and
principles while applying Work execution and managed context:

```text
git+https://github.com/microsoft/amplifier-bundle-work@main#subdirectory=presets/anchors-work.md
```

Register it as `anchors-work` in a consuming host. This preset follows the Anchors root on `main` and composes the Work session last. Anchors still owns its
transitive dependencies and routing policy; the preset does not freeze every
Anchors dependency or force worker models to match the parent. Configured host
providers and policies remain in effect.
## Contributing

> [!NOTE]
> This project is not currently accepting external contributions, but we're actively working toward opening this up. We value community input and look forward to collaborating in the future. For now, feel free to fork and experiment!

Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit [Contributor License Agreements](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
