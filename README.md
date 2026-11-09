# 🚀 TinDog: Bootstrap on Day 58

Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*, Day 58: the Bootstrap lectures and the TinDog landing page, served by a small Python 3.13 program with no runtime dependencies.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

Day 58 teaches Bootstrap, a CSS toolkit built on a 12-column grid. This repository rebuilds the three lecture steps as static pages and serves them from Python:

| Part | What it is for |
| --- | --- |
| `src/tindog/` | The Python package: `constants.py`, the layers (`domain`, `application`, `infrastructure`, `presentation`) and the lecture pages in `site/` |
| `tests/` | `pytest` tests |
| `docs/` | Project documents (Business Case, plan, milestones, reviews) |
| `Doxyfile` | Configuration for the Doxygen reference of the source |

## 📋 Requirements

- Python 3.13 or newer, to run the code and the tests.
- A web browser, to look at the pages. The pages load Bootstrap from a CDN, so the browser needs internet access.
- Doxygen (optional), to build the source reference.

There are no runtime dependencies. `pytest` is the only development dependency.

## 🛠️ Setup

Create a local virtual environment named `.venv`, activate it, upgrade `pip` and install the project with its test tool.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run `deactivate` to leave the environment. The `.venv` folder is ignored by git.

## ▶️ Run

The lecture pages are added in the next milestones; this section is completed there.

## 🧪 Tests

With the environment active:

```bash
python -m pytest
```

## 📄 License

GNU Affero General Public License v3.0 or later, see [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Domain dictionary][DICT-001] | The PO terms and the IT terms |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Governance][GOV-001] | The review workflow, who decides and how disputes escalate |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/issues
[license]: ./LICENSE
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[DICT-001]: ./docs/dictionary.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[GOV-001]: ./docs/sqa/governance.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
