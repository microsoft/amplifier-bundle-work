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

The root contributes seven tool modules, including `apply_patch`, `delegate`,
`read_transcript`, and `load_skill`. Modules may expose more than one callable tool.
It does not select a provider, model, or reasoning effort. Other capabilities
must be composed explicitly.

## Extend an existing bundle

Compose the behavior last to retain the existing provider and tool configuration:

```yaml
includes:
  - bundle: <your-existing-bundle>
  - bundle: git+https://github.com/microsoft/amplifier-bundle-work@main#subdirectory=behaviors/work-local.yaml
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
- Conversation search, application actions, artifact presentation, and worker controls
  are discovered from the host when present. The root does not emulate those
  application services or assume every host supplies them.

## Work skill library

The root and Anchors + Work preset include 33 on-demand skills: documents, PDF,
presentations, spreadsheets, live Excel guidance, visualization, template creation,
integration management, five core authoring/research/image workflows, and 20
original reference templates. Use `load_skill` or a host's `/skill-name` support.
The library is discovered through its bundle namespace from any workspace.
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
runtime, provider, agent, and skill-source configuration. `work-local.yaml`
remains the execution-only overlay.

Office/PDF authoring uses optional public Python dependencies:

```sh
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
git+https://github.com/microsoft/amplifier-bundle-work@main#subdirectory=presets/anchors-work.md
```

Register it as `anchors-work` in a consuming host. This preset follows the Anchors root on `main` and composes the Work behavior last. Anchors still owns its
transitive dependencies and routing policy; the preset does not freeze every
Anchors dependency or force worker models to match the parent. Configured host
providers and policies remain in effect.
