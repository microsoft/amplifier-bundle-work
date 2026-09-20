---
name: spreadsheets
description: Create, edit, analyze, and chart XLSX, CSV, and TSV files. Use for models, trackers, budgets, and Google Sheets-bound workbooks; use excel-live-control for an open Excel session.
compatibility: "Amplifier with filesystem and process tools; openpyxl; LibreOffice or another calculation engine; Poppler and image-reading capability for visual QA."
user-invocable: true
---

# Spreadsheets

Read `${SKILL_DIR}/../_shared/artifacts.md`. Use `openpyxl` for XLSX, Python's
`csv` module for delimited files, and an actual spreadsheet engine when evaluating
formulas. **openpyxl writes formulas but does not calculate them.**

Inspect the workbook before editing: sheets and visibility, used ranges, formulas,
defined names, tables, charts, validations, conditional formats, number formats,
external links, merged cells, and macros. Preserve these features outside the
requested changes. For XLSM use `keep_vba=True` and retain the extension, but
do not claim this verifies macro execution or every native Excel feature.

Build a clear flow from source inputs and assumptions through calculations to
summaries. Use typed dates and numbers, meaningful units, formulas for derived
values, and consistent references. Keep editable assumptions distinct from
calculated cells. Do not hide missing inputs by converting every error to zero.
Use blank, zero, duplicate identifiers, date boundaries, and rounding examples
to test the logic that matters. Reconcile important totals independently.

Use readable column widths, wrapped headings, suitable date/currency/percentage
formats, frozen headers where helpful, filters, and charts tied to actual data.
Choose formulas supported by the intended engine. Do not replace native Excel
Data Tables, iterative models, dynamic arrays, or pivot behavior with static
values without the user's agreement.

Reopen the saved workbook once with formulas visible. Recalculate a disposable
copy through Excel or LibreOffice, then reopen the recalculated file with
`data_only=True` to inspect cached results and formula errors. Change a driver
in a copy and confirm outputs update. Setting `fullCalcOnLoad` alone is not a
recalculation test. Retain the original when the engine changes unsupported
features; disclose any unverified native behavior.

Render the used areas of created or changed sheets and inspect readability,
chart labels, truncation, and page breaks. After adding rows, extend print areas,
tables, filters, formula ranges, and chart series where needed. A blank template
may print only its header until its print area is expanded; verify populated
rows appear in the exported pages, not just in the editable workbook.
Return the requested workbook and
describe what was checked. Native Google Sheets delivery requires a real import
connector. Do not call a static XLSX preview a live Excel session.
