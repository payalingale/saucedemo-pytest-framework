headed_mode='python -m pytest -v --headed --slowmo 500'
no_headed_mode = python -m pytest -v
regression_suite = python -m pytest -m regression -v
single test = python -m pytest tests/test_cart.py::test_add_two_items_updates_badge -v --headed --slowmo 500
