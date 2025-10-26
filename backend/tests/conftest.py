# backend/tests/conftest.py
import os, sys, pathlib

BACKEND_ROOT = pathlib.Path(__file__).resolve().parents[1]  # .../backend
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))
