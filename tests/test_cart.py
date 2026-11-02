from playwright.sync_api import expect


def test_add_two_items_updates_badge(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.header.cart_badge).to_have_text('2')
