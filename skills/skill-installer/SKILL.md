---
name: skill-installer
description: Discover and install Amplifier-compatible skills from a local folder or Git repository into the requested project, personal directory, or bundle.
compatibility: "Amplifier filesystem tools and load_skill; Git and network access for remote sources."
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

Use `.agents/skills` when the user requests a shared cross-client install. Work
discovers both conventions; project skills precede user skills, and native paths
win within a scope. Check the actual winning path from `load_skill` after install.

Check resource closure before copying an individual skill. Work's Office skills
share `../_shared` helpers, so install the collection through its behavior or
include that sibling directory without overwriting an existing different version.
A lone `SKILL.md` or leaf directory is not the complete package in this case.

For Git sources, follow the requested branch and record the tested revision in
validation evidence. Do not pin bundle or module source declarations. Register
through the host's real skill-source configuration when preferable to copying.
Namespaced bundle sources are resolved through Foundation; relative `./skills`
is unsafe when the host starts elsewhere.

Finish the authorized installation in the current conversation:

1. Confirm the guarded writes succeeded. A saved permission or file-existence
   check alone does not prove installation; keep refused or unknown effects explicit.
2. Refresh the destination source with `load_skill(source="/absolute/skills")`,
   using its resolved path. An already configured directory can need this refresh
   after a new skill is written. Do not require a chat reload or another user Go.
3. Use `load_skill(info="installed-name")` to verify the winning path and inspect
   the installed files and resources. Source refresh adds unknown names; existing
   catalog names keep precedence. Report shadowing rather than replacing a winner
   or claiming an existing name's metadata was refreshed.
4. Verify catalog visibility. For an inline skill, load its full content when
   needed to verify the installation. For `context: fork`, inspect metadata and
   files instead: do not invoke it merely to test installation. Installing a skill
   does not authorize executing it.

Report the destination, revision, invocation, dependencies, and validation. Do
not claim that skill installation also installed its external services.
