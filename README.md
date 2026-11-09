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
| `tools/screenshots/` | Dockerfile and script that take the screenshots in a container |
| `docs/images/`, `docs/wiki/` | The screenshots and the wiki (English, Danish, Bahasa Malaysia) |
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

With the environment active, start the local server and open the address it prints:

```bash
python -m tindog
```

The index page is at `http://127.0.0.1:8058/` and links to the three lecture steps. Use `--host` and `--port` to change the address. Stop the server with `Ctrl+C`.

### Lecture step 1: Bootstrap introduction

Buttons, a card and the 12-column grid. Page: [`lecture-1-bootstrap-introduction`](src/tindog/site/lecture-1-bootstrap-introduction/index.html).

![Lecture step 1: Bootstrap introduction][shot-1]

### Lecture step 2: Bootstrap components, "Move It"

A one-page site with a navbar, dropdown, search, hero, cards, carousel, footer and dark mode. Page: [`lecture-2-bootstrap-components`](src/tindog/site/lecture-2-bootstrap-components/index.html).

![Lecture step 2: the Move It page][shot-2]

### Lecture step 3: the TinDog landing page

A responsive landing page with title, features, testimonial, press, pricing, call to action and footer. Page: [`lecture-3-tindog`](src/tindog/site/lecture-3-tindog/index.html).

![Lecture step 3: the TinDog landing page][shot-3]

What each step taught is explained in the [wiki][documentation] in English, Danish and Bahasa Malaysia.

The screenshots are taken in a Docker container, not on the desktop:

```bash
docker build -t tindog-screenshots -f tools/screenshots/Dockerfile .
docker run --rm -v "$(pwd)/docs/images:/work/docs/images" tindog-screenshots
```

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
[shot-1]: ./docs/images/lecture-1-bootstrap-introduction.png
[shot-2]: ./docs/images/lecture-2-bootstrap-components.png
[shot-3]: ./docs/images/lecture-3-tindog.png
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
