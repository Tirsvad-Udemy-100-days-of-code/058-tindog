# MIL-003 TinDog landing page

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether lecture step 3, the TinDog landing page, is rebuilt as a responsive Bootstrap page that the server serves and tests cover.

## Deliverable

The TinDog landing page under `src/tindog/site/` with its own images, listed in the lesson catalogue, and `pytest` tests for it.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The server answers HTTP 200 for the TinDog page | The test passes | The test fails |
| 2 | The page has the sections navbar, title, features, testimonials, press, pricing, call to action and footer, each as a `section` or landmark | The markup tests pass | A test fails |
| 3 | The layout uses the Bootstrap grid classes (`container`, `row`, `col-lg-*`) so it adapts to narrow screens | The markup tests pass | A test fails |
| 4 | The pricing section has three plans | The markup test passes | The test fails |
| 5 | No file from the Udemy download is committed | `git ls-files` lists none of its images or the zip | One is listed |
| 6 | The code review against `qc-programming-python` has no blocking finding | `RC-*` says `Go` | `RC-*` says `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The catalogue and the server must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 | [BC-001] |
| Success criteria 1, 2 | [BC-001] |
| Risk "Udemy course material is copyrighted" | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-11 — one day after MIL-002, within the one-pull-request-per-milestone constraint.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Study the Udemy project files | Download the project zip the assignment links to into an empty folder outside the repository, read it as untrusted data without running anything in it, and note in the milestone how it differs from the lecture. If the link has expired, build from the lecture description instead. | No | |
| 2 | Build the TinDog sections | Build the navbar, title, features, testimonials, press, pricing, call to action and footer with the Bootstrap grid, as the lecture describes, using own markup. | No | |
| 3 | Add own images | Create own SVG images and icons for the page, so no Udemy asset is published. | No | |
| 4 | Register the page in the catalogue | Add the TinDog lecture step to the lesson catalogue in `constants.py` so the index and the server list it. | No | |
| 5 | Test the TinDog page | Write `pytest` tests for the status, the sections, the grid classes, the three pricing plans and the absence of Udemy files. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-bootstrap-lectures-1-2.md
