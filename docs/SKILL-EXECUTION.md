# Skill execution acceptance

Validation date: 2026-09-20. These results describe explicit, bounded synthetic
cases, not a general quality benchmark or source pin. The portable case inputs
are in [evals](../evals/README.md); host runners and live receipts remain outside
this repository.

All 33 skills were loaded and tried in actual model sessions: 30 produced
working results after the documented repairs, including one receipt-path
deviation; three required adapters that were not available. This distinction
is part of the result, not a claim that all 33 capabilities are operational.

## Environment and evidence

An isolated Amplifier Unified 0.19.4 host at `83eb5a53` prepared the actual Work
bundle and real mounted tools. It retained the existing selected provider,
Terra / `gpt-5.6-terra` / high, through `provider-openai`. Each case had a fresh
synthetic workspace and session. Actual `load_skill` calls, produced files,
independent checks, and authoritative message history established execution.
No production conversation, private source template, or real business input
was replayed.

Installed runtime code was recorded separately from cached bundle/context
sources. Foundation was `52dec7e276db62f720448c8e2ec176b9cbffde2d`, kernel
`6d4cd217f83bb29b671b5c9d854aaa08be14db1b`, loop-live
`cbc85d2b8e24d5892a9dcfe78eaadb02b9c2eef5`, and provider-openai
`f0c94b001f70e11c0a668eb9886639b63cc0bbbf`. Installed tool-skills Python files
were byte-matched to cached source `da9c368196fcb9f98d93312bcbe5527561d5fc34`.
A cache directory name alone was not treated as installed-code provenance.

Work guidance changed during acceptance. Per-case hashes of actual model-visible
skill bodies distinguish the initial `21f53e6`, compatibility update `ab35f68`,
printing/retrieval update `a5974bf`, typography/composition fixes `d99a102` and
`a140a38`, and chart/save guidance `7b5e214`. This does not claim every case ran
against every revision. Runtime sources continue to follow `main`.

The deployed host lacked a working model-side pixel reader for generated files.
Models disclosed that limitation. An independent observer inspected rendered
pages instead; rendering success and observer review are not autonomous model
visual QA. A separate runtime parity change is outside this acceptance scope.

## Template cases

All 20 produced populated editable outputs, preserved their installed reference
files, and passed independent content/structure checks. All 53 final page images
were reviewed. Six spreadsheet templates retained formulas, calculated expected
cached values, and passed changed-input recalculation checks on saved copies.
Every deck was checked for effective typography and paragraph alignment against
its reference, including inherited defaults.

| Skill (prefix `artifact-template-`) | Result | Reviewed pages |
| --- | --- | ---: |
| design-report | Pass | 1 |
| experiment-analysis | Pass | 1 |
| investment-committee-memo | Pass | 1 |
| legal-memorandum | Pass | 1 |
| minimal-letterhead | Pass | 1 |
| strategy-memorandum | Pass | 1 |
| system-design | Pass | 1 |
| business-review | Pass | 5 |
| market-trends-report | Pass | 5 |
| operating-review | Pass | 5 |
| project-kickoff | Pass | 5 |
| simple-dark-mode | Pass | 4 |
| simple-light-mode | Pass | 4 |
| team-alignment | Pass | 5 |
| analytics-dashboard | Pass | 2 |
| financial-budget | Pass | 2 |
| operating-calendar | Pass | 2 |
| project-tracker | Pass | 2 |
| sales-pipeline | Pass | 2 |
| three-statement-forecast | Pass | 3 |

Two genuine slide fidelity failures (`simple-light-mode` and `team-alignment`)
were rerun after adding preservation instructions for inherited font defaults,
run/paragraph properties, and alignment. Both retries passed. Other completed
decks were rechecked without model replay. Template formulas and asset bytes
were not altered to satisfy the checks.

A `minimal-letterhead` startup failed before a prompt because concurrent cold
clones raced in Foundation's cache. The unexecuted case passed after the cache
was ready. Another case was interrupted during setup and restarted before its
prompt. The cache issue has a separate proposed fix in
[Foundation #402](https://github.com/microsoft/amplifier-foundation/pull/402);
that fix was not installed in these sessions.

Some initial assertions were overly strict about PDF whitespace or harmless
subject paraphrases. They were corrected against the original artifacts,
retaining failed receipts. Delayed UI projections also omitted final messages
that were present in authoritative histories. No sales-pipeline model replay
was needed; one redundant visualization delivery-only continuation made no
mutations.

## Workflow cases

| Skill | Result | Evidence |
| --- | --- | --- |
| documents | Pass | Editable one-page memo, supplied facts and risk table, rendered page reviewed |
| pdf | Pass | Blank original preserved; filled text/checkbox values and interactive widgets retained; page reviewed |
| presentations | Pass | Three editable slides with notes, content and shape bounds checked; all pages reviewed |
| spreadsheets | Pass after repair | Formula caches 77.5 revenue/5 units; changed copy 90/6; intact chart, correct axis labels and two-page print layout |
| skill-creator | Pass | Created, registered, loaded, and executed a new audit skill |
| skill-installer | Pass | Complete licensed fixture installed to project `.agents/skills`, registered, loaded, and executed; source unchanged |
| plugin-creator | Functional pass with path deviation | Actual Foundation load and namespace resolution, correct module/source/configuration; receipt written at a different workspace path |
| template-creator | Pass | Actual helper retained reference/hash, then registered, loaded, and used the new template |
| visualize | Pass after repair | Nine browser checks: persisted state, two user changes, clean save, state-preserving same-app revision, reload, standalone values, narrow layout, no page errors |
| openai-docs | Pass | Actual official HTTPS response retained; supported API facts with direct citations; used authorized process fetch |
| imagegen | Adapter unavailable | Actual mounted capabilities inspected; no image generation claimed |
| excel-live-control | Adapter unavailable | No live Excel adapter found; no unrelated workbook accessed or file substitute claimed |
| plugin-management | Adapter unavailable for requested Drive task | Management schemas/inventory inspected read-only; no authenticated Drive import/export claimed |

The initial extension attempt exhausted its iteration bound without valid
module composition. A concrete public Foundation example corrected that gap;
the retry loaded and used its authored skill. Its validation receipt was valid
but placed under the generated extension instead of the requested output path.
That deviation remains recorded, and guidance now explicitly honors the
requested receipt destination.

The spreadsheet's initial print split a chart across pages and reversed its
axis labels. A retry fixed printing; a bounded continuation repaired the axis
mapping in that same artifact and session. Recalculation and observer review
then passed, with original cell values/formulas unchanged and the changed-input
workbook byte-for-byte unchanged. Prior faulty outputs remain in private
evidence. This is a repaired acceptance case, not a claim of first-attempt
success.

The generated canvas initially saved shared state without acknowledging its
native input edit version, leaving the view dirty. A targeted continuation
revised the same app to commit saved edits. Browser checks then confirmed
`dirty=false`, a subsequent revision preserved the same app and saved state,
and reload retained 20 hours / 60 tasks. The standalone 420-pixel view also
produced the expected 30, 0, and 60 task values without horizontal overflow.
One browser-check invocation omitted a required revision argument; correcting
the harness and reusing the completed app needed no additional model call.

## Scope limits

These cases explicitly name skills. They do not measure natural catalog routing,
repeat-run reliability, other models, Windows/Linux artifact rendering, native
Excel behavior, or quality improvement against a previous/no-skill baseline.
The references are original Work assets, not fidelity copies of proprietary
OpenAI templates. Credentials, user settings, model transcripts, live receipts,
and generated acceptance artifacts are excluded from this repository.
