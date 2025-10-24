

import pytest
import time
from selenium import webdriver


@pytest.fixture(scope="function")
def setUp_fixture():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    time.sleep(2)
    driver.quit()

