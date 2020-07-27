from .base_page import BasePage
from .locators import ItemPageLocators
import time


class ItemPage(BasePage):
    def move_to_properties_bottom(self):
        self.move_to_element(*ItemPageLocators.PROPERTIES_BLOCK_BOTTOM)

    def should_be_same_properties(self, properties, address):
        self.move_to_properties_bottom()
        self.should_be_same_price(properties['price'])
        self.should_be_same_rooms(properties['rooms'])
        self.should_be_same_floor(properties['floor'], properties['floors'])
        self.should_be_same_full_area(properties['full_area'])
        self.should_be_same_living_area(properties['living_area'])
        self.should_be_same_kitchen_area(properties['kitchen_area'])
        self.should_be_same_address(address)
        self.should_be_same_floors(properties['floors'])
        self.should_be_same_description(properties['description'])

    def should_be_same_address(self, address):
        displayed_address = self.get_element_text(*ItemPageLocators.PROPERTIES_ADDRESS)
        assert address == displayed_address, \
            "Неправильный адрес в описании объявления"

    def should_be_same_description(self, description):
        displayed_description = self.get_element_text(*ItemPageLocators.PROPERTIES_DESCRIPTION)
        assert description == displayed_description, \
            f"Неправильное текст описания объявления: {displayed_description}"

    def should_be_same_floor(self, floor, floors):
        displayed_floor = self.get_element_text(*ItemPageLocators.PROPERTIES_FLOOR)
        assert f"{floor}/{floors}" == displayed_floor, \
            "Неправильное кол-во этажей в описании объявления"

    def should_be_same_floors(self, floors):
        displayed_floors = self.get_element_text(*ItemPageLocators.PROPERTIES_FLOORS)
        assert str(floors) == displayed_floors, \
            "Неправильная этажность здания в описании объявления"

    def should_be_same_full_area(self, area):
        displayed_area = self.get_element_text(*ItemPageLocators.PROPERTIES_FULL_AREA)
        length = len(str(area))
        displayed_price = displayed_area.replace(' ', '')
        displayed_price = displayed_price[:length]
        assert str(area) == displayed_price, "Неправильная полная площадь в описании объявления"

    def should_be_same_living_area(self, area):
        displayed_area = self.get_element_text(*ItemPageLocators.PROPERTIES_LIVING_AREA)
        length = len(str(area))
        displayed_price = displayed_area.replace(' ', '')
        displayed_price = displayed_price[:length]
        assert str(area) == displayed_price, "Неправильная жилая площадь в описании объявления"

    def should_be_same_kitchen_area(self, area):
        displayed_area = self.get_element_text(*ItemPageLocators.PROPERTIES_KITCHEN_AREA)
        length = len(str(area))
        displayed_price = displayed_area.replace(' ', '')
        displayed_price = displayed_price[:length]
        assert str(area) == displayed_price, "Неправильная площадь кухни в описании объявления"

    def should_be_same_price(self, price):
        displayed_price = self.get_element_text(*ItemPageLocators.PROPERTIES_PRICE)
        length = len(str(price))
        displayed_price = displayed_price.replace(' ', '')
        displayed_price = displayed_price[:length]
        assert str(price) == displayed_price, "Неправильная цена в описании объявления"

    def should_be_same_rooms(self, rooms):
        displayed_rooms = self.get_element_text(*ItemPageLocators.PROPERTIES_ROOMS)
        assert str(rooms) == displayed_rooms, \
            "Неправильное кол-во комнат в описании объявления"


