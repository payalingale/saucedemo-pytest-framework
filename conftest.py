import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page


@pytest.fixture(scope='session', autouse=True)
def configure_test_id(playwright):
    playwright.selectors.set_test_id_attribute('data-test')


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture
def inventory_page(login_page):
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(login_page.page)
