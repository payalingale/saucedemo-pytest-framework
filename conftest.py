from data.users import standard_user
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckOutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from playwright.sync_api import Page
from dotenv import load_dotenv
load_dotenv()

ENVIRONMENTS = {
    "prod": "https://www.saucedemo.com",
    "staging": "https://staging.saucedemo.example",
}


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        default='prod',
        choices=list(ENVIRONMENTS),
        help='Environment to run against'
    )


@pytest.fixture(scope='session')
def base_url(request):
    return ENVIRONMENTS[request.config.getoption("--env")]


@pytest.fixture(scope='session', autouse=True)
def configure_test_id(playwright):
    playwright.selectors.set_test_id_attribute('data-test')


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture
def cart_page(inventory_page):
    return CartPage(inventory_page.page)


@pytest.fixture
def checkout_info_page(cart_page):
    return CheckOutInfoPage(cart_page.page)


@pytest.fixture
def checkout_overview_page(cart_page):
    return CheckoutOverviewPage(cart_page.page)


@pytest.fixture
def checkout_complete_page(cart_page):
    return CheckoutCompletePage(cart_page.page)
