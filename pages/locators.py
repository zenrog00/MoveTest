from selenium.webdriver.common.by import By


class AddNoticePageLocators:
    ADDRESS = [By.CSS_SELECTOR, 'div.adding-object__address-address']
    ADDRESS_BLOCK = (By.CSS_SELECTOR, 'section[id="address"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'a.adding-object__btn-finish')
    DAILY_RENT_BUTTON = (By.CSS_SELECTOR, 'li.radio-tab__item:nth-child(3)')
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'textarea[name="fullDescription"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    FLOOR_INPUT = (By.CSS_SELECTOR, 'input[name="floor"]')
    FLOORS_INPUT = (By.CSS_SELECTOR, 'input[name="floors"]')
    FREE_ADD_BUTTON = (By.CSS_SELECTOR, 'div.adding-object__pricelist__item__name:nth-child(1)')
    FULL_AREA_INPUT = (By.CSS_SELECTOR, 'input[name="squareTotal"]')
    HOME_PROPERTIES_BLOCK = (By.CSS_SELECTOR, 'section[id="properties-home"]')
    KITCHEN_AREA = (By.CSS_SELECTOR, 'input[name="squareKitchen"]')
    LIVING_AREA_INPUT = (By.CSS_SELECTOR,'input[name="squareLive"]')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'a.adding-object__step-btns-next')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    PHOTO_INPUT = (By.CSS_SELECTOR, 'input[name="files[]"]')
    PRICE_BLOCK = (By.CSS_SELECTOR, 'section[id="price"]')
    PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="price"]')
    OBJECT_FLAT_BUTTON = (By.CSS_SELECTOR, 'div.adding-object__row:nth-child(4) '
                                           'label.radio-links-marker__container:nth-child(1)')
    PROPERTIES_BLOCK = (By.CSS_SELECTOR, 'section[id="properties"]')
    PROPERTY_FLAT_BUTTON = (By.CSS_SELECTOR, 'div.adding-object__row:nth-child(3) '
                                             'label.radio-links-marker__container:nth-child(1)')
    RENT_BUTTON = (By.CSS_SELECTOR, 'li.radio-tab__item:nth-child(2)')
    ROOMS_INPUT = (By.CSS_SELECTOR, 'input[name="rooms"]')
    SELL_BUTTON = (By.CSS_SELECTOR, 'li.radio-tab__item:nth-child(1)')
    STREET_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Укажите улицу..."]')
    SUCCESS_PAGE = (By.CSS_SELECTOR, 'div.success-page')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.success-page h1')


class UserItemsPageLocators:
    ADDRESS_LINK = (By.CSS_SELECTOR, 'a.ob-link.ng-binding')
    DELETE_FROM_MODERATION_BUTTON = (By.CSS_SELECTOR, 'a[ng-click="doneModeration()"]')
    ON_MODERATION_BUTTON = (By.CSS_SELECTOR, 'li.ng-binding:nth-child(2)')
    PRICE = (By.CSS_SELECTOR, 'div.ob-price>strong')
    SELECT_ALL_BUTTON = (By.CSS_SELECTOR, 'div.oby-bar-check')


class ItemPageLocators:
    PROPERTIES_ADDRESS = (By.CSS_SELECTOR, 'div:nth-child(2)>div>div>ul>li:nth-child(1)>'
                                           'div.object-info__details-table_property_value')
    PROPERTIES_DESCRIPTION = (By.CSS_SELECTOR, 'div.two-column__left > div:nth-child(9)')
    PROPERTIES_PRICE = (By.CSS_SELECTOR, 'div:nth-child(1)>div>div:nth-child(1)>ul>li:nth-child'
                                         '(1)>div.object-info__details-table_property_value')
    PROPERTIES_ROOMS = (By.CSS_SELECTOR, 'div:nth-child(1)>div>div:nth-child(1)>ul>li:nth-child'
                                         '(4)>div.object-info__details-table_property_value')
    PROPERTIES_FLOOR = (By.CSS_SELECTOR, 'div:nth-child(1)>div>div:nth-child(1)>ul>li:nth-child'
                                         '(5)>div.object-info__details-table_property_value')
    PROPERTIES_FLOORS = (By.CSS_SELECTOR, 'div:nth-child(2)>div>div>ul>li:nth-child(2)>'
                                          'div.object-info__details-table_property_value')
    PROPERTIES_FULL_AREA = (By.CSS_SELECTOR, 'div:nth-child(1)>div>div:nth-child(2)>ul>li:nth-child'
                                             '(2)>div.object-info__details-table_property_value')
    PROPERTIES_KITCHEN_AREA = (By.CSS_SELECTOR, 'div:nth-child(1)>div>div:nth-child(2)>ul>li:nth-child'
                                                '(4)>div.object-info__details-table_property_value')
    PROPERTIES_LIVING_AREA = (By.CSS_SELECTOR, 'div:nth-child(1)>div>div:nth-child(2)>ul>li:nth-child'
                                               '(3)>div.object-info__details-table_property_value')
    PROPERTIES_BLOCK_BOTTOM = (By.CSS_SELECTOR, 'div.object-page__bottom-button-line')
    TITLE = (By.CSS_SELECTOR, 'div.object-title_page-title')



