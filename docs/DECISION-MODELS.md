# Optional decision models and UI use

Work includes the portable UI-use behavior once; work-amp-dev inherits it.
The behavior supplies bounded browser/computer tasks and includes the canonical
computer-use behavior. It preserves the host loop, context and provider choices.
Browser execution requires the UI-use browser extra and explicit host setup.
Desktop execution uses the existing computer tool and its normal permission path.

Ordinary action selection is the default. Decision selection requires an enabled
provider-owned backend and a per-surface binding permitting observation transfer.
OpenAI and Azure extend their existing provider accounts; TypeSafe Jev has its own
provider module. The shared `amplifier-lib-decisions` library owns the portable
contract, without credentials, an SDK, browser dependencies or a Core dependency.
There is no decision hook bundle to include.

For unpublished development, use explicit `sources.bundles` and `sources.modules`
overrides. The maintained include tracks the canonical UI-use repository's main
branch; publish its dependencies before merging that include into Work.

The `work-ui-use` alias remains usable for an existing consumer. It composes the
same behavior without replacing the consumer's orchestrator or context.
