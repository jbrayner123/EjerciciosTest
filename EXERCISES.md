# Exercises — Unit Testing (FastAPI + React)

Follow these four tasks. Some tests are **skipped** — remove the skip markers once your implementation is ready.

## 1) Backend — `GET /items` with optional filter `?q=`
- Implement `GET /items` returning all items.
- If `?q=` is passed, filter items by name (case-insensitive).

## 2) Backend — Mock a dependency for `GET /price/{usd}`
- Create a dependency `get_exchange_rate()` (USD→COP).
- Implement `GET /price/{usd}` returning `{ usd, rate, cop }`.
- In tests, override the dependency to return a fixed rate.

## 3) Frontend — `<LoginForm />` component + test
- Controlled inputs (email, password), submit calls `onSubmit({ email, password })`.

## 4) Frontend — `useCounter` hook + test
- Returns `{ count, inc, dec, reset }` with optional step parameter.
