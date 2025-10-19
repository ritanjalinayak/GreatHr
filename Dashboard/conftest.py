
from selenium import webdriver
import time

import pytest


@pytest.fixture(scope="function")
def fix_setup():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)
    yield driver
    time.sleep(2)
    driver.quit()
    
