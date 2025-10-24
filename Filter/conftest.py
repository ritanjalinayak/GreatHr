

import pytest
import time
from selenium import webdriver

from login.common_logic import Login_page


@pytest.fixture(scope="function")
def setUp_fixture():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    login_obj=Login_page(driver)
    login_obj.username_field("standard_user")
    login_obj.password_field("secret_sauce")
    login_obj.login_click()
    yield driver
    time.sleep(2)
    driver.quit()

