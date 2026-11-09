"""@file take_screenshots.py
@brief Takes one full-page screenshot per lecture step, inside a Docker container.

Run through `docker run` (see tools/screenshots/Dockerfile); never on the host
desktop (framework/process/gui-testing.md). The browser tooling lives in the
image and is not a dependency of the project.
"""

import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

from tindog.application.list_lessons import list_lessons
from tindog.infrastructure.http_server import create_server
from tindog.presentation.index_page import render_index

## @brief Browser window width in pixels (a typical laptop screen).
VIEWPORT_WIDTH = 1280

## @brief Browser window height in pixels.
VIEWPORT_HEIGHT = 800

## @brief Milliseconds to wait for the CDN and the page to settle.
SETTLE_MS = 1500


def take_screenshots(output_dir: Path) -> list[Path]:
    """@brief Serve the site on a free port and photograph every lesson page.

    @param output_dir Folder that receives `<lesson folder>.png` files.
    @return The files written, in lesson order.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    lessons = list_lessons()
    server = create_server(render_index(lessons), port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    port = server.server_address[1]
    written: list[Path] = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT})
            for lesson in lessons:
                page.goto(f"http://127.0.0.1:{port}{lesson.url_path}", wait_until="networkidle")
                page.wait_for_timeout(SETTLE_MS)
                target = output_dir / f"{lesson.folder}.png"
                page.screenshot(path=str(target), full_page=True)
                written.append(target)
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    return written


def main(argv: list[str]) -> int:
    """@brief Entry point: the first argument is the output folder."""
    output_dir = Path(argv[1]) if len(argv) > 1 else Path("docs/images")
    for path in take_screenshots(output_dir):
        sys.stdout.write(f"{path}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
