# Optional image generation and editing

`behaviors/work-images.yaml` composes the provider-neutral `tool-image` module.
`presets/work-images.md` adds it to Work without changing the conversation's
provider, model or orchestrator. The ordinary Work root remains unchanged.

The runtime module belongs in
[amplifier-module-tool-image](https://github.com/microsoft/amplifier-module-tool-image).
Its backend capability contract and file/receipt semantics are defined there.
Image backend registration, account credentials, paid-call permission and model
selection belong to the consuming host. Installing this behavior supplies none
of those account entitlements.

Enabling this optional behavior sets `allow_paid: true` for user-requested image
work. The host must configure and explicitly enable its selected backend separately.
`images` is the logical backend
identifier in this behavior, not a provider or model name. The chosen backend must
be mounted in the same session. Inputs and generated files remain in the execution
workspace, with narrower configured read/write restrictions respected. Keep
credentials in host configuration, never in this bundle or saved task prompts.

Use `image_generate` capabilities before generation. Every paid effect has a
stable request ID and a durable local receipt. Repeating an ID cannot replay an
unknown or completed request. Edits bind the exact target/reference SHA-256
hashes and produce new files. The imagegen skill covers saved-output delivery and
pixel inspection when the host exposes those capabilities.

Sources track `@main`. During review, use an explicit local module-source override
for the candidate tool repository and record tested commits in private validation
evidence. The new module's remote repository must exist before this optional
behavior can resolve without that override.
