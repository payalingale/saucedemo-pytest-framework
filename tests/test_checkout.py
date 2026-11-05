
from playwright.sync_api import expect


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
    prices = checkout_overview_page.subtotal_label.all_text_contents()
    print(prices.strip())


def test_checkout_requires_first_name(inventory_page, cart_page, checkout_info_page):
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.add_to_cart("Sauce Labs Backpack")
    cart_page.header.open_cart()
    cart_page.checkout()
    checkout_info_page.enter_details('', "Doe", "00000")
    checkout_info_page.click_continue()
    expect(checkout_info_page.error).to_have_text(
        'Error: First Name is required')
