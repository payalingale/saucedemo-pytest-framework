from playwright.sync_api import expect
from decimal import Decimal
import pytest
from data.users import problem_user
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckOutInfoPage


@pytest.mark.xfail(strict=True, reason="SauceDemo bug: problem_user cannot type a last name")
def test_problem_user_can_enter_last_name(login_page):
    user = problem_user()
    login_page.login(user.username, user.password)
    inventory = InventoryPage(login_page.page)
    inventory.add_to_cart("Sauce Labs Onesie")
    cart = CartPage(login_page.page)
    cart.header.open_cart()
    cart.checkout()
    info = CheckOutInfoPage(login_page.page)
    info.enter_details('John', 'Doe', '00000')
    expect(info.last_name).to_have_value('Doe')
