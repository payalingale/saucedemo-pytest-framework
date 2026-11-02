import pytest
from pages.loginPage import LoginPage
from playwright.sync_api import Page


@pytest.fixture(scope='session', autouse=True)
def configure_test_id(playwright):
    playwright.selectors.set_test_id_attribute('data-test')


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.open()
    return lp
