
import pytest

from AddToCart.commonLogic import cartpage


@pytest.mark.smoke
@pytest.mark.addtocart
def test_check_AddTOcart(setup_driver):
    driver =setup_driver
    call_class=cartpage(driver)
    call_class.check_addToCart()
    assert call_class.match_product()== True



@pytest.mark.verifyProduct
def test_verify_cartItem(setup_driver):
    driver=setup_driver
    call=cartpage(driver)
    call.add_one_product()
    call.click_cart_button()
    
    assert call.verifyCartItem()==True




    

