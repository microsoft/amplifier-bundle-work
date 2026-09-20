# Agent Skills integration

Reviewed against agentskills.io on 2026-09-20. The format is useful across the
Amplifier ecosystem; execution still depends on the composed host and tools.

## Adopted guidance

The [specification](https://agentskills.io/specification) distinguishes required
identity/routing fields from optional license, compatibility, and metadata.
All 33 Work skills now declare their concrete environment requirements through
`compatibility`. Work uses the Amplifier `user-invocable` extension for commands;
it does not present that field as part of the base standard. The template
packager includes requirements in newly created skills too.

The [client guide](https://agentskills.io/client-implementation/adding-skills-support)
describes `.agents/skills` as a sharing convention. Work explicitly includes it
without changing the tool module's global defaults. Fresh composition tests
verify this precedence:

1. Project `.amplifier/skills`
2. Project `.agents/skills`
3. User `~/.amplifier/skills`
4. User `~/.agents/skills`
5. The namespaced Work library

An earlier composed source may still take precedence. Inspect the actual loaded
path when diagnosing a collision. Foreign packages in shared directories still
need dependency, permission, and platform review.

The [authoring guide](https://agentskills.io/skill-creation/best-practices)
reinforces procedures grounded in actual tasks, concise entrypoints, and resources
loaded when needed. Work's authoring skill now includes the portable field rules.
Workbook guidance also addresses a concrete local gotcha: blank templates can
retain header-only print ranges after new rows are added.

The [script guide](https://agentskills.io/skill-creation/using-scripts) recommends
clear noninteractive interfaces and dependency declarations. Work's helpers use
flags, useful errors, structured results, and collision refusal. Dependency
discovery must describe the environment that executes the task; finding a host
package does not prove a worker can import it. Bundle/module sources continue
to follow `main`. Tested hashes identify evidence, not source constraints.

## Validation layers

The upstream `skills-ref` at revision
`69ef37e9424c0a7ea9dd2293b559e43ec8176379` validated the **standard-field
projection** of all 33 skills. Its unmodified full-file check rejects
`user-invocable` on all 33. That expected extension rejection is recorded, not
hidden by claiming full unmodified standard-validator acceptance. The real
Amplifier loader validates the files with the extension intact.

The [evaluation guide](https://agentskills.io/skill-creation/evaluating-skills)
motivates fresh execution cases and independently checked outputs. The
[description guide](https://agentskills.io/skill-creation/optimizing-descriptions)
separates ordinary-prompt selection from explicit invocation. Our receipt should
therefore distinguish:

- Format and package resources.
- Discovery and loading through the real composed session.
- A bounded task with a produced, checked result.
- Rendering, model-side visual inspection, and observer inspection.
- Optional adapters and unavailable paths.
- Natural routing and quality comparisons, when actually measured.

The concrete execution results and limitations are in
[SKILLS-VALIDATION.md](SKILLS-VALIDATION.md). Small acceptance cases do not prove
general quality improvement; that requires repeat runs and a comparable baseline.
Host-specific runners and private receipts stay outside this portable bundle.
