import pytest
from data.users import standard_user
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


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


@pytest.fixture
def cart_page(inventory_page):
    return CartPage(inventory_page.page)


@pytest.fixture
def checkout_info_page(cart_page):
    return CheckoutInfoPage(cart_page.page)


@pytest.fixture
def checkout_overview_page(cart_page):
    return CheckoutOverviewPage(cart_page.page)


@pytest.fixture
def checkout_complete_page(cart_page):
    return CheckoutCompletePage(cart_page.page)
