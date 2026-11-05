# CheckoutCompletePage

# locators: complete-header, back-to-products

from playwright.sync_api import Page


class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.complete_header = page.get_by_test_id('complete-header')
        self.back_to_products = page.get_by_test_id('back-to-products')
