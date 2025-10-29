
import pytest

from AddToCart.commonLogic import cartpage


@pytest.mark.smoke
@pytest.mark.addtocart
def test_check_AddTOcart(setup_driver):
    driver =setup_driver
    call_class=cartpage(driver)
    call_class.check_addToCart()
    assert call_class.match_product()== True



    

