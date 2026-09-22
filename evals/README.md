# Portable skill acceptance cases

These cases exercise the 33 Work skills with synthetic facts. They are inputs
and expected behavior, not saved model conversations. A consuming host owns the
session runner, authentication, artifact presentation, and browser acceptance.
The ordinary pytest suite makes no provider calls.

- [Workflow cases](workflow-cases.json): 13 authoring, artifact, research,
  visualization, and optional-adapter workflows.
- [Template cases](template-cases.json): 20 original reference templates,
  including independent arithmetic and formatting assertions.

For each case:

1. Prepare a fresh workspace and a real session from the Work bundle. Preserve
   its namespace roots. Isolate personal/project skill directories and keep the
   user's selected provider/model; record actual mounted tools and revisions.
2. Materialize the case's synthetic inputs. Point output placeholders at that
   workspace and load the named skill through the session's actual tool.
3. Execute with bounded iterations/time and keep generated files out of the
   installed skill package. Observe actual tool calls, not a statement of intent.
4. Check outputs independently: read editable files, retain original hashes,
   calculate expected totals, and inspect rendered output through a real image
   capability. Record observer inspection separately from model inspection.
5. Preserve failed receipts. Retry only an unexecuted case or an explicitly
   corrected case; do not replay completed work just to refresh a report.

An unavailable adapter is a separate outcome. Correctly explaining that no live
Excel or image-generation adapter is mounted validates capability handling; it
does not validate live workbook editing or image generation. Likewise, a saved
PNG does not prove that the model saw it.

Use semantic assertions that tolerate harmless layout/whitespace changes while
checking the actual requested facts and structure. Do not grade a model-written
receipt without checking the artifact or authoritative tool result it describes.
Record corrections to an overly strict checker and recheck existing outputs
before spending another model call.

These are explicit invocation cases. For natural selection, use ordinary prompts
and near misses with the complete catalog. For quality-improvement claims, add a
previous-version or no-skill baseline with the same tools/model and repeat runs.
See [integration notes](../docs/AGENT-SKILLS.md) and
[validation results](../docs/SKILLS-VALIDATION.md).

## Natural selection and sustained work

[natural-cases.json](natural-cases.json) supplies ordinary requests, near misses,
and three two-turn retrieval/create/review/revise/deliver cases. The runner must
show the full catalog and send `turns` verbatim, without naming skills, adding
routing hints or asking for an evaluation marker. Expected/forbidden skills and
check lists are observer-only. Send the revision only after saving the first
output and its digest. Each case gets a fresh workspace/session.

Start with two near misses and one sustained case, then inspect failures before
expanding. Save actual catalog, mounted provider/model/effort, tool calls, source
and output hashes, per-turn usage, and final delivery links. Score successful
`load_skill` calls separately from artifact content, native feature preservation,
actual recalculation, model-side pixel inspection, and observer visual review.
Never count a model-written review statement or a render receipt as image input.
A blocked external adapter is not an end-to-end pass.

Build the original synthetic inputs with `evals/fidelity.py prepare <workspace>`.
The fixtures are separate from the twenty shipped reference templates. The
portable checks exercise native DOCX features, editable slide charts/notes and
workbook names/validation/conditional formatting/hidden sheets. They prove local
file structure only; native Office/cloud behavior and visual layout require
the intended engine and recorded visual review.

Do not infer cross-model parity or quality improvement from this bounded sample.
A no-skill or previous-version comparator requires the same prompt, tools, model,
limits and repeated runs before making that specific comparative claim.
