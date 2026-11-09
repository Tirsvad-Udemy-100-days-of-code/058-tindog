# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [109e51b] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [GOV-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-003] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-004], [RC-010] |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | [MIL-004] | [RC-006] |
| [MIL-004] | MIL | en | it | [BC-001], [MIL-003] | - | [RC-007] |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | - | [RC-008] |
| [GOV-001] | GOV | en | it | [BC-001], [SA-001] | - | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002], [MIL-003] | none | pytest tests in MIL-002 and MIL-003 | Covered |
| CN-002 | [PP-001], [GOV-001] | none | RC records | Covered |
| CN-003 | [MIL-001] (Go/No-Go criterion 6) | none | grep check in MIL-001 | Covered |
| CN-004 | [MIL-002] | none | code review RC | Covered |
| CN-005 | [MIL-001], [MIL-004] | none | README check in MIL-004 | Covered |
| CN-006 | [MIL-001], [MIL-004] | none | API check in MIL-001 | Covered |
| CN-007 | [MIL-001] | none | pyproject check in MIL-001 | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [PP-001] | No Business Case risk trace or No-Go rule in the first draft | [RC-003] | Resolved | [PP-001] |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-repository-foundation.md
[MIL-002]: ../milestones/mil-002-bootstrap-lectures-1-2.md
[MIL-003]: ../milestones/mil-003-tindog-landing-page.md
[MIL-004]: ../milestones/mil-004-readme-screenshots-wiki.md
[DICT-001]: ../dictionary.md
[GOV-001]: ./governance.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
[RC-008]: ./reviews/rc-008-dictionary.md
[RC-009]: ./reviews/rc-009-governance.md
[RC-010]: ./reviews/rc-010-code-mil-001.md
[109e51b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/commit/109e51b66de566b81925c85b7a93dcf006cf5b95
