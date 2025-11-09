import time
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
        self.original_price =""
        self.original_name=""
        

    def check_addToCart(self):
        all_products=self.wait.until(EC.visibility_of_all_elements_located(self.addtocart_all))
        for x in all_products:
            x.find_element(*self.addTocart_button).click()
            self.totalcart+=1
        print(self.totalcart)    

    def match_product(self):
        cart_badge = self.driver.find_element(*self.filter)
        return self.totalcart == int(cart_badge.text)


    
    # def add_one_product(self):
    #     one_items= self.driver.find_elements(*self.addtocart_all)

    #     self.original_price = one_items[2].find_element(*self.check_item_price).text
    #     self.original_name = one_items[2].find_element(*self.check_item_name).text
    #     one_items[2].find_element(*self.addTocart_button).click()

    

    def add_one_product(self):   
         one_items= self.driver.find_elements(*self.addtocart_all)
         for i in one_items:
            self.name = i.find_element(By.CLASS_NAME,"inventory_item_name").text
            if self.name == "Sauce Labs Bolt T-Shirt":
                self.price = i.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
                i.find_element(*self.addTocart_button).click()
                break
           
                
        
# clicking addtocart button.

    def click_cart_button(self):
       element = self.wait.until(
        EC.element_to_be_clickable(self.cartButton)
        )
       element.click()



    def verifyCartItem(self):
        productName=self.driver.find_element(By.CLASS_NAME,"inventory_item_name").text

        productPrice=self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text

        print(self.name)
        print(self.price)
        print(productName)
        print(productPrice)

        return productName==self.name and productPrice==self.price  



    












            
        

        
    
