"""@file cli.py
@brief Command line entry point: `python -m tindog` and the `tindog` command.
"""

import argparse
import logging
from collections.abc import Sequence

from tindog.application.list_lessons import list_lessons
from tindog.constants import DEFAULT_HOST, DEFAULT_PORT, PACKAGE_NAME
from tindog.infrastructure.http_server import serve
from tindog.presentation.index_page import render_index


def build_parser() -> argparse.ArgumentParser:
    """@brief Build the argument parser."""
    parser = argparse.ArgumentParser(prog=PACKAGE_NAME, description="Serve the Day 58 lecture pages.")
    parser.add_argument("--host", default=DEFAULT_HOST, help="address to bind to (default: %(default)s)")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="port to listen on (default: %(default)s)")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """@brief Parse the arguments and serve the site.

    @param argv Arguments without the program name; None reads sys.argv.
    @return Process exit code.
    """
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    serve(render_index(list_lessons()), args.host, args.port)
    return 0
