# OpenAI workflow migration

The reference task listed 13 skills (five core, eight plugins). Filesystem
inventory on 2026-09-20 found another 20 template skills in the plugin cache:
28 plugin skills in total. The Work library maps those 28 and the five core
skills into 33 unique Amplifier names. Cached source files remain untouched.

Upstream `microsoft/amplifier-bundle-skills` was cloned at
`57f082c7b91147a53f476e28aa6aaa4b3e1d85a0`. Its authoring workflow is named
`adapt-skill`, not `adopt`. The companion change extends it with package
inventory, OpenAI portability guidance, provenance, and layered validation.

## What this migration delivers

| Group | Result | Dependency or material difference |
| --- | --- | --- |
| documents, pdf | Portable file workflows and shared rendering helper | Public Python libraries; advanced native features need separate acceptance |
| presentations, spreadsheets | Editable local Office workflows | python-pptx/openpyxl replace private artifact-tool; openpyxl does not calculate formulas |
| 20 artifact templates | Original editable Work reference files and previews | They do not preserve OpenAI reference designs, formulas, or assets |
| template-creator | Functional local reference packager | Amplifier skills discovery, no Codex gallery service |
| visualize | Standalone HTML plus optional Unified canvas adapter | No OpenAI widget globals, CDN assumption, or automatic follow-up calls |
| plugin-management, plugin-creator | Amplifier bundles/MCP/Smart Tool workflows | No Codex marketplace or account connection transfer |
| skill-creator, skill-installer | Amplifier authoring and installation guidance | Uses real skill loader and bundle namespaces |
| openai-docs | Official-source research workflow | Needs mounted search/fetch capability |
| imagegen | Generation/edit workflow with capability checks | Needs an actual image generator; none is bundled |
| excel-live-control | Live-workbook workflow with capability checks | Needs an actual Excel adapter; none is bundled |

These are original workflow replacements. This is **not an exact port of all
source functionality**. The source documents package carries an explicit
restriction against extraction/copying/redistribution; the default templates
are marked proprietary. The implementation contains no copied OpenAI source
scripts, reference prose, private runtime code, or retained binary templates.
Source names, package versions, file counts, and entrypoint hashes identify the
inputs in `migration/openai-skills.json`; those identifiers do not grant rights.
An exact source/asset port requires permission covering that use and a separate
fidelity effort. No public redistribution permission is assumed.

## Host setup

Select the absolute path to this checkout's `bundle.md` in Unified, or compose
`behaviors/work-skills.yaml` last over another root. The behavior has its own
`work-skills` namespace rooted at the bundle directory. Preserve Foundation's
source-base-path mapping when preparing the bundle; flattening its mount plan
into an unrelated file loses namespaced resources.

The `load_skill` module is pinned to the inspected upstream commit. It supports
both immediate resolver registration and the deferred request-hook path. Skills
remain inline; loading them does not invoke child agents or change the provider.
The catalog has a bounded visibility budget and bodies load on demand.

Provision artifact dependencies only in a suitable task environment. LibreOffice
and Poppler are external executables, not vendored into the repository. Use the
shared renderer with an empty output directory, inspect all resulting pages,
and keep intermediate output out of Git. For templates, retain the source file
hash and test requested edits against the chosen engine's preservation limits.

## Validation boundaries

The deterministic suite exercises Foundation composition, the real kernel and
skill tool, all skill loads, resource hashes, template packaging, collision
refusal, and missing-renderer behavior. Separate artifact smoke checks exercise
Office generation, rendering and spreadsheet recalculation. Host acceptance
uses an isolated Unified instance with no production state or provider calls.
See the final validation report for the exact revision and results.

No test here proves general language-model quality parity, native Office feature
parity, connected Excel behavior, image-provider execution, or cloud-import
acceptance. Skill-load success is only discovery/loading evidence.
