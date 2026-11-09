"""@file test_http_server.py
@brief Integration tests: the real server on localhost with an ephemeral port.
"""

import threading
import urllib.error
import urllib.request
from collections.abc import Iterator

import pytest

from tindog import constants
from tindog.application.list_lessons import list_lessons
from tindog.domain.lesson import Lesson
from tindog.infrastructure.http_server import create_server

INDEX_HTML = "<!doctype html><title>test index</title>"
FILE_MARKERS = (b"DEFAULT_PORT", b"[project]", b"setuptools")


@pytest.fixture
def base_url() -> Iterator[str]:
    server = create_server(INDEX_HTML, host=constants.DEFAULT_HOST, port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://{constants.DEFAULT_HOST}:{server.server_address[1]}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def fetch(url: str) -> tuple[int, bytes]:
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as error:
        return error.code, error.read()


def test_root_returns_the_given_index(base_url: str) -> None:
    status, body = fetch(base_url + "/")
    assert status == 200
    assert body.decode("utf-8") == INDEX_HTML


@pytest.mark.parametrize("lesson", list_lessons(), ids=lambda lesson: lesson.slug)
def test_each_lesson_page_is_served(base_url: str, lesson: Lesson) -> None:
    status, body = fetch(base_url + lesson.url_path)
    assert status == 200
    assert b"<html" in body.lower()


@pytest.mark.parametrize(
    "asset",
    ["index.html", "css/styles.css", "images/phone.svg"],
)
def test_tindog_lesson_files_are_served(base_url: str, asset: str) -> None:
    folder = next(row[3] for row in constants.LESSON_DATA if row[1] == "tindog-landing-page")
    status, body = fetch(f"{base_url}/{folder}/{asset}")
    assert status == 200
    assert body


def test_missing_page_returns_404(base_url: str) -> None:
    status, _ = fetch(base_url + "/missing.html")
    assert status == 404


@pytest.mark.parametrize(
    "path",
    ["/../constants.py", "/%2e%2e/constants.py", "/..%2f..%2fpyproject.toml", "/../../pyproject.toml"],
)
def test_path_traversal_never_serves_files_outside_the_site(base_url: str, path: str) -> None:
    status, body = fetch(base_url + path)
    assert status != 200
    assert not any(marker in body for marker in FILE_MARKERS)
