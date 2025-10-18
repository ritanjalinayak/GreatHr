

import pytest

from login.common_logic import Login_page



@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected", [
    ("", "", "Epic sadface: Username is required"),
    ("wrong_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "", "Epic sadface: Password is required"),
])
def test_regression(login_fixture,username,password,expected):
    driver=login_fixture
    obj=Login_page(driver)
    obj.username_field(username) 
    obj.password_field(password)
    obj.login_click()
    assert expected in obj.error_msg()  
