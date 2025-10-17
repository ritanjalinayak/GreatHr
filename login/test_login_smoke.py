

import pytest
from login.common_logic import Login_page

@pytest.mark.smoke
def test_swag_lab_login(login_fixture):
    driver=login_fixture
    obj=Login_page(driver)
    obj.username_field("standard_user")
    obj.password_field("secret_sauce")
    obj.login_click()
    assert driver.title=="Swag Labs"