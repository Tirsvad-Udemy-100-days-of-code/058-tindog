"""@file test_lesson_pages.py
@brief Markup tests for the static lecture pages, using the standard html.parser.
"""

from dataclasses import dataclass, field
from html.parser import HTMLParser

import pytest

from tindog import constants


@dataclass
class Element:
    tag: str
    attrs: dict[str, str]

    @property
    def classes(self) -> set[str]:
        return set(self.attrs.get("class", "").split())


@dataclass
class Page:
    elements: list[Element] = field(default_factory=list)

    def with_class(self, name: str) -> list[Element]:
        return [e for e in self.elements if name in e.classes]

    def with_tag(self, tag: str) -> list[Element]:
        return [e for e in self.elements if e.tag == tag]


class _Collector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.page = Page()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.page.elements.append(Element(tag, {k: v or "" for k, v in attrs}))


def parse(number: int) -> Page:
    folder = next(row[3] for row in constants.LESSON_DATA if row[0] == number)
    text = (constants.SITE_DIR / folder / constants.LESSON_PAGE_NAME).read_text(encoding="utf-8")
    collector = _Collector()
    collector.feed(text)
    return collector.page


@pytest.fixture(params=[1, 2], ids=["lesson-1", "lesson-2"])
def page(request: pytest.FixtureRequest) -> Page:
    return parse(request.param)


def test_page_has_lang_and_viewport(page: Page) -> None:
    assert page.with_tag("html")[0].attrs.get("lang")
    assert [e for e in page.with_tag("meta") if e.attrs.get("name") == "viewport"]


def test_page_loads_bootstrap_css_with_integrity(page: Page) -> None:
    links = [e for e in page.with_tag("link") if e.attrs.get("href") == constants.BOOTSTRAP_CSS_URL]
    assert links
    assert links[0].attrs.get("integrity") == constants.BOOTSTRAP_CSS_INTEGRITY


def test_page_loads_bootstrap_js_with_integrity(page: Page) -> None:
    scripts = [e for e in page.with_tag("script") if e.attrs.get("src") == constants.BOOTSTRAP_JS_URL]
    assert scripts
    assert scripts[0].attrs.get("integrity") == constants.BOOTSTRAP_JS_INTEGRITY


def test_lesson_1_has_success_button() -> None:
    assert [e for e in parse(1).with_class("btn") if "btn-success" in e.classes]


def test_lesson_1_has_a_card() -> None:
    assert parse(1).with_class("card")


def test_lesson_1_has_row_with_three_medium_columns() -> None:
    page = parse(1)
    columns = [e for e in page.elements if any(c.startswith("col-md-") for c in e.classes)]
    assert page.with_class("row")
    assert len(columns) >= 3


def test_lesson_2_has_navbar() -> None:
    assert [e for e in parse(2).with_class("navbar") if e.tag == "nav"]


def test_lesson_2_has_dropdown_menu() -> None:
    assert parse(2).with_class("dropdown-menu")


def test_lesson_2_has_search_form() -> None:
    assert [e for e in parse(2).with_tag("form") if e.attrs.get("role") == "search"]


def test_lesson_2_has_carousel_with_three_items() -> None:
    page = parse(2)
    assert page.with_class("carousel")
    assert len(page.with_class("carousel-item")) >= 3


def test_lesson_2_has_footer_and_container() -> None:
    page = parse(2)
    assert page.with_tag("footer")
    assert page.with_class("container")


def test_lesson_2_sets_bootstrap_theme_on_html() -> None:
    assert "data-bs-theme" in parse(2).with_tag("html")[0].attrs


def test_lesson_2_has_hero_and_features_sections() -> None:
    ids = {e.attrs.get("id") for e in parse(2).elements}
    assert {"hero", "features"} <= ids
