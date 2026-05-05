# No .venv Python Server

This containerised application runs a `uvicorn` server within a Docker container **without a virtual environment**.

It is a proof-of-concept to showcase that a Python server **does not need two isolated environments**, one being nested within the other.

## Setup & Installation

### Local

```sh
uv sync
source .venv/bin/activate
```
