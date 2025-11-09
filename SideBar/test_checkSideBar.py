
import time
import pytest
from PlaceOrder.commonlogic import TotalProductCheckPage
from SideBar.commonlogic import sidebarpage
from login.common_logic import Login_page


@pytest.mark.smoke
@pytest.mark.SideBar

def test_addMaterial(setup_browser):
    driver=setup_browser
    obj=Login_page(driver)
    obj.username_field("standard_user")
    obj.password_field("secret_sauce")
    obj.login_click()


    sidebarobj=sidebarpage(driver)
    sidebarobj.check_sideBar()
    assert sidebarobj.check_naveItem()==True
