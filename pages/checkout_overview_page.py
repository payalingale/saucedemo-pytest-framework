
from playwright.sync_api import Page


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.inventory_item_price = page.get_by_test_id('inventory-item-price')
        self.subtotal_label = page.get_by_test_id('subtotal-label')
        self.tax_label = page.get_by_test_id('tax-label')
        self.total_label = page.get_by_test_id('total-label')
        self.finish_button = page.get_by_test_id('finish')

    def finish(self):
        self.finish_button.click()
