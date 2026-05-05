# No .venv Python Server

This containerised application runs a `uvicorn` server within a Docker container **without a virtual environment**.

It is a proof-of-concept to showcase that a Python server **does not need two isolated environments**, one being nested within the other.

## Setup & Installation

### Local Dev

```sh
uv sync
source .venv/bin/activate
uv run main.py
```

### Docker Container

```
docker build . -t python-server-test
docker images
docker run -p 8000:8000 python-server-test
```
