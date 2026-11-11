from playwright.sync_api import Page


class CheckoutInfoPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_test_id('firstName')
        self.last_name = page.get_by_test_id('lastName')
        self.postal_code = page.get_by_test_id('postalCode')
        self.continue_button = page.get_by_test_id('continue')
        self.error = page.get_by_test_id('error')

    def enter_details(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()
