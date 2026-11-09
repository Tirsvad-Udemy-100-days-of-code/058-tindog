"""@file http_server.py
@brief Local HTTP server that serves the static lecture pages.
"""

import logging
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from tindog.constants import DEFAULT_HOST, DEFAULT_PORT, SITE_DIR

_LOG = logging.getLogger(__name__)


class SiteRequestHandler(SimpleHTTPRequestHandler):
    """@brief Serves files from one folder and a generated index page.

    The base class resolves every path inside the folder, so a path such as
    `/../secret` cannot leave it.
    """

    def __init__(self, *args: object, index_html: str, **kwargs: object) -> None:
        """@brief Store the generated index page; other arguments go to the base class."""
        self._index_html = index_html
        super().__init__(*args, **kwargs)  # type: ignore[arg-type]

    def do_GET(self) -> None:
        """@brief Answer the root path with the index page, other paths from disk."""
        if self.path in ("/", "/index.html"):
            body = self._index_html.encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        """@brief Send the access log to the logging module instead of stderr."""
        _LOG.info("%s - %s", self.address_string(), format % args)


def create_server(
    index_html: str,
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    site_dir: Path = SITE_DIR,
) -> ThreadingHTTPServer:
    """@brief Build, but do not start, the server.

    @param index_html The page served at the root path.
    @param host Address to bind to.
    @param port Port to bind to; 0 lets the system choose a free one.
    @param site_dir Folder with the static pages.
    @return The server; call serve_forever() on it.
    """
    handler = partial(SiteRequestHandler, index_html=index_html, directory=str(site_dir))
    return ThreadingHTTPServer((host, port), handler)


def serve(index_html: str, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> None:
    """@brief Serve the site until the user presses Ctrl+C."""
    with create_server(index_html, host, port) as server:
        bound_host, bound_port = server.server_address[:2]
        _LOG.info("Serving on http://%s:%s/ (Ctrl+C to stop)", bound_host, bound_port)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            _LOG.info("Stopped")
