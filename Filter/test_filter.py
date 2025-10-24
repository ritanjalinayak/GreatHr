
import time
import pytest

from Filter.common_logic import filter_visible_test
from login.common_logic import Login_page


@pytest.mark.smoke
@pytest.mark.filter

def test_A_to_Z_alphabetes(setUp_fixture):
    driver=setUp_fixture

    # login to the application by using common logic.
    login_obj=Login_page(driver)
    login_obj.username_field("standard_user")
    login_obj.password_field("secret_sauce")
    login_obj.login_click()
    time.sleep(2)

    # Checking the filter by using filter class.
    obj4=filter_visible_test(driver)

    # checking for A to Z sorting
    obj4.dropdown_clicking(0)
    assert obj4.sorting_order()== True
    time.sleep(2)


    # Checking for Z to A sorting
    obj4.dropdown_clicking(1)
    assert obj4.reverse_true()== True
    time.sleep(2)

    # Checking for price lower to higher
    obj4.dropdown_clicking(2)
    assert obj4.price_checking() == True
    time.sleep(2)


    # Checking for price high to low.

    obj4.dropdown_clicking(3)
    assert obj4.CheckingPrice_H_to_low()==True





    

    
    

