# Amplifier Work bundle

This repository owns portable Work composition, operating instructions, and
composition tests. Keep runtime implementations in their module repositories.
Application-specific setup, browser acceptance, and preview launchers belong in
the consuming application. Do not add a dependency on an application here.

Reusable behaviors must preserve both the host's orchestrator and context
manager. Complete roots/session compositions choose defaults; applications may
override them. `work-local` is transcript-only; `work-session` owns both runtimes.
`work-amp-dev` composes Work plus Foundation's amp-dev behavior, never Anchors.
Preserve `@work:context/system.md` explicitly in each Work root body. When changing
include order, verify namespace resolution and intended skill precedence:
list-valued module configurations accumulate parent-first rather than replace.

Preserve provider neutrality, explicit delegation policy, and branch-tracking module
sources. Do not pin bundle or module sources to commits or tags. Record tested
revisions in validation receipts, without turning them into source constraints. Keep credentials, user settings, transcripts, and live test output out
of Git. Follow the repository boundaries in
https://github.com/microsoft/amplifier/blob/main/docs/REPOSITORY_RULES.md.
