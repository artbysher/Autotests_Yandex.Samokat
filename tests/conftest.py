import pytest
from selenium import webdriver
from curl import *


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(MAIN_SITE)
    yield browser
    browser.quit()

