import subprocess
import threading
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

STATIC_DIR = os.path.join(os.path.dirname(__file__), ".web", "build", "client")

@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(STATIC_DIR, path)

def run_backend():
    subprocess.run(["reflex", "run", "--env", "prod", "--backend-only"])

if __name__ == "__main__":
    thread = threading.Thread(target=run_backend)
    thread.daemon = True
    thread.start()
    app.run(host="0.0.0.0", port=8000)