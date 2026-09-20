---
name: plugin-creator
description: Package reusable capabilities as an Amplifier bundle, behavior, skills collection, or MCP integration. Use for Amplifier extensions, not Codex marketplace registration.
user-invocable: true
---

# Extension Creator

In Amplifier, choose the package that supplies the needed capability: a skill
for guidance, a behavior for composition, a tool module for runtime operations,
or an MCP server for an external integration. Keep application-specific setup
in the consuming host; keep execution implementations in their module repos.

Create `bundle.md` with YAML frontmatter including `bundle.name`, `version`, and
`description`. Add explicit `includes`, `tools`, `context`, or skills sources as
needed. Use immutable source revisions for distributed runtime modules, and
bundle-relative namespace paths for resources. Reuse existing capabilities
before implementing a new module. Preserve provider neutrality.

For a skills collection, compose a reviewed tool-skills module and register
`@<bundle-name>:skills`. Create skills using `skill-creator`; do not introduce a
Codex manifest or marketplace as an Amplifier registration mechanism. For MCP,
document the server command, dependencies, environment-variable names, and
available operations; let the host own secrets and connection lifecycle.

Load the bundle through Foundation from an unrelated directory, inspect the
mount plan, and test overlays for preservation of existing providers/tools.
Test module operations separately from composition and browser acceptance.
Provide setup instructions and provenance. Publishing or connecting an external
service is a separate action governed by the user's requested scope.
