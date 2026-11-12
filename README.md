# SauceDemo Test Automation Framework

UI test automation for the [SauceDemo](https://www.saucedemo.com) demo shop, covering login, cart and the full checkout flow. Built with pytest and Playwright, using the Page Object Model, parallel runs and GitHub Actions CI.

## Tech stack

- Python 3.12
- pytest + pytest-playwright
- pytest-xdist (parallel runs)
- pytest-html (HTML report)
- GitHub Actions (CI)

## Project structure

```
saucedemo-pytest-framework/
├── .github/workflows/tests.yml     # CI: smoke on push, full suite on demand
├── pages/                          # Page objects: locators + actions, no assertions
│   ├── components/header.py        # Shared header (cart icon, menu, logout)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_info_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
├── data/users.py                   # Test users; password read from env
├── tests/
│   ├── test_login.py               # Run logged out
│   ├── test_problem_user.py
│   └── authenticated/              # Start already logged in
│       ├── conftest.py             # Session-scoped storage_state login
│       ├── test_cart.py
│       └── test_checkout.py
├── conftest.py                     # --env option, page fixtures, report metadata
├── pytest.ini                      # Markers, tracing/screenshot/video on failure
├── requirements.txt
├── .env.example                    # Copy to .env and set SAUCE_PASSWORD
└── .python-version
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
cp .env.example .env    # then set SAUCE_PASSWORD in .env
```

## Running tests

```bash
# Full suite
python -m pytest -v

# Smoke tests only (critical path)
python -m pytest -m smoke -v

# Regression tests only
python -m pytest -m regression -v

# In parallel with 4 workers
python -m pytest -n 4

# Headed and slowed down, to watch the browser
python -m pytest -v --headed --slowmo 500

# A single test
python -m pytest tests/authenticated/test_checkout.py::test_overview_total_matches_item_prices -v

# With an HTML report
python -m pytest --html=reports/report.html --self-contained-html
```

On failure, traces, screenshots and videos are saved to `test-results/`. Open a trace with:

```bash
python -m playwright show-trace test-results/<test-folder>/trace.zip
```

## Design decisions

- **Locators use `get_by_test_id`:** `data-test` attributes are added for testing, so they don't change when styling or text changes. Locators that use them don't break on UI changes.
- **Login once with `storage_state`:** each session logs in through the UI once and saves the cookies. Every test still gets a fresh context loaded with them, so tests stay isolated without a login each time. It's only in `tests/authenticated/` because the login tests need to start logged out.
- **`Decimal` for money:** `37.98 + 3.04` gives `41.019999999999996` as floats, so a float-based total check would fail even when the site is correct.
- **No assertions in page objects:** pages only find elements and perform actions; tests decide what is correct. This keeps page objects reusable across tests.
- **Parallel runs with pytest-xdist:** the suite went from 14.5 s to 9.5 s with `-n 4`.

## CI

GitHub Actions (`.github/workflows/tests.yml`):

- **On every push and pull request:** runs the smoke tests for fast feedback.
- **On demand** (Run workflow button): runs the full suite in parallel.
- The HTML report is always uploaded as an artifact; traces and screenshots are uploaded only when a test fails.
- The password comes from the `SAUCE_PASSWORD` GitHub Secret, never from the code.

## Roadmap

- API tests with Playwright `request`
- Logging in page-object actions
