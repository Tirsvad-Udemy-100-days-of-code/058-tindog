# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This analysis identifies who has a stake in the Day 58 TinDog project and what each needs, so that the Business Case, plan and documents use stable stakeholder IDs. It uses the power/interest grid (Manage Closely, Keep Satisfied, Keep Informed, Monitor) and maps concerns to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Complete the assignment with a clean, correct and well-explained repository |
| S02 | Udemy coursists | Fellow learners who share code and compare solutions | Udemy 100 Days of Code community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact, and is also the developer. Power and interest are both high.
- **Keep Informed (S02, S03):** they cannot change the scope but they judge the result. S02 has high interest because they compare solutions; S03 has medium interest because they browse briefly. Both are served by the README, wiki and repository metadata.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The three lecture steps are rebuilt and each is explained | Functionality |
| CN-002 | S01 | Every step is planned, reviewed and traceable through branches and pull requests | Supportability |
| CN-003 | S01 | The tokens in the local environment file stay private | Functionality (security) |
| CN-004 | S02 | The code is readable and keeps the assignment's function names | Supportability |
| CN-005 | S02 | The project runs after following the README, and the tests pass | Usability |
| CN-006 | S03 | The repository has a clear description, topics and README | Usability |
| CN-007 | S03 | Installing needs no runtime dependencies | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| COM-001 | Chat with S01 | At plan acceptance and at the end of the run | Plan dry run, then run summary with `RC-*` verdicts and stand-in decisions | All milestones |
| COM-002 | Pull request on the git host | One per milestone | Changes, closed issues, checks | All milestones |
| COM-003 | README and wiki | At the last milestone | Run instructions, screenshots, lessons in en, da, ms | MIL-004 |
| COM-004 | Repository description and topics | Once | Description and topics on the git host | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants rich explanations in three languages; S03 wants a short, scannable README | S01, S03 | The README stays short with screenshots and run steps; the longer explanations are in the wiki |
| S02 wants the assignment's names; clean code conventions prefer other names | S01, S02 | Keep the course names where the course defines them (for example `index.html`, `css/styles.css`) and follow conventions elsewhere |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | O1 in [BC-001] |
| S01 | CN-002 | O5 in [BC-001] |
| S01 | CN-003 | Risk "Tokens in `.env` leak" in [BC-001] |
| S02 | CN-004 | O2 in [BC-001] |
| S02 | CN-005 | O2 in [BC-001] |
| S03 | CN-006 | O3 and O5 in [BC-001] |
| S03 | CN-007 | O2 in [BC-001] |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Accepted by the AI as stand-in for S01 under autonomous mode, once the user accepts the plan | 2026-11-09 |

---

[BC-001]: ./business-case.md
