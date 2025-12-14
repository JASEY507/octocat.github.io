#!/bin/bash

export TOOL_PASS="98921h2ı0hrı2wfonsnv"

pip install -r requirements.txt >/dev/null 2>&1

python3 tool.py &

uvicorn server:app --host 0.0.0.0 --port 8080
