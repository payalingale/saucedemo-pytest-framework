import pytest
from data.users import standard_user
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture(scope="session")
def standard_user_state(browser, base_url, tmp_path_factory):
    path = tmp_path_factory.mktemp("auth") / "standard_user.json"
    context = browser.new_context(base_url=base_url)
    page = context.new_page()

    login = LoginPage(page)
    login.open()
    user = standard_user()
    login.login(user.username, user.password)
    # be sure login finished before saving
    page.wait_for_url("**/inventory.html")

    context.storage_state(path=path)            # save cookies + localStorage
    context.close()
    return path


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, standard_user_state):
    return {**browser_context_args, "storage_state": standard_user_state}


@pytest.fixture
def inventory_page(page):
    # already logged in, no login steps
    page.goto("/inventory.html")
    return InventoryPage(page)
