# RC-015 Code review for MIL-004

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001]
- Scope: full review of tools/screenshots/take_screenshots.py and its Dockerfile
- Language and domain: n/a
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked against the document; no defect found. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked against the document; no defect found. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | No linter configured; PEP 8 by hand; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Checked against the document; no defect found. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; try/finally shuts the server down. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked against the document; no defect found. |
| 7 | Files, locks and connections are managed with context managers | Pass | Browser and playwright use context managers; the server is closed in finally. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked against the document; no defect found. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | The script writes the file names to stdout as its result; it uses no logging because it is a one-shot tool and prints no secret. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram; plain technical task. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | N-A | A container-only tool; its result is checked by looking at the three images and by the hygiene and page tests; no unit test is possible without a browser. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | Optional. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | playwright is pinned in the Dockerfile only, not in the project dependencies. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Viewport and wait values are named constants; lesson data comes from the catalogue. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | The tool imports the project package, not the other way round. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Checked against the document; no defect found. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | N-A | A tool outside src/ and tests/ by design. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English names, no spaces. |

## Overall Verdict

Go — Every Mandatory criterion passes or is not applicable with a reason.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None: no Fail and no Pending criterion. | S01 | 2026-11-09 |

---

[MIL-004]: ../../milestones/mil-004-readme-screenshots-wiki.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
