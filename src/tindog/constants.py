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
