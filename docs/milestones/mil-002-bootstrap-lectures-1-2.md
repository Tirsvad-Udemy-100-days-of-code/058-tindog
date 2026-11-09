# MIL-002 Bootstrap lectures 1 and 2

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether lecture steps 1 (Bootstrap introduction) and 2 (Bootstrap components, the "Move It" page) are rebuilt as pages that a local Python server serves and tests cover.

## Deliverable

A lesson catalogue and a standard-library HTTP server in `src/tindog/`, the pages for lecture steps 1 and 2 under `src/tindog/site/`, and `pytest` tests for both.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The server answers HTTP 200 for the index and for the pages of lecture steps 1 and 2 | The tests assert it and pass | A test fails |
| 2 | The server answers 404 for an unknown path and refuses a path outside the site folder | The tests assert both and pass | A test fails |
| 3 | Each page loads Bootstrap from a CDN and uses the components the lecture names (buttons, card, navbar, carousel, footer) | The markup tests pass | A test fails |
| 4 | Constants (host, port, paths, CDN URLs) are in `constants.py` only | `grep` finds no literal duplicate elsewhere | A duplicate is found |
| 5 | The code review against `qc-programming-python` has no blocking finding | `RC-*` says `Go` | `RC-*` says `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | The package skeleton, configuration and `tests/` must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2 | [BC-001] |
| Success criteria 1, 2, 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — one day after MIL-001, within the one-pull-request-per-milestone constraint.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the lesson catalogue | Add a `Lesson` value object in the domain layer and a use case that lists the lessons (title, slug, folder), with the lesson data in `constants.py`. S02 reads this to see which lecture step each page belongs to. | No | |
| 2 | Add the local HTTP server | Add a standard-library server in the infrastructure layer with `serve()` and `main()`, that serves `src/tindog/site/`, returns 404 for unknown paths and refuses path traversal. No runtime dependency is added. | No | |
| 3 | Build the lecture 1 page | Build the Bootstrap introduction page: the CDN link, a button, a card and a short explanation of the 12-column grid, as the lecture shows. | No | |
| 4 | Build the lecture 2 "Move It" page | Build the one-page site for the fictional start-up Move It: navbar with dropdown and search, hero, features, carousel, footer, containers, and dark mode through `data-bs-theme`. | No | |
| 5 | Test the server and the pages | Write `pytest` tests for the catalogue, the server (200, 404, traversal) and the page markup for both lecture steps. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-repository-foundation.md
