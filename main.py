"""Serve the website locally from this folder."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
from pathlib import Path


HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8000"))
WEB_ROOT = Path(__file__).resolve().parent


class WebsiteHandler(SimpleHTTPRequestHandler):
    """Serve index.html for the site root and static files from this folder."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_ROOT), **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        super().do_GET()


def main():
    server = ThreadingHTTPServer((HOST, PORT), WebsiteHandler)
    print(f"Serving {WEB_ROOT}")
    print(f"Open http://{HOST}:{PORT}/ in your browser")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
