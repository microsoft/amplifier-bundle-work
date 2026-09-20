# Amplifier Work bundle

This repository owns portable Work composition, operating instructions, and
composition tests. Keep runtime implementations in their module repositories.
Application-specific setup, browser acceptance, and preview launchers belong in
the consuming application. Do not add a dependency on an application here.

Preserve provider neutrality, explicit delegation policy, and branch-tracking module
sources. Do not pin bundle or module sources to commits or tags. Record tested
revisions in validation receipts, without turning them into source constraints. Keep credentials, user settings, transcripts, and live test output out
of Git. Follow the repository boundaries in
https://github.com/microsoft/amplifier/blob/main/docs/REPOSITORY_RULES.md.
