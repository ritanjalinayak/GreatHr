
import time
import pytest
from PlaceOrder.commonlogic import TotalProductCheckPage
from login.common_logic import Login_page


@pytest.mark.smoke
@pytest.mark.additem

def test_addMaterial(setup_browser):
    driver=setup_browser
    obj=Login_page(driver)
    obj.username_field("standard_user")
    obj.password_field("secret_sauce")
    obj.login_click()
    

    cart=TotalProductCheckPage(driver)
    cart.addITEM() 
    cart.click_cart_button()
    cart.ClickCheckOutButton()
    time.sleep(2)
    cart.First_name("Ritanjali")
    cart.Last_name("Nayak")
    cart.Postal_code(751030)
    cart.click_button()
    assert cart.price_check()==True
   
@pytest.mark.PlaceOrder    
def test_placeOrder(setup_browser):
    driver=setup_browser
    obj=Login_page(driver)
    obj.username_field("standard_user")
    obj.password_field("secret_sauce")
    obj.login_click()
    

    cart=TotalProductCheckPage(driver)
    cart.addITEM() 
    cart.click_cart_button()
    cart.ClickCheckOutButton()
    time.sleep(2)
    cart.First_name("Ritanjali")
    cart.Last_name("Nayak")
    cart.Postal_code(751030)
    cart.click_button()
    assert cart.sucess_msg()==True
    



    
