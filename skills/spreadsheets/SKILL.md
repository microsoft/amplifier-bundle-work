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
For charts, match labels to the displayed orientation: the numeric axis carries
the value/unit and the category axis identifies the items. Verify this after
conversion; correct source cells do not prove the rendered labels are correct.
In openpyxl `BarChart`, `x_axis` is the category (`TextAxis`) object and
`y_axis` is the value (`NumericAxis`) object even with `type = "bar"`.
For horizontal revenue-by-item bars, use `chart.x_axis.title = "Item"` and
`chart.y_axis.title = "Revenue (USD)"`; do not swap these properties to match
physical screen directions. See the [bar chart documentation](https://openpyxl.readthedocs.io/en/3.1/charts/bar.html).
For signed bar series, set `series.invertIfNegative = False` explicitly and
verify that negative values plot on the negative side of zero. Some LibreOffice
imports render a missing setting incorrectly even when source formulas and
chart caches retain the negative value. Compare every plotted category and sign
with the calculated cells; correct tables alone do not validate a chart.
Choose formulas supported by the intended engine. Do not replace native Excel
Data Tables, iterative models, dynamic arrays, or pivot behavior with static
values without the user's agreement.

Reopen the saved workbook once with formulas visible. Recalculate a disposable
copy through Excel or LibreOffice, then reopen the recalculated file with
`data_only=True` to inspect cached results and formula errors. Change a driver
in a copy and confirm outputs update. Setting `fullCalcOnLoad` alone is not a
recalculation test. Retain the original when the engine changes unsupported
features; disclose any unverified native behavior.

The delivered file must contain actual calculated results, not only a disposable
verification copy. Run `${SKILL_DIR}/scripts/finalize_xlsx.py` on the final draft
with `--output <new-final.xlsx>`. It uses LibreOffice (or `WORK_SOFFICE`), validates
every input and formula against the calculated copy, then transfers only real
formula caches into the original package. All other native parts are retained.
The supported helper always performs a fresh calculation of its immutable input
snapshot; it does not accept precomputed caches. Do not fabricate caches. Known
input, formula, scoped-name, table and hidden-row differences fail visibly,
as do source edits during calculation. These conservative checks are not a
complete proof of arbitrary workbook semantics. Metadata-sensitive
`CELL`/`INFO`/XLM formulas, iterative or precision-as-displayed modes,
shared/array/data-table formulas and error results fail visibly and require the
native engine instead of being flattened. Reopen the
delivered file with both formula and `data_only=True` views. Any subsequent save
with openpyxl can erase caches, so finalize again after the last edit.

Render the used areas of created or changed sheets and inspect readability,
chart labels, truncation, and page breaks. After adding rows, extend print areas,
tables, filters, formula ranges, and chart series where needed. A blank template
may print only its header until its print area is expanded; verify populated
rows appear in the exported pages, not just in the editable workbook.
Include floating chart bounds in the intended print view; worksheet cell
dimensions alone omit charts. For a one-page summary, choose a suitable paper
orientation, set `page_setup.fitToWidth = 1`, `fitToHeight = 1`, and enable
`sheet_properties.pageSetUpPr.fitToPage`. Long tables may need multiple pages
in height instead. Check the exported page count against the intended views and
ensure no chart or title is split across pages. Keep text readable when scaling.
Inspect every final page, including changed source-data sheets. An attachment or
an earlier render is not a visual check of the final file. Confirm that each
final PNG was actually delivered as pixels to the image reader.
Return the requested workbook and
describe what was checked. Native Google Sheets delivery requires a real import
connector. Do not call a static XLSX preview a live Excel session.
