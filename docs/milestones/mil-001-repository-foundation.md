# MIL-001 Repository foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the repository is ready to hold lecture code: a Python 3.13+ project skeleton exists, the required project documents are accepted, and the repository on the git host is described and tagged.

## Deliverable

A repository with `pyproject.toml`, a Python `.gitignore`, `src/tindog/` with `constants.py` and the layer folders, `tests/`, a `Doxyfile`, a first `README.md` with the `.venv` instructions, the project documents (dictionary, traceability matrix, governance), and a repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` has `requires-python = ">=3.13"` and an empty `dependencies` list | Both hold | Either fails |
| 2 | `python -m pytest` runs in a fresh `.venv` | Exit code 0 | Any other exit code |
| 3 | `.env` and `.venv` are ignored by git | `git check-ignore .env .venv` lists both | Either is not listed |
| 4 | The repository has a description and at least 5 topics on the git host | The API returns both | Either is missing |
| 5 | The README follows `framework/templates/README-template.md` and `check-readme.sh` passes | Exit code 0 | Any other exit code |
| 6 | `.env` is not read, imported or printed by any project file | `grep` finds no use under `src/`, `tests/`, `docs/` | A use is found |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway; the Business Case and Stakeholder Analysis are accepted before it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, O5 | [BC-001] |
| Success criteria 2, 3, 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-09 — the first day of the plan, within the Business Case constraint of one pull request per milestone.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Describe and tag the repository | Set the repository description and topics (for example python, bootstrap, bootstrap5, html, css, udemy, 100-days-of-code, tindog) through the git host API, using the token from the local `.env` without reading it into the project. S03 finds the repository through these. | No | |
| 2 | Add project configuration | Create `pyproject.toml` (Python 3.13+, no runtime dependencies, pytest as a dev extra and its configuration) and a Python `.gitignore` that also ignores `.env` and `.venv`. This is the configuration S02 installs from. | No | |
| 3 | Create the package skeleton | Create `src/tindog/` with `constants.py`, the domain, application and infrastructure layer folders as the `clean-architecture` skill describes, and `tests/` with a first passing test, so later milestones add code in place. | No | |
| 4 | Add the Doxyfile | Add a `Doxyfile` that reads `src/` and writes to an ignored folder, and a Doxygen comment style in the first module, as the Business Case requires. | No | |
| 5 | Write the first README | Fill `framework/templates/README-template.md`: overview, requirements, create and use a local `.venv`, `python -m pip install --upgrade pip`, run and test commands, links. Screenshots are added in MIL-004. | No | |
| 6 | Add the project documents | Create the domain dictionary, the traceability matrix and the governance document, review them, and record the prompt log; check the repository visibility to decide whether `docs/ai-prompts/` is ignored. | No | |

---

[BC-001]: ../business-case.md
