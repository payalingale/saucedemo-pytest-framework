<<<<<<< HEAD
saucedemo-pytest-framework/
├── .github/workflows/tests.yml
├── pages/
│ ├── components/header.py
│ ├── login*page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ └── checkout*\*.py
├── api/client.py
├── data/users.py
├── tests/
│ ├── conftest.py
│ ├── test_login.py
│ ├── authenticated/
│ │ ├── conftest.py
│ │ ├── test_cart.py
│ │ └── test_checkout.py
│ └── api/test_posts.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
└── README.md

Day 1 (Sun, Nov 1): Foundation. This is a fresh repo, built properly from the start.

New repo saucedemo-pytest-framework, with a venv, requirements.txt and .gitignore
pytest.ini: testpaths, --base-url, registered markers, --strict-markers
Move LoginPage and InventoryPage in, and switch to get_by_test_id (configure data-test as the test ID attribute)
Login tests: happy path plus one parametrized test covering 3 error cases
✅ Done when: pytest passes from the repo root, goto("/") has no hardcoded URL, and the code is pushed to GitHub

Day 2 (Mon): The complete purchase flow

CartPage, CheckoutInfoPage, CheckoutOverviewPage, CheckoutCompletePage
A Header component (cart icon, menu, logout), reused across pages
An end-to-end test: log in → add 2 items → cart → checkout → “Thank you for your order!”
A test that checks the overview total equals the item prices plus tax, calculated in Python
✅ Done when: no raw selectors appear in any test file, there are no assertions in page objects, and the E2E test passes

Day 3 (Tue): Fixtures, data, environments

Fixtures for each page object in conftest.py
Test users in data/users.py, and the password from an environment variable (.env plus python-dotenv, with .env in .gitignore)
A custom --env command-line option
smoke and regression markers applied, plus a problem_user test that catches a real site bug
✅ Done when: pytest -m smoke runs a subset, no secrets are in git, and you can explain fixture scope with your id() proof

Day 4 (Wed): Speed and isolation

Record a baseline with pytest --durations=10
Log in once with storage_state at session scope, and use it only for tests in tests/authenticated/ (folder-level conftest)
Parallel runs with pytest -n auto, plus a random-order run with pytest-randomly
✅ Done when: the suite passes in parallel and in random order, and you can state the before/after timing in numbers

Day 5 (Thu): Debugging and reporting

Traces, screenshots and video kept on failure (retain-on-failure)
An HTML report (pytest-html or Allure)
A pytest_runtest_makereport hook that attaches a screenshot to failed tests
Python logging in page-object actions
✅ Done when: you break a test on purpose, open its trace, and explain what it shows

Day 6 (Fri): API layer and CI

An API fixture with Playwright request (against jsonplaceholder), with tests for GET, POST and a negative case
A GitHub Actions workflow: smoke tests on every push, full suite on demand, artifacts uploaded on failure, password from GitHub Secrets
✅ Done when: a push triggers a green CI run, and a deliberately broken test produces a downloadable trace

Day 7 (Sat): Defend it

A README covering structure, how to run, and design decisions with reasons
A self-review: one change you’d make with more time
A mock interview: 2-minute framework walkthrough plus 15 questions on your own code
The final test: rebuild the login chunk from an empty folder in 30 minutes, with no notes
✅ Done when: you score PASS on at least 10 of 15, and the rebuild works
=======
# saucedemo-pytest-framework
>>>>>>> 5002a7f9f0604fd8fff6562545825085dbb77e58
