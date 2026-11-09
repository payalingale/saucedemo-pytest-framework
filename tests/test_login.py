import pytest
from playwright.sync_api import expect, Page
import re
from data.users import standard_user, locked_user, problem_user


@pytest.mark.smoke
def test_login_page_loads(page: Page):
    username = page.get_by_test_id('username')
    page.goto("/")
    expect(page).to_have_title('Swag Labs')
    expect(username).to_be_visible()


@pytest.mark.smoke
def test_standard_user_lands_on_inventory(login_page):
    user = standard_user()
    login_page.login(user.username, user.password)
    expect(login_page.page).to_have_url(re.compile(r".*/inventory\.html"))


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, use_valid_password, message",
    [
        ("locked_out_user", True,  "Epic sadface: Sorry, this user has been locked out."),
        ("standard_user",   False, "Epic sadface: Password is required"),
        ("",                True,  "Epic sadface: Username is required"),
    ],
    ids=["locked-out", "empty-password", "empty-username"],
)
def test_login_shows_error(login_page, username, use_valid_password, message):
    password = standard_user().password if use_valid_password else ""
    login_page.login(username, password)
    expect(login_page.error).to_have_text(message)
