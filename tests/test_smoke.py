import pytest
from playwright.sync_api import expect, Page
import re


@pytest.mark.smoke
def test_login_page_loads(page: Page):
    username = page.get_by_test_id('username')
    page.goto("/")
    expect(page).to_have_title('Swag Labs')
    expect(username).to_be_visible()


def test_standard_user_lands_on_inventory(login_page):
    login_page.login('standard_user', 'secret_sauce')
    expect(login_page.page).to_have_url(re.compile(r".*/inventory\.html"))
