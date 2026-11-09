# Governance / ARB Workflow

## Metadata
| Key | Value |
| --- | --- |
| ID | GOV-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [109e51b] |

---

## Purpose

Defines how this project applies Quality Criteria (QC) checklists to real
artifact instances, producing SQA Review Records and Go/No-Go decisions. It supports the Business Case objective O5 (every step traceable) in [BC-001].

## ARB Review Workflow

1. **Submission** — the artifact owner submits an instance for review,
   identifying its type's QC checklist (`framework/qc/*/qc-*.md`).
2. **QC Checklist Review** — the assigned reviewer (see RACI) applies the
   checklist criterion by criterion.
3. **Review Record** — the reviewer documents the outcome as an SQA Review
   Record (`RC-*` under `docs/sqa/reviews/`).
4. **Go/No-Go Decision** — the Accountable role for the artifact category
   decides; contested or cross-cutting cases escalate to the ARB Chair.
5. **Sign-off** — on **Go**, the artifact's `## Version History` gets an
   `Accepted` row (the previous row becomes `Deprecated`). On **Go-with-conditions**, status stays `Proposed` until
   the Action Items are closed. On **No-Go**, the artifact returns to its
   owner.
6. **Traceability Update** — the Traceability Matrix is updated with the
   instance and its `RC-*` reference.

## RACI by Artifact Category

Every cell is a stakeholder ID from the Stakeholder Analysis, never a role name. S01 is the only person with power over the project, so S01 is Accountable in every category.

| Artifact Category | Responsible (runs the review) | Accountable (Go/No-Go owner) | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Strategic (Stakeholder Analysis, Business Case) | S01 | S01 | S02 | S03 |
| Process/Business (Project Plan, Milestones/Gateways, Dictionary, Governance) | S01 | S01 | S02 | S03 |
| Documentation (README, wiki) | S01 | S01 | S02 | S03 |
| Code (source code and tests) | S01 | S01 | S02 | S03 |

Cross-cutting escalations and disputed verdicts are Accountable to the ARB
Chair (`S01`), overriding the category-level Accountable role.

## Escalation Rules

- A **No-Go** verdict, or any disagreement between the Responsible reviewer
  and the category's Accountable owner, escalates to the ARB Chair.
- A reviewer may not review an instance they authored; the alternate reviewer is S01. The one exception is
  autonomous mode: the AI may act as stand-in for a reviewer or an Accountable
  role, recorded as `AI as stand-in for <S-ID>` and `Mode: autonomous, not
  independent`; the Product Owner's acceptance of the plan is the
  authorisation for it.
- Repeated No-Go verdicts (2 or more) on the same artifact type trigger a
  review of the corresponding `QC-*` checklist itself.

## Cadence

- Reviews are triggered per artifact instance as it is produced or revised.
- QC checklists are reviewed annually.
- A blocking finding (a `Fail` on a Mandatory criterion) gives `No-Go`; `Go-with-conditions` is only for findings that do not block. A criterion only a person can confirm stays `Pending` until S01 confirms it; a stand-in never closes it. No risk exception is planned.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[109e51b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/commit/109e51b66de566b81925c85b7a93dcf006cf5b95
