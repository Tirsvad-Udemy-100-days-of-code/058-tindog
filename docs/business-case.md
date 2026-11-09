# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Executive Summary

Day 58 of Udemy's 100 Days of Code asks the participant to learn Bootstrap and build the "TinDog" landing page, a start-up site that matches dogs with friends. This project delivers that assignment as a runnable, documented Python 3.13+ repository: the Bootstrap lessons rebuilt as static pages, a small standard-library Python server and tests, a README with a screenshot per lecture step, and a wiki in English, Danish and Bahasa Malaysia that explains what each step taught. The result is a learning record for S01 and a readable reference for S02 and S03.

## Methodological and Standards Foundation

The work follows the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, `RC-*` records) and Larman's *Applying UML and Patterns* where a design artifact is needed. Quality characteristics follow ISO/IEC 25010:2023. Python code follows the `coding-conventions` skill and the `qc-programming-python` checklist; the structure follows the `clean-architecture` skill.

## Problem Statement

- The Udemy exercise is delivered as a zip of HTML, CSS and images with no repository, no tests and no run instructions, so a learner cannot show or reproduce the result.
- Learners compare solutions, but a solution without a README, screenshots or an explanation shows what was built, not what was learned.
- A Python bootcamp assignment about a front-end toolkit has no Python in it, so it does not fit the rest of the course repositories.

## Business Opportunity

A small, tidy repository can make the lesson reproducible with one command, show every lecture step as a screenshot, and explain the lessons in three languages. It also adds to the public portfolio of course repositories that S03 browses.

## Objectives

1. **O1** Rebuild the three Day 58 lecture steps (Bootstrap introduction, Bootstrap components with the "Move It" page, the TinDog project) as runnable pages.
2. **O2** Provide a Python 3.13+ project (`pyproject.toml`, `.venv`, `pytest`, `constants.py`, Doxygen comments, `Doxyfile`) that serves the pages and is covered by tests.
3. **O3** Show one screenshot per lecture step in the README and in the wiki.
4. **O4** Publish a wiki in English, Danish and Bahasa Malaysia that explains what each lecture step taught.
5. **O5** Give the repository on the git host a description and topics, and keep every step traceable through branches and pull requests.

## Scope

### In Scope

- Static pages for lecture steps 1 to 3 under `src/`, using Bootstrap from a CDN.
- A standard-library Python module that serves the pages locally, with `constants.py`.
- `pyproject.toml`, Python `.gitignore`, `Doxyfile`, `README.md` from the framework template, and `.venv` instructions including `python -m pip install --upgrade pip`.
- `pytest` tests in `tests/`.
- Screenshots per lecture step, taken headless in a Docker container.
- A wiki in `docs/wiki/` in English, Danish and Bahasa Malaysia.
- Repository description and topics on the git host.
- The project documents the framework requires (Business Case, Stakeholder Analysis, Project Plan, milestones, review records).

### Out of Scope

- A backend, database, user accounts or a real matching service for TinDog.
- Deployment or hosting of the site.
- Bootstrap themes, paid or custom, and a custom build of Bootstrap.
- Runtime Python dependencies beyond the standard library.
- Testing a GUI on the host desktop (`framework/process/gui-testing.md`).

## Expected Benefits

### Tangible Benefits

- A repository that runs with documented commands and passes its tests.
- Three README screenshots and a three-language wiki per lecture step.
- A described, tagged repository that S03 can find.

### Intangible Benefits

- A durable record of what Bootstrap's grid, components and utilities taught.
- A repeatable pattern (plan, branch, review, pull request) for the next course day.

## Strategic Alignment

The project supports S01's goal of finishing the 100 Days of Code course with a clean public repository per day, and keeps each repository consistent with the framework's planning and review rules.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Pages for the 3 lecture steps are served | 3 of 3 pages answer HTTP 200 | `pytest` result |
| 2 | Tests pass on Python 3.13 | 100 % of tests pass | `python -m pytest` exit code 0 |
| 3 | Runtime dependencies | 0 packages in `[project].dependencies` | `pyproject.toml` |
| 4 | Screenshots | 3 images, one per lecture step, in the README and in every wiki language | file count in `docs/images/` and links in README and wiki |
| 5 | Wiki languages | 3 languages, same page set | files `<Page>.md`, `<Page>-da.md`, `<Page>-ms.md` |
| 6 | Repository metadata | description set and at least 5 topics | git host API response |
| 7 | Pull requests | 1 pull request per milestone, each closing its issues | git host PR list |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Udemy download link has expired or the files differ from the lecture | The TinDog assets cannot be reused | Rebuild the pages from the lecture description and use own placeholder images; record the difference in the milestone |
| The Bootstrap CDN or the network is unavailable when screenshots are taken | Screenshots cannot be produced | Take screenshots in Docker with network access; retry; fall back to a pinned local copy only if the CDN stays down |
| Udemy course material is copyrighted | Publishing the original files could breach terms | Do not commit the downloaded zip or its images; write own markup and use own or generated images |
| Danish or Bahasa Malaysia text contains errors | Misleading wiki pages | English is authoritative; translations follow it page by page; S01 reviews them |
| Tokens in `.env` leak | Account compromise | `.env` is ignored by git, never read into the project, never printed or put on a command line |

## Assumptions

- S01 is the Product Owner, developer and reviewer; in autonomous mode the AI is S01's stand-in for reviews, recorded as such.
- Docker is available on the host for headless screenshots.
- The git host accepts the token in `.env` for pushes, pull requests, description, topics, issues and the wiki.
- The wiki is enabled in the repository settings.

## Constraints

- Python 3.13 or newer, `venv`, `pytest`, constants in `constants.py`, `pyproject.toml` for configuration.
- Source in `src/`, tests in `tests/`, documents in `docs/`.
- Doxygen comments in the source and a `Doxyfile`.
- No runtime dependencies unless needed.
- The PO language is English and the domain is IT.
- One branch and one pull request per milestone.

## Cost–Benefit Assessment

The justification is qualitative because the project is a personal learning exercise with no revenue; the cost is S01's time and the benefit is a reusable learning record.

| Costs | Benefits |
| --- | --- |
| About 2 to 3 hours of S01 review time plus AI work | A reproducible, tested and documented Day 58 solution |
| Docker image pull for screenshots | Three-language explanation of the lesson |
| No licence or hosting cost | A tagged repository visible to S02 and S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Finish the assignment, own the scope, review and accept the results |
| S02 | Readable, runnable code with the assignment's names and README instructions |
| S03 | Clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, every objective is verifiable, and the risks have mitigations.

---

[SA-001]: ./stakeholder-analysis.md
