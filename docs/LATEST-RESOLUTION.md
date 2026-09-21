# Current Amplifier dependencies and frozen reproduction

The bundle and module declarations follow `main`. A committed Python lock
records one earlier resolution; `uv sync --locked` alone reproduces it.
For a new development or artifact-authoring environment, explicitly resolve
current Amplifier packages before syncing:

```sh
python3 scripts/resolve_amplifier_latest.py --mode latest --project . \
  --evidence /absolute/private/new-work-resolution
uv sync --locked --group dev --group artifacts
uv run --no-sync pytest -q
```

Use a new private evidence directory for each resolution. The script refreshes
Amplifier packages from declared dependencies, development groups, optional
extras and the resolved transitive graph, while preserving explicit source
choices and local overrides. It does not modify maintained branch declarations,
install packages, prepare bundles or call providers. Third-party dependencies
continue to follow their declared compatibility requirements.

The evidence directory retains the original lock, the new resolved lock, the
manifest digest, resolved Amplifier revisions and the package refresh passes.
A failed resolution restores the original lock. Prior evidence is never
overwritten. Review the new lock and run the applicable tests before treating
that environment as qualified.

For reproduction, use an isolated checkout with the earlier recorded `uv.lock`
and run the same command with `--mode replay` and a new evidence directory.
Replay verifies that the lock stays byte-for-byte unchanged.

This tool qualifies this repository's development and artifact dependency
graph. A consuming host owns resolution and validation of the bundle's dynamic
module/include graph, integration, provider configuration and release acceptance.
Existing conversations, active worker environments, local source overrides and
all bundled skills are outside this command's mutation scope.
