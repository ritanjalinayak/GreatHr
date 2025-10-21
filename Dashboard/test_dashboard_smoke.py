

import pytest

from Dashboard.common_logic import dashboard_page
from login.common_logic import Login_page


@pytest.mark.smoke
@pytest.mark.dashboard
def test_dashboard_checking(fix_setup):

    driver=fix_setup
    login_obj=Login_page(driver)
    login_obj.username_field("standard_user")
    login_obj.password_field("secret_sauce")
    login_obj.login_click()

    obj=dashboard_page(driver)

    assert obj.dashboardTitle()=="Swag Labs"
    assert obj.is_url_correct()==True
    assert obj.sort_menu()==True
    assert obj.is_dropdown_visible()==True
    assert obj.Check_cart()==True





