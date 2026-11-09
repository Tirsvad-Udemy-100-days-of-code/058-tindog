"""@file constants.py
@brief Constants shared by the whole tindog package.

Every literal that more than one module needs, or that a reader may want to
change, is defined here once.
"""

from pathlib import Path

## @brief Name of the Python package and of the command line program.
PACKAGE_NAME = "tindog"

## @brief Host the local server binds to by default (this machine only).
DEFAULT_HOST = "127.0.0.1"

## @brief Port the local server listens on by default.
DEFAULT_PORT = 8058

## @brief Folder, inside the package, that holds the static lecture pages.
SITE_DIR_NAME = "site"

## @brief Absolute path to the folder that holds the static lecture pages.
SITE_DIR = Path(__file__).resolve().parent / SITE_DIR_NAME

## @brief Bootstrap version used by every lecture page.
BOOTSTRAP_VERSION = "5.3.3"

## @brief CDN address of the Bootstrap stylesheet.
BOOTSTRAP_CSS_URL = (
    f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/css/bootstrap.min.css"
)

## @brief CDN address of the Bootstrap script bundle (includes Popper).
BOOTSTRAP_JS_URL = (
    f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/js/bootstrap.bundle.min.js"
)

## @brief Subresource integrity hash of the Bootstrap stylesheet.
BOOTSTRAP_CSS_INTEGRITY = "sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"

## @brief Subresource integrity hash of the Bootstrap script bundle.
BOOTSTRAP_JS_INTEGRITY = "sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"

## @brief The lecture steps as (number, slug, title, folder in the site folder).
LESSON_DATA: tuple[tuple[int, str, str, str], ...] = (
    (1, "bootstrap-introduction", "Bootstrap introduction", "lecture-1-bootstrap-introduction"),
    (2, "bootstrap-components", "Bootstrap components: Move It", "lecture-2-bootstrap-components"),
    (3, "tindog-landing-page", "The TinDog landing page", "lecture-3-tindog"),
)

## @brief Name of the page file inside each lesson folder.
LESSON_PAGE_NAME = "index.html"

## @brief Title of the generated index page.
INDEX_TITLE = "TinDog: Bootstrap on Day 58"
