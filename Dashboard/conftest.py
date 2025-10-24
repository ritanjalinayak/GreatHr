
from selenium import webdriver
import time

import pytest

from login.common_logic import Login_page


@pytest.fixture(scope="function")
def fix_setup():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)
    login_obj=Login_page(driver)
    login_obj.username_field("standard_user")
    login_obj.password_field("secret_sauce")
    login_obj.login_click()
    yield driver
    time.sleep(2)
    driver.quit()
    
