# Optional decision models and UI use

Work includes the portable UI-use behavior once; work-amp-dev inherits it.
The behavior supplies bounded browser/computer tasks and preserves the host loop,
context and provider choices. A host can supply a connected or managed browser;
direct browser execution requires UI-use's optional browser extra and host setup.
Desktop execution is separately enabled through UI-use's `behaviors/computer.yaml`
or the canonical computer-use behavior, retaining its normal permission path.
The default include installs no browser SDK, decision SDK or desktop executor.

Ordinary action selection is the default. Decision selection requires an enabled
provider-owned backend and a per-surface binding permitting observation transfer.
OpenAI and Azure extend their existing provider accounts; TypeSafe Jev has its own
provider module. The shared `amplifier-lib-decisions` library owns the portable
contract, without credentials, an SDK, browser dependencies or a Core dependency.
There is no decision hook bundle to include.

The maintained include tracks the canonical UI-use repository's main branch.
For changes that are not yet merged, use explicit `sources.bundles` and
`sources.modules` overrides. The host needs the scoped dispatch and attributed
ordinary-inference capabilities supplied by the coordinated streaming/live loop
updates before bounded UI-use tasks can run.

The `work-ui-use` alias remains usable for an existing consumer. It composes the
same behavior without replacing the consumer's orchestrator or context.
