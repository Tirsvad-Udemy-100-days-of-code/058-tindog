# RC-014 Review of the wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e5f840f] |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Closed criterion 14 after the check of the published wiki; verdict Go | [fde8103] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-WIKI-001]
- Scope: full review of docs/wiki/ (5 pages in en, da, ms, plus _Sidebar.md); the wiki is not an artifact with a status, MIL-004 is cited as the milestone that delivers it
- Language and domain: n/a
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | docs/wiki/_Sidebar.md exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, one list of the 5 English pages, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All 5 English pages are listed; a script checked every internal link of every page: no dead link. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wiki, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is last, with English, Dansk and Bahasa Malaysia each linking to its Home. |
| 6 | The sidebar does not repeat the page list per language | Pass | The list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is hand-written content, not produced by a generator kept in the project. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English and the PO language (English) exist; Danish and Bahasa Malaysia added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 15 pages: the same 5 pages in en, da and ms. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | -da and -ms suffixes, English has none. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, file names, class names and addresses are English in all languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | Checked on the published wiki on 2026-11-09 after the merge of PR 27: 15 pages and 15 internal links answer 200, the 3 screenshots load, and the sidebar with the Languages section is shown (checked by S01 stand-in). |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional: no layout rule changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 16 files are directly in docs/wiki/. |

## Overall Verdict

Go — All criteria pass. Criterion 14 was checked on the published wiki after the merge, so the earlier Go-with-conditions is closed.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Done: published wiki checked, criterion 14 set to Pass and the verdict to Go. | S01 | 2026-11-09 |

---

[MIL-004]: ../../milestones/mil-004-readme-screenshots-wiki.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[e5f840f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/commit/e5f840fed7c167422e6b3df444d2c34fb6e34498
[fde8103]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/commit/fde8103d037464767991dd3cad545f09016c92b7
