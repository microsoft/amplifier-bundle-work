# Optional decision and UI-use spike

Work and work-amp-dev continue to use ordinary models and their existing tools.
Neither new behavior is part of those defaults. Compose `work-ui-use` explicitly
to add bounded observed-action tasks, and `work-decision-models` only when a typed
decision backend is wanted. They preserve the host's providers, context and loop.
They contain composition only; the separate `amplifier-bundle-ui-use` and
`amplifier-bundle-decision-models` repositories own runtime implementations.

These components are unpublished spike packages. Install them explicitly or set
host `overrides.tool-ui-use.source` and
`overrides.hooks-decision-models.source` to the local checkouts. Explicit source
rows ensure isolated worker dependency preparation includes the new modules. No public source URL is asserted until repository ownership and delivery
are settled. Future remote sources should track a maintained branch.

The root/host must separately enable `programmatic_dispatch` and include `ui_use`
in loop-live's `programmatic_callers` alongside `tool_exec`. A compatible loop
exports `tools.dispatch` and `model.current`. Missing capabilities give a blocked
controller result; ordinary individual tools remain usable. A reusable behavior
must never choose or replace the host's loop to obtain this capability.

The UI-use module needs explicit browser origins and ordinary per-action approval.
For the narrow local X11 experiment, compose computer-use and set
`tool-computer-use.config.observed_control: true`. OCR supplies candidate regions;
the canonical computer tool retains approvals, presence, halt and freshness gates.
This is not a general accessibility implementation or a Windows/macOS acceptance.

Unified can save a named backend and independently choose browser or computer
decision selection. A saved preference does not install tools or grant access.
No configured selection means ordinary models, even when keys and packages exist.
Choose ordinary selection to override an inherited decision preference. A missing
decision backend, refusal or low-confidence answer falls back to the ordinary
selector when configured; an unknown execution outcome stops without replay.
Use ordinary selection explicitly to recover from a decision model's blocked vote.

Future routing may consume the same typed decision interface. This spike does not
change chat/delegation routing, and no decision service is required by Work.
