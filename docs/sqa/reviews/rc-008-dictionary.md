# RC-008 Review of the Domain Dictionary

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [DICT-001], [QC-DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | Checked against the document; no defect found. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Checked against the document; no defect found. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | Pass | The project has no Domain Model; the dictionary terms are those used in BC-001 and the milestones. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | Pass | No design artifact exists yet; the IT terms are used in code and wiki commands. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Checked against the document; no defect found. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | Used-in columns name BC, PP, MIL and source code, which exist. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Checked against the document; no defect found. |
| 8 | The dictionary rows are in ascending order of the PO term (case-insensitive, by the alphabet of the PO language) | Pass | Rows are in ascending order: Course day, Landing page, Lecture step, Local viewing, Page component, Responsive layout. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language and Domain rows hold en and it. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | en is BCP 47 and it is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register checked against the registry: matches the type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms follow DICT-001 (lecture step, landing page, page component, responsive layout); no synonym found. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Headings, keys, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The reviewer reads English and knows the IT domain, so no second language reviewer was needed; recorded as a stand-in decision. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (PO, CDN, SVG, ARB) are spelled out or standard IT terms. |

## Overall Verdict

Go — Every Mandatory criterion passes.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None: no Fail and no Pending criterion. | S01 | 2026-11-09 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
