from playwright.sync_api import expect
import pytest


@pytest.mark.smoke
def test_add_two_items_updates_badge(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.header.cart_badge).to_have_text('3')


def test_remove_item_from_cart(inventory_page, cart_page):
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.header.open_cart()
    expect(cart_page.item_names).to_have_text(
        ["Sauce Labs Onesie", "Sauce Labs Backpack"])
    cart_page.remove("Sauce Labs Onesie")
    expect(inventory_page.header.cart_badge).to_have_text('1')
