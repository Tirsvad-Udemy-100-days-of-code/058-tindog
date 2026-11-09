"""@file test_lesson_pages.py
@brief Markup tests for the static lecture pages, using the standard html.parser.
"""

from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

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


TINDOG_LESSON = 3
TINDOG_SECTION_IDS = ("title", "features", "testimonial", "press", "pricing", "cta")


def lesson_folder(number: int) -> Path:
    folder = next(row[3] for row in constants.LESSON_DATA if row[0] == number)
    return constants.SITE_DIR / folder


def is_relative(reference: str) -> bool:
    return not urlparse(reference).scheme and not reference.startswith(("/", "#"))


@pytest.fixture(params=[1, 2, 3], ids=["lesson-1", "lesson-2", "lesson-3"])
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


@pytest.mark.parametrize("section_id", TINDOG_SECTION_IDS)
def test_lesson_3_has_section_element_with_id(section_id: str) -> None:
    matches = [e for e in parse(TINDOG_LESSON).with_tag("section") if e.attrs.get("id") == section_id]
    assert len(matches) == 1


def test_lesson_3_has_footer_element() -> None:
    assert parse(TINDOG_LESSON).with_tag("footer")


def test_lesson_3_uses_the_bootstrap_grid() -> None:
    page = parse(TINDOG_LESSON)
    assert page.with_class("container") or page.with_class("container-fluid")
    assert page.with_class("row")
    assert [e for e in page.elements if any(c.startswith("col-lg-") for c in e.classes)]


def test_lesson_3_pricing_has_exactly_three_cards() -> None:
    folder = lesson_folder(TINDOG_LESSON)
    text = (folder / constants.LESSON_PAGE_NAME).read_text(encoding="utf-8")
    start = text.index('<section id="pricing"')
    end = text.index("</section>", start)
    collector = _Collector()
    collector.feed(text[start:end])
    assert len(collector.page.with_class("card")) == 3


def test_lesson_3_every_image_has_alt_text() -> None:
    images = parse(TINDOG_LESSON).with_tag("img")
    assert images
    assert all(e.attrs.get("alt", "").strip() for e in images)


def test_lesson_3_relative_references_resolve_to_files() -> None:
    page = parse(TINDOG_LESSON)
    images = [e.attrs["src"] for e in page.with_tag("img") if "src" in e.attrs]
    styles = [e.attrs["href"] for e in page.with_tag("link") if e.attrs.get("rel") == "stylesheet"]
    relative = [ref for ref in images + styles if is_relative(ref)]
    assert any(ref.endswith(".css") for ref in relative)
    assert any(ref.endswith(".svg") for ref in relative)
    missing = [ref for ref in relative if not (lesson_folder(TINDOG_LESSON) / ref).is_file()]
    assert missing == []
