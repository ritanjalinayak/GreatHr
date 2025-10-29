

import time
from selenium import webdriver
import pytest

from login.common_logic import Login_page


@pytest.fixture(scope="function")
def setup_driver():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/inventory.html")
    driver.maximize_window()
    login_obj=Login_page(driver)
    login_obj.username_field("standard_user")
    login_obj.password_field("secret_sauce")
    login_obj.login_click()
    time.sleep(2)
    yield driver
    time.sleep(2)
    driver.quit()
 