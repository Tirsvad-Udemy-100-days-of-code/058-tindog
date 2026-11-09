"""@file list_lessons.py
@brief Use case: list the lecture steps in course order.
"""

from tindog.constants import LESSON_DATA
from tindog.domain.lesson import Lesson


def list_lessons() -> tuple[Lesson, ...]:
    """@brief Return every lecture step, ordered by its number."""
    lessons = (Lesson(*row) for row in LESSON_DATA)
    return tuple(sorted(lessons, key=lambda lesson: lesson.number))
