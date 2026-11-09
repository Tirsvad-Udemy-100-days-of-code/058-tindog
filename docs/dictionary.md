# Domain Dictionary (PO and IT terms)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [109e51b] |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term. PO language: English (`en`), domain `it`.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Course day | en | Project | One day of the bootcamp, delivered as one repository. | BC, PP | source code |
| Landing page | en | Static page | A single HTML page that introduces a product to a visitor. | BC, MIL | source code |
| Lecture step | en | Lesson | One part of the day's course material, with its own page, screenshot and wiki text. | BC, MIL | source code |
| Local viewing | en | HTTP serving | Opening the pages in a browser from the machine the project runs on. | BC, PP | source code |
| Page component | en | Bootstrap component | A ready-made Bootstrap element such as a card, navbar or carousel. | BC, MIL | source code |
| Responsive layout | en | Grid layout | A page arrangement that adapts to the screen width through the 12-column grid. | BC, MIL | source code |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation
  Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- Rows are in ascending order of the PO term (case-insensitive, by the
  alphabet of the PO language), so a term is found without searching.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[109e51b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/commit/109e51b66de566b81925c85b7a93dcf006cf5b95
