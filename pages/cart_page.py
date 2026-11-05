from playwright.sync_api import Page
from pages.components.header import Header


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = Header(page)
        self.cart_items = page.get_by_test_id('inventory-item')
        self.item_names = page.get_by_test_id('inventory-item-name')
        self.checkout_button = page.get_by_test_id("checkout")

    def remove(self, productName):
        card = self.cart_items.filter(has_text=productName)
        card.get_by_role("button", name="Remove").click()

    def checkout(self):
        self.checkout_button.click()
