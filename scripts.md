headed_mode='python -m pytest -v --headed --slowmo 500'
no_headed_mode = python -m pytest -v
regression_suite = python -m pytest -m regression -v
single test = python -m pytest tests/test_checkout.py::test_overview_total_matches_item_prices -v --headed --slowmo 500 -
