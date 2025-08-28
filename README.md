# Pytest Practice

## Steps
1) Create & activate a venv:
   - Linux/macOS: `python -m venv .venv && source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
2) `pip install -r requirements.txt`
3) Run tests:
   - `pytest -q`
   - or `pytest -n auto --alluredir=allure-results`

## Exercises (~30 min)
- **E1:** Add a rule: email must contain `@` and a valid domain; write a parametrized test.
- **E2:** Property test: `age` ∈ [0, 120] or NA after `clean_users`.
- **E3:** Add a test asserting `user_id` is an int (not a string).

## CI
The workflow in `.github/workflows/tests.yml` runs tests and uploads an Allure artifact.
