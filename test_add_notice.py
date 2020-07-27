from .pages.add_notice_page import AddNoticePage
from .pages.locators import AddNoticePageLocators
from .pages.user_items_page import UserItemsPage
from .pages.item_page import ItemPage
import pytest
import json
import time


class TestAddNotice:
    @pytest.fixture(scope='class', autouse=True)
    def login(self, browser):
        page = AddNoticePage(browser)
        page.send_email()
        page.go_to_next()
        page.send_password()
        page.go_to_next()

    @pytest.fixture(scope='class')
    def properties(self):
        with open('properties.json', 'r') as f:
            properties = json.load(f)
        yield properties

    @pytest.fixture(scope='function', autouse=True)
    def delete_added_item(self, browser):
        yield
        page = UserItemsPage(browser)
        page.click_on_moderation_button()
        page.click_select_all_button()
        page.click_delete_from_moderation_button()

    sell_type_buttons = [AddNoticePageLocators.SELL_BUTTON,
                         AddNoticePageLocators.RENT_BUTTON,
                         AddNoticePageLocators.DAILY_RENT_BUTTON]

    @pytest.mark.parametrize('sell_type_button', sell_type_buttons)
    def test_default_add(self, browser, properties, sell_type_button):
        add_notice_page = AddNoticePage(browser)
        add_notice_page.click_sell_type_button(*sell_type_button)
        add_notice_page.click_property_flat()
        add_notice_page.click_object_flat()
        add_notice_page.move_to_address_block()
        add_notice_page.send_street(properties['street'])
        address = add_notice_page.get_address()
        add_notice_page.send_required_properties(properties)
        add_notice_page.move_to_bottom()
        add_notice_page.click_free_add_button()
        add_notice_page.click_confirm_button()
        add_notice_page.should_be_success_message()
        user_items_page = UserItemsPage(browser)
        user_items_page.click_on_moderation_button()
        user_items_page.should_be_same_address(address)
        user_items_page.should_be_same_price(properties['price'])
        user_items_page.go_to_item_page()
        item_page = ItemPage(browser, browser.current_url)
        item_page.should_be_same_properties(properties, address)

