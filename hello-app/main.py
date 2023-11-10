from fastapi import FastAPI
import os
from pathlib import Path
import time

started_at = time.time()

app = FastAPI()

@app.get("/env-var")
def read_env():
    return os.getenv("HELLOENV")

@app.get("/env-file")
def read_text_file():
    data = Path("data/text.txt")
    assert data.exists(), "File not found."
    return data.read_text()

@app.get("/secret")
def read_secret():
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    return {
        "user": user,
        "password": password
    }

@app.get("/healthz")
def healthz():
    duration = time.time() - started_at
    assert duration > 10, f"{duration=}"
    return "ok"