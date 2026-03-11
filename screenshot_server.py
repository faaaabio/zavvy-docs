"""
Servidor local para receber screenshots do browser e salvar em disco.
POST /save  { "path": "app/dashboard/01-home.png", "data": "<base64>" }
"""
import base64
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

SAVE_DIR = "screenshots"


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        rel_path = body["path"]
        b64 = body["data"].split(",")[-1]  # remove data:image/png;base64, prefix
        full_path = os.path.join(SAVE_DIR, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "wb") as f:
            f.write(base64.b64decode(b64))
        print(f"  Saved: {full_path}")
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b"ok")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, *args):
        pass  # silence default logs


if __name__ == "__main__":
    port = 7788
    print(f"Screenshot server rodando em http://localhost:{port}")
    HTTPServer(("localhost", port), Handler).serve_forever()
