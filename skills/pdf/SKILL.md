---
name: pdf
description: Read, extract, create, combine, or fill PDFs and AcroForms. Use for PDF deliverables and page inspection; use documents for editable Word output.
compatibility: "Amplifier with filesystem and process tools; pypdf and reportlab; Poppler for rendering; image-reading capability for visual QA."
user-invocable: true
---

# PDF

Read `${SKILL_DIR}/../_shared/artifacts.md` for setup and rendering.

Use `pypdf` for metadata, extraction, page operations, and forms; use ReportLab
for new PDFs. Inspect page count, dimensions, text availability, encryption,
annotations, and form fields before modifying an existing document. Scanned
pages need an available OCR engine; lack of extracted text is not an empty page.
Keep exact page references for extracted claims and do not invent missing text.

For a fillable form, inspect `PdfReader.get_fields()` and each widget's field
type, export values, and flags. Map the user's answers to field identifiers;
derive nothing sensitive or consequential merely to complete a form. Clone the
document with `PdfWriter`, update fields using its documented API, and preserve
interactive widgets unless flattening is requested. Check checkboxes using the
actual export state. Signed or encrypted PDFs require a compatible authorized
workflow; modifying a signed file may invalidate its signature.

Save to a separate file, reopen it, inspect field values and annotations, and
render the completed pages. Confirm glyphs, form appearances, pagination, and
content placement. Fix overflow and missing appearances before delivery. Report
when a native viewer's form behavior or signature verification was not tested.
