"""@file test_index_page.py
@brief Tests for the index page renderer.
"""

from tindog import constants
from tindog.application.list_lessons import list_lessons
from tindog.domain.lesson import Lesson
from tindog.presentation.index_page import render_index


def test_index_links_to_every_lesson() -> None:
    html = render_index(list_lessons())
    for lesson in list_lessons():
        assert f'href="{lesson.url_path}"' in html


def test_index_references_bootstrap_css() -> None:
    assert constants.BOOTSTRAP_CSS_URL in render_index(list_lessons())


def test_index_escapes_html_in_titles() -> None:
    html = render_index((Lesson(1, "x", "<script>alert(1)</script>", "f"),))
    assert "<script>" not in html
    assert "&lt;script&gt;" in html
