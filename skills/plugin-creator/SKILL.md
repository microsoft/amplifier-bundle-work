---
name: plugin-creator
description: Package reusable capabilities as an Amplifier bundle, behavior, skills collection, or MCP integration. Use for Amplifier extensions, not Codex marketplace registration.
compatibility: "Amplifier bundle or module authoring workspace; filesystem/process tools; validation tools for the selected extension type."
user-invocable: true
---

# Extension Creator

In Amplifier, choose the package that supplies the needed capability: a skill
for guidance, a behavior for composition, a tool module for runtime operations,
or an MCP server for an external integration. Keep application-specific setup
in the consuming host; keep execution implementations in their module repos.

Create `bundle.md` with YAML frontmatter including `bundle.name`, `bundle.version`,
and `bundle.description`. Add explicit `includes`, `tools`, `context`, or skills sources as
needed. Use branch-tracking sources for runtime modules, record tested revisions
in validation evidence without constraining future updates, and use
bundle-relative namespace paths for resources. Reuse existing capabilities
before implementing a new module. Preserve provider neutrality.

For a skills collection, compose a reviewed tool-skills module and register
`@<bundle-name>:skills`. Create skills using `skill-creator`; do not introduce a
Codex manifest or marketplace as an Amplifier registration mechanism. For MCP,
document the server command, dependencies, environment-variable names, and
available operations; let the host own secrets and connection lifecycle.

Start a simple skills collection with this working shape, replacing the bundle
name consistently and placing `skills/<skill-name>/SKILL.md` beside `bundle.md`:

```yaml
---
bundle:
  name: example-skills
  version: 0.1.0
  description: Reusable skills for the requested workflow.
tools:
  - module: tool-skills
    source: git+https://github.com/microsoft/amplifier-bundle-skills@main#subdirectory=modules/tool-skills
    config:
      skills:
        - "@example-skills:skills"
---

# Example skills

Load the relevant skill when requested.
```

`module` is the module ID; the Git URL belongs in `source`. Putting the URL in
`module` does not declare a loadable module. Use the Foundation environment
already available to the task, or provision a task-local environment with
`amplifier-foundation` from its `main` branch. Avoid broad filesystem searches
for private application internals just to validate a bundle.

From an unrelated working directory, use the public bundle interface:

```python
import asyncio
from pathlib import Path
from amplifier_foundation import load_bundle
from amplifier_foundation.mentions import BaseMentionResolver

bundle_path = Path("/absolute/path/to/example-skills/bundle.md")
bundle = asyncio.run(load_bundle(str(bundle_path), strict=True))
bundle.resolve_pending_context()
plan = bundle.to_mount_plan()
assert bundle.base_path == bundle_path.parent
resolver = BaseMentionResolver(bundles={bundle.name: bundle}, base_path=Path.cwd())
assert resolver.resolve(f"@{bundle.name}:skills") == bundle_path.parent / "skills"
print(plan)
```

Check the module ID, source, and configured namespace in the resulting plan.
Then register the authored skills directory with the current `load_skill`
tool's advertised source schema, load the new skill, and execute a small case.
Do not mistake configuration parsing for installed module or host acceptance.

Load the bundle through Foundation from an unrelated directory, inspect the
mount plan, and test overlays for preservation of existing providers/tools.
Test module operations separately from composition and browser acceptance.
Provide setup instructions and provenance. Publishing or connecting an external
service is a separate action governed by the user's requested scope.
