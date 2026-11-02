from playwright.sync_api import Page
from pages.components.header import Header


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = Header(page)
        self.product_cards = page.get_by_test_id('inventory-item')

    def add_to_cart(self, product_name):
        card = self.product_cards.filter(has_text=product_name)
        card.get_by_role("button", name="Add to cart").click()
