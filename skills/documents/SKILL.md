---
name: documents
description: Create, edit, review, comment on, or redline Word DOCX documents. Use for reports, memos, letters, and Google Docs-bound files; render and inspect before delivery.
user-invocable: true
---

# Documents

Read `${SKILL_DIR}/../_shared/artifacts.md` for environment, rendering, and delivery.
This is an original portable implementation, not the restricted OpenAI package.

1. Establish the intended reader, decision or purpose, requested format, and
   source facts. For an existing file, inspect paragraphs, styles, tables,
   sections, comments, and relationships before choosing the edit strategy.
2. Create or edit DOCX with `python-docx`. Use semantic Title and heading styles,
   explicit page margins and paragraph spacing, consistent typography, and table
   widths that fit the page. Use actual page breaks only where structurally
   needed. Keep headings with following text and repeat table headers.
3. Preserve the reference's structure when a template is supplied. Replace
   placeholders in a copy; do not flatten formatted runs or remove hyperlinks,
   bookmarks, fields, numbering, headers, or footers as a side effect.
4. For comments, use the installed library's documented comment API, anchor to
   the intended runs, and use the user-provided author or a neutral label. For
   tracked changes, do not substitute plain text replacement: use a capable
   Office adapter or inspect and edit OOXML `w:ins`/`w:del`, revision IDs, dates,
   and author metadata on a copy. Verify accepting/rejecting changes in the
   intended engine; report this feature as unverified if it cannot be tested.
5. Reopen the saved DOCX and check text, tables, headers, links, and requested
   changes. Render with the shared helper, inspect all pages, and iterate.
6. Return the DOCX. Import to a native Google Doc only through a real connector
   when requested, and report the resulting URL after verifying the operation.

Completion requires a saved, readable file with verified content and a visually
reviewed layout. Separate native tracked-change or cloud acceptance from local
file checks; never claim them based on XML inspection alone.
