
import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="function")
def login_fixture():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    yield driver
    time.sleep(3)
    driver.quit()