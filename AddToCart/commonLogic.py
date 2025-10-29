from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class cartpage:
    
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.totalcart=0
        self.addtocart_all=(By.CSS_SELECTOR, ".inventory_list .inventory_item")
        self.addTocart_button=(By.TAG_NAME,"button")
        self.filter=(By.CLASS_NAME,"shopping_cart_badge")
        self.cartButton=(By.CLASS_NAME,"shopping_cart_link")
        self.check_item_name=(By.CLASS_NAME,"inventory_item_name")
        self.check_item_price=(By.CSS_SELECTOR, ".inventory_item_price")
        

    def check_addToCart(self):
        all_products=self.wait.until(EC.visibility_of_all_elements_located(self.addtocart_all))
        for x in all_products:
            x.find_element(*self.addTocart_button).click()
            self.totalcart+=1
        print(self.totalcart)    

    def match_product(self):
        cart_badge = self.driver.find_element(*self.filter)
        return self.totalcart == int(cart_badge.text)
    
    def add_one_product(self):
        one_items=self.driver.find_elements(*self.addtocart_all)
        for item in one_items:
            if item.text=="Sauce Labs Bolt T-Shirt":
               self.driver.find_element(*self.add_one_product).click()


    def click_cart_button(self):
        self.driver.find_element(*self.cartButton).click()



    def verifyCart(self):
        return self.











            
        

        
    
