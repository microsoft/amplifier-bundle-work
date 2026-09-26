# Optional image generation and editing

`behaviors/work-images.yaml` is a compatibility include for the canonical
[amplifier-bundle-imagegen](https://github.com/microsoft/amplifier-bundle-imagegen).
`presets/work-images.md` still adds image tools to Work without changing the
conversation provider, model, or orchestrator. Existing source URLs for both
Work entrypoints remain valid.

Work's ordinary root and standalone `behaviors/work-skills.yaml` compose the
canonical bundle's **skill-only** behavior. They expose all 33 skills: 32 bodies
owned by Work plus `imagegen` owned by the imagegen bundle. They do not mount
`tool-image`, enable paid calls, or install an image provider. Project and personal
skill overrides still precede both library namespaces. Work contains no second
imagegen skill body that could shadow the canonical one.

The canonical bundle owns the
[image skill](https://github.com/microsoft/amplifier-bundle-imagegen/blob/main/skills/imagegen/SKILL.md),
[tool implementation](https://github.com/microsoft/amplifier-bundle-imagegen/tree/main/modules/tool-image),
and [backend and receipt contract](https://github.com/microsoft/amplifier-bundle-imagegen/blob/main/README.md).
Follow those sources for capability discovery, generation/editing, preserved
originals, stable request IDs, unknown-effect reconciliation, and exact saved
artifact inspection. Work does not duplicate that policy.

Opting into `work-images` enables requested paid image calls through the logical
`images` backend. The consuming host must separately configure and explicitly
enable that backend and supply account credentials and model selection. Compose
host-specific image settings after the behavior to retain that host's selected
backend and paid-call policy. Installing the behavior grants no account
entitlements and does not change the conversation provider. Keep credentials in
host configuration, never in this bundle or saved task prompts.

Sources follow `@main`. Review records resolved commits as evidence, never as
maintained source pins. Local composition tests may use the explicit
`WORK_IMAGEGEN_BUNDLE` checkout override described in the README. They exercise
real manifests, namespace resolution, and skill loading without provider calls;
they do not establish image-provider entitlement or production acceptance. The
canonical repository must be accessible before publishing this dependency.
