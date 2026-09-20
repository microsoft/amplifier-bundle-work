---
name: skill-installer
description: Discover and install Amplifier-compatible skills from a local folder or Git repository into the requested project, personal directory, or bundle.
user-invocable: true
---

# Skill Installer

Resolve the requested repository/path and revision. Use existing authorized Git
credentials, never embedded tokens. Inspect the skill package, license, scripts,
resource links, and dependencies before installation. Do not execute source
scripts or preprocessing merely to list skills. If a foreign skill needs tool,
runtime, or host translation, use `adapt-skill` when available or report those
requirements before calling it usable.

Use `.amplifier/skills` for a requested project install, `~/.amplifier/skills` for
a personal install, or the exact bundle directory the user selected. Refuse
silent collisions. Copy the whole permitted package while excluding repository
metadata, credentials, generated caches, and dependency directories. Reject
symlinks escaping the package and keep originals intact.

For Git sources, pin a reviewed commit and register through the host's real
skill-source configuration when that is preferable to copying. Namespaced bundle
sources are resolved through Foundation; relative `./skills` is unsafe when the
host starts elsewhere. Refresh discovery through the supported tool or a fresh
session, then call `load_skill` for every installed name and verify resources.
Report the destination, revision, invocation, dependencies, and validation. Do
not claim that skill installation also installed its external services.
