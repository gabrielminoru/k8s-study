from python:3.10-slim-buster
copy main.py main.py
copy requirements.txt requirements.txt
run pip install -r requirements.txt
cmd ["uvicorn", "main:app","--host=0.0.0.0", "--port=8080"]