import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="function")
def login_fixture():
    driver=webdriver.Chrome()
    time.sleep(2)
    yield driver
    driver.quit()
