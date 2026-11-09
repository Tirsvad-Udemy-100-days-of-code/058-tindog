# RC-011 Code review for MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [efb18c4] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review of the lesson catalogue, server, CLI, index page and tests added for MIL-002
- Language and domain: n/a
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked against the document; no defect found. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked against the document; no defect found. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | No formatter or linter is configured; PEP 8 followed by hand, one justified noqa (A002, the base-class parameter name) and one justified type: ignore. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Checked against the document; no defect found. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; only KeyboardInterrupt is caught, to stop the server. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked against the document; no defect found. |
| 7 | Files, locks and connections are managed with context managers | Pass | The server is used as a context manager in serve(); tests shut it down in a fixture. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked against the document; no defect found. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | logging is used; grep finds no print call in src or tests; nothing secret is logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; all tasks are plain technical tasks. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 38 tests pass; the integration tests use only 127.0.0.1 and port 0. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | Optional: mypy is not configured. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | dependencies is empty; pytest is a dev extra. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Bootstrap URLs, hashes, host, port and lesson data are defined once in constants.py; the HTML files repeat the CDN URL because static HTML cannot import it, and a test ties them to the constants. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports only constants; application imports domain; infrastructure imports constants; presentation imports the others. No cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One responsibility per module; the server receives the index page instead of importing presentation. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers under src/tindog; tests/unit and tests/integration. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English lowercase with underscores or hyphens. |

## Overall Verdict

Go — Every Mandatory criterion passes or is not applicable with a reason. The reviewing agent read the code but not the checklist file, so this record is the stand-in's own application of the checklist.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Optional follow-up: ignore a query string when matching the root path (`/?x=1`); harmless for this site. | S01 | 2026-11-13 |

---

[MIL-002]: ../../milestones/mil-002-bootstrap-lectures-1-2.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[efb18c4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/commit/efb18c48ca8f36a5c49ad20b90b4387b58c6da36
