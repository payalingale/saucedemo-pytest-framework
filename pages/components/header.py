from playwright.sync_api import Page


class Header:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.get_by_test_id('shopping-cart-link')
        self.cart_badge = page.get_by_test_id('shopping-cart-badge')

    def open_cart(page):
        page.cart_link.click()
