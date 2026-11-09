"""@file index_page.py
@brief Renders the index page that links to every lecture step.
"""

from html import escape

from tindog.constants import (
    BOOTSTRAP_CSS_INTEGRITY,
    BOOTSTRAP_CSS_URL,
    INDEX_TITLE,
)
from tindog.domain.lesson import Lesson


def _link_item(lesson: Lesson) -> str:
    return f'      <a class="list-group-item list-group-item-action" href="{escape(lesson.url_path)}">Lecture step {lesson.number}: {escape(lesson.title)}</a>'


def render_index(lessons: tuple[Lesson, ...]) -> str:
    """@brief Return the HTML of the index page for the given lessons."""
    items = "\n".join(_link_item(lesson) for lesson in lessons)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(INDEX_TITLE)}</title>
  <link rel="stylesheet" href="{BOOTSTRAP_CSS_URL}" integrity="{BOOTSTRAP_CSS_INTEGRITY}" crossorigin="anonymous">
</head>
<body>
  <main class="container py-5">
    <h1 class="mb-4">{escape(INDEX_TITLE)}</h1>
    <div class="list-group">
{items}
    </div>
  </main>
</body>
</html>
"""
