from .base_page import BasePage
from .locators import UserItemsPageLocators


class UserItemsPage(BasePage):
    def __init__(self, browser, url='https://move.ru/user/items/', timeout=10):
        super().__init__(browser, url, timeout)

    def click_select_all_button(self):
        self.browser.find_element(*UserItemsPageLocators.SELECT_ALL_BUTTON).click()

    def click_delete_from_moderation_button(self):
        self.browser.find_element(*UserItemsPageLocators.DELETE_FROM_MODERATION_BUTTON).click()

    def click_on_moderation_button(self):
        self.browser.find_element(*UserItemsPageLocators.ON_MODERATION_BUTTON).click()

    def go_to_item_page(self):
        self.browser.find_element(*UserItemsPageLocators.ADDRESS_LINK).click()
        length = len(self.browser.window_handles)
        item_page = new_window = self.browser.window_handles[length-1]
        self.browser.switch_to.window(item_page)

    def should_be_same_address(self, address):
        assert address == self.get_element_text(*UserItemsPageLocators.ADDRESS_LINK),\
            "В объявлении отображается другой адрес"

    def should_be_same_price(self, price):
        displayed_price = self.get_element_text(*UserItemsPageLocators.PRICE)
        displayed_price = displayed_price.replace(' ', '')
        assert str(price) == displayed_price, \
            f"В объявлении отображается другая цена"
