# MIL-004 README, screenshots and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the project is ready for S02 and S03: a screenshot per lecture step, a complete README, and a wiki in English, Danish and Bahasa Malaysia that explains what each step taught.

## Deliverable

Three screenshots in `docs/images/`, the final `README.md` with them, a screenshot script that runs in a Docker container, and the wiki pages in `docs/wiki/` in three languages.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/images/` holds one screenshot per lecture step (3 files) and the README shows each | 3 files and 3 image links | Fewer files or links |
| 2 | The screenshots were taken in a Docker container, not on the host desktop | The script and the task notes show the container | The host desktop was used |
| 3 | The wiki has the same page set in `<Page>.md`, `<Page>-da.md` and `<Page>-ms.md`, each with the language line | The file list matches for 3 languages | A page is missing in a language |
| 4 | Each wiki lecture page contains the screenshot and a section on what the step taught | Present in 3 languages | Missing in a language |
| 5 | `_Sidebar.md` follows `framework/process/wiki.md` | The reviewer finds the shape | The shape differs |
| 6 | `bash framework/scripts/check-readme.sh` passes and the README runs the project as written | Exit code 0 and the commands work | Either fails |
| 7 | The wiki review against `QC-WIKI-001` has no blocking finding | `RC-*` says `Go` | `RC-*` says `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | All three pages must exist before they are photographed and explained |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, O4 | [BC-001] |
| Success criteria 4, 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 — the last day of the plan, within the Business Case constraint of one pull request per milestone.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the screenshot script | Add a Dockerfile and a script that start the server and take a full-page screenshot of each lecture page in a headless browser inside a Docker container, so the host desktop is not used (`framework/process/gui-testing.md`). The browser tooling stays in the image and is not a project dependency. | No | |
| 2 | Take the three screenshots | Run the script and save one screenshot per lecture step in `docs/images/`; check each image shows its page. | No | |
| 3 | Finish the README | Add the screenshot of each lecture step, complete the run and test instructions and the document appendix, and run `check-readme.sh`. | No | |
| 4 | Write the English wiki | Write `Home`, one page per lecture step with its screenshot and what the step taught, `Running-the-Project`, and `_Sidebar` in `docs/wiki/`. | No | |
| 5 | Write the Danish wiki | Translate every English page into Danish as `<Page>-da.md`, with the language line. | No | |
| 6 | Write the Bahasa Malaysia wiki | Translate every English page into Bahasa Malaysia as `<Page>-ms.md`, with the language line. | No | |
| 7 | Check the Doxygen output | Run `doxygen Doxyfile` if Doxygen is installed, or in a container, and fix any warning from the comments. | No | |

---

[BC-001]: ../business-case.md
[MIL-003]: ./mil-003-tindog-landing-page.md
