"""@file test_lesson.py
@brief Tests for the Lesson value object, the list_lessons use case and the CLI parser.
"""

import dataclasses

import pytest

from tindog import constants
from tindog.application.list_lessons import list_lessons
from tindog.domain.lesson import Lesson
from tindog.presentation.cli import build_parser


def test_url_path_starts_with_slash_and_points_to_the_page() -> None:
    lesson = Lesson(1, "slug", "Title", "folder-a")
    assert lesson.url_path == f"/folder-a/{constants.LESSON_PAGE_NAME}"


def test_lesson_is_immutable() -> None:
    lesson = Lesson(1, "slug", "Title", "folder-a")
    with pytest.raises(dataclasses.FrozenInstanceError):
        lesson.number = 2  # type: ignore[misc]


def test_list_lessons_returns_lessons_ordered_by_number() -> None:
    numbers = [lesson.number for lesson in list_lessons()]
    assert numbers == sorted(numbers)


def test_list_lessons_matches_the_constants() -> None:
    rows = {(x.number, x.slug, x.title, x.folder) for x in list_lessons()}
    assert rows == set(constants.LESSON_DATA)


def test_parser_defaults_come_from_constants() -> None:
    args = build_parser().parse_args([])
    assert (args.host, args.port) == (constants.DEFAULT_HOST, constants.DEFAULT_PORT)


def test_parser_accepts_host_and_port() -> None:
    args = build_parser().parse_args(["--host", "0.0.0.0", "--port", "9000"])
    assert (args.host, args.port) == ("0.0.0.0", 9000)
