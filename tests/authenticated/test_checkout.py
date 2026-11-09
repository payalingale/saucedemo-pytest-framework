
from playwright.sync_api import expect
from decimal import Decimal
import pytest
from data.users import problem_user
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckOutInfoPage


@pytest.mark.smoke
def test_complete_purchase_of_two_items(inventory_page, cart_page, checkout_info_page, checkout_overview_page, checkout_complete_page):
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.add_to_cart("Sauce Labs Backpack")
    cart_page.header.open_cart()
    cart_page.checkout()
    checkout_info_page.enter_details('John', 'Doe', '00000')
    checkout_info_page.click_continue()
    expect(checkout_overview_page.inventory_item_price).to_have_count(2)
    checkout_overview_page.finish()
    expect(checkout_complete_page.complete_header).to_have_text(
        'Thank you for your order!')


def test_overview_total_matches_item_prices(inventory_page, cart_page, checkout_info_page, checkout_overview_page):
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.add_to_cart("Sauce Labs Backpack")
    cart_page.header.open_cart()
    cart_page.checkout()
    checkout_info_page.enter_details('John', 'Doe', '00000')
    checkout_info_page.click_continue()
    expect(checkout_overview_page.inventory_item_price).to_have_count(2)
    prices = checkout_overview_page.inventory_item_price.all_text_contents()
    subtotal = sum(Decimal(p.replace("$", ""))
                   # YOUR calculation
                   for p in prices)
    tax_text = checkout_overview_page.tax_label.text_content()
    tax = Decimal(tax_text.split("$")[1])
    expect(checkout_overview_page.subtotal_label).to_have_text(
        f"Item total: ${subtotal}")
    expect(checkout_overview_page.total_label).to_have_text(
        f"Total: ${subtotal + tax}")


def test_checkout_requires_first_name(inventory_page, cart_page, checkout_info_page):
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.add_to_cart("Sauce Labs Backpack")
    cart_page.header.open_cart()
    cart_page.checkout()
    checkout_info_page.enter_details('', "Doe", "00000")
    checkout_info_page.click_continue()
    expect(checkout_info_page.error).to_have_text(
        'Error: First Name is required')
