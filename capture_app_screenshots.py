"""
Captura screenshots do app Zavvy logado usando pyautogui (tela real)
Recebe instrução via HTTP para navegar + capturar
"""
import time
import os
import json
import pyautogui
from PIL import Image
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

SAVE_DIR = "screenshots/app"
pyautogui.FAILSAFE = False

# Controle compartilhado
state = {"pending": None, "done": False}


def capture_screen(filename, scroll_full=False):
    """Captura a tela atual e salva"""
    time.sleep(0.8)  # aguarda render
    full_path = os.path.join(SAVE_DIR, filename)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    if not scroll_full:
        img = pyautogui.screenshot()
        img.save(full_path)
        print(f"  Saved: {full_path}")
        return

    # Captura scroll completo: múltiplas telas + stitch
    frames = []
    screen_w, screen_h = pyautogui.size()

    # Scroll até o topo
    pyautogui.hotkey('ctrl', 'Home')
    time.sleep(0.5)

    prev_scroll = -1
    while True:
        img = pyautogui.screenshot()
        frames.append(img)

        # Rola para baixo
        pyautogui.scroll(-10)
        time.sleep(0.4)

        # Verifica se chegou ao fim
        import subprocess
        result = subprocess.run(
            ['python', '-c', 'import pyautogui; print(pyautogui.position())'],
            capture_output=True, text=True
        )
        # Compara pixels do rodapé para detectar fim da página
        new_img = pyautogui.screenshot()
        if frames and list(new_img.crop((0, screen_h-50, screen_w, screen_h)).getdata()) == \
                list(frames[-1].crop((0, screen_h-50, screen_w, screen_h)).getdata()):
            break
        if len(frames) > 15:  # segurança
            break

    # Stitch simples: só usa os frames
    if len(frames) == 1:
        frames[0].save(full_path)
    else:
        # Empilha verticalmente (simples, com sobreposição)
        total_h = screen_h + (len(frames) - 1) * (screen_h - 100)
        stitched = Image.new('RGB', (screen_w, total_h))
        for i, f in enumerate(frames):
            stitched.paste(f, (0, i * (screen_h - 100)))
        stitched.save(full_path)

    print(f"  Saved: {full_path} ({len(frames)} frames)")


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        filename = body["filename"]
        capture_screen(filename)
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
        pass


if __name__ == "__main__":
    port = 7789
    print(f"App screenshot server em http://localhost:{port}")
    HTTPServer(("localhost", port), Handler).serve_forever()
