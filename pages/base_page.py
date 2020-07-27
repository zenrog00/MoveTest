from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.get(self.url)

    def get_element_text(self, selector_type, locator):
        return self.browser.find_element(selector_type, locator).text

    def is_element_present(self, selector_type, locator):
        try:
            self.browser.find_element(selector_type, locator)
        except NoSuchElementException:
            return False
        else:
            return True

    def move_to_element(self, selector_type, locator):
        element = self.browser.find_element(selector_type, locator)
        action = ActionChains(self.browser)
        action.move_to_element(element).perform()
