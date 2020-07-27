from .base_page import BasePage
from .locators import AddNoticePageLocators
from selenium.webdriver.common.keys import Keys
import os


class AddNoticePage(BasePage):
    def __init__(self, browser, url='https://move.ru/add_notice/', timeout=10):
        super().__init__(browser, url, timeout)

    def click_confirm_button(self):
        self.browser.find_element(*AddNoticePageLocators.CONFIRM_BUTTON).click()

    def click_free_add_button(self):
        self.browser.find_element(*AddNoticePageLocators.FREE_ADD_BUTTON).click()

    def click_sell_type_button(self, selector_type, locator):
        self.browser.find_element(selector_type, locator).click()

    def click_property_flat(self):
        self.browser.find_element(*AddNoticePageLocators.PROPERTY_FLAT_BUTTON).click()

    def click_object_flat(self):
        self.browser.find_element(*AddNoticePageLocators.OBJECT_FLAT_BUTTON).click()

    def get_address(self):
        return self.get_element_text(*AddNoticePageLocators.ADDRESS)

    def go_to_next(self):
        self.browser.find_element(*AddNoticePageLocators.NEXT_BUTTON).click()

    def move_to_address_block(self):
        self.move_to_element(*AddNoticePageLocators.ADDRESS_BLOCK)

    def move_to_bottom(self):
        self.move_to_element(*AddNoticePageLocators.CONFIRM_BUTTON)

    def move_to_home_properties_block(self):
        self.move_to_element(*AddNoticePageLocators.HOME_PROPERTIES_BLOCK)

    def move_to_price_block(self):
        self.move_to_element(*AddNoticePageLocators.PRICE_BLOCK)

    def move_to_properties_block(self):
        self.move_to_element(*AddNoticePageLocators.PROPERTIES_BLOCK)

    def send_email(self, email='ontondend@yandex.ru'):
        self.browser.find_element(*AddNoticePageLocators.EMAIL_INPUT).send_keys(email)

    def send_description(self, description):
        self.browser.find_element(*AddNoticePageLocators.DESCRIPTION_INPUT).send_keys(description)

    def send_floor(self, floor):
        self.browser.find_element(*AddNoticePageLocators.FLOOR_INPUT).send_keys(floor)

    def send_floors(self, floors):
        self.browser.find_element(*AddNoticePageLocators.FLOORS_INPUT).send_keys(floors)

    def send_full_area(self, area):
        self.browser.find_element(*AddNoticePageLocators.FULL_AREA_INPUT).send_keys(area)

    def send_kitchen_area(self, area):
        self.browser.find_element(*AddNoticePageLocators.KITCHEN_AREA).send_keys(area)

    def send_living_area(self, area):
        self.browser.find_element(*AddNoticePageLocators.LIVING_AREA_INPUT).send_keys(area)

    def send_password(self, password='4b7a7ac'):
        self.browser.find_element(*AddNoticePageLocators.PASSWORD_INPUT).send_keys(password)

    def send_price(self, price):
        self.browser.find_element(*AddNoticePageLocators.PRICE_INPUT).send_keys(price)

    def send_photo(self, path):
        abs_path = os.path.abspath(path)
        self.browser.find_element(*AddNoticePageLocators.PHOTO_INPUT).send_keys(abs_path)

    def send_required_properties(self, properties):
        self.move_to_properties_block()
        self.send_rooms(properties['rooms'])
        self.send_floor(properties['floor'])
        self.send_full_area(properties['full_area'])
        self.send_living_area(properties['living_area'])
        self.send_kitchen_area(properties['kitchen_area'])
        self.move_to_home_properties_block()
        self.send_floors(properties['floors'])
        self.move_to_price_block()
        self.send_photo(properties['photo'])
        self.send_description(properties['description'])
        self.send_price(properties['price'])

    def send_rooms(self, rooms):
        self.browser.find_element(*AddNoticePageLocators.ROOMS_INPUT).send_keys(rooms)

    def send_street(self, street):
        self.browser.find_element(*AddNoticePageLocators.STREET_INPUT).send_keys(street)
        self.browser.find_element(*AddNoticePageLocators.STREET_INPUT).send_keys(Keys.ENTER)

    def should_be_success_page(self):
        assert self.is_element_present(*AddNoticePageLocators.SUCCESS_PAGE),\
            "Нет окна об успешности добавления объявления"

    def should_be_success_message(self):
        self.should_be_success_page()
        expected_message = 'Объявление успешно добавлено!'
        assert expected_message == self.get_element_text(*AddNoticePageLocators.SUCCESS_MESSAGE),\
            "Нет сообщения об успешности добавления"
