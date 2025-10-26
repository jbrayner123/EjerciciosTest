# Testing Starter — FastAPI (backend) + React (frontend)

This repository is a **ready-to-run** template to practice **unit testing** locally and in **GitHub Actions**.

- Backend: **FastAPI** + **pytest** (with `TestClient`).
- Frontend: **React + Vite** + **Vitest** + **React Testing Library**.
- CI: **GitHub Actions** workflow that runs both test suites on every push/PR.

---

## ✅ Prerequisites
- **Python 3.10+** (recommended 3.11)
- **Node.js 18+** (recommended 20)
- Optional: **uv** (fast Python package manager) — You can install it locally from https://astral.sh/uv

---

## ▶️ How to run locally

### 1) Backend (FastAPI + pytest)
```bash
cd backend

# Option A: with uv (recommended locally)
uv venv
uv pip install -r requirements.txt
uv run pytest -q

# Option B: with pip
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

### 2) Frontend (React + Vitest)
```bash
cd frontend
npm install
npm test -- --run
```
> The tests run in a **jsdom** environment and use **React Testing Library**.

---

## 🤖 GitHub Actions (CI)
The workflow file is in `.github/workflows/ci.yml`. On every **push** / **pull request**, it will:
- Install Python deps and run **backend tests** (`pytest`).
- Install Node deps and run **frontend tests** (`vitest`).

No configuration needed — just **push this repo to GitHub**.
