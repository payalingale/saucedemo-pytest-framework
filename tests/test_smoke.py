import pytest
from playwright.sync_api import expect, Page


@pytest.mark.smoke
def test_login_page_loads(page: Page):
    username = page.get_by_test_id('username')
    page.goto("/")
    expect(page).to_have_title('Swag Labs')
    expect(username).to_be_visible()
