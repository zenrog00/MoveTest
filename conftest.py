import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help="Choose browser: chrome, firefox, opera")


@pytest.fixture(scope='class')
def browser(request):
    browser_name = request.config.getoption('browser')
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    elif browser_name == 'opera':
        browser = webdriver.Opera
    else:
        raise pytest.UsageError('Browser should be: chrome, firefox or opera')
    yield browser
    browser.quit()
