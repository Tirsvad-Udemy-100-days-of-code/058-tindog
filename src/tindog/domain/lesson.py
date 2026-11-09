"""@file lesson.py
@brief The Lesson value object: one lecture step of the course day.
"""

from dataclasses import dataclass

from tindog.constants import LESSON_PAGE_NAME


@dataclass(frozen=True, slots=True)
class Lesson:
    """@brief One lecture step with its own page.

    @param number Position of the step in the course day, starting at 1.
    @param slug Short lowercase name used in file names and wiki pages.
    @param title Human readable title.
    @param folder Folder, inside the site folder, that holds the page.
    """

    number: int
    slug: str
    title: str
    folder: str

    @property
    def url_path(self) -> str:
        """@brief URL path of the lesson page, starting with a slash."""
        return f"/{self.folder}/{LESSON_PAGE_NAME}"
