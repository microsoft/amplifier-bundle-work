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
