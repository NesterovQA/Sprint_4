import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    # firefox_options = Options()
    # firefox_options.add_argument('--window-size=1920,1080')
    yield driver
    driver.quit()
