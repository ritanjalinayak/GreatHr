
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TotalProductCheckPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.addtocart_all=(By.CSS_SELECTOR, ".inventory_list .inventory_item")
        self.addTocart_button=(By.TAG_NAME,"button")
        self.check_item_name=(By.CLASS_NAME,"inventory_item_name")
        self.check_item_price=(By.CSS_SELECTOR, ".inventory_item_price")
        self.cartButton=(By.CLASS_NAME,"shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.firstName=(By.NAME, "firstName")
        self.lastName=(By.NAME, "lastName")
        self.postalCode=(By.ID, "postal-code")
        self.total_price=(By.CSS_SELECTOR,".cart_item .inventory_item_price")
        self.price_count=[]
        self.all_price=(By.CSS_SELECTOR,".summary_subtotal_label")
        self.finish_button=(By.NAME, "finish")
        self.succeussful_msg=(By.CLASS_NAME, "complete-header")
        self.tax=(By.CSS_SELECTOR,".summary_tax_label")
        self.countPRICE=(By.CLASS_NAME, "summary_total_label")



        



    def addITEM(self):
        products=self.wait.until(EC.visibility_of_all_elements_located(self.addtocart_all))
        needed_items = ["Sauce Labs Bike Light", 
                    "Sauce Labs Bolt T-Shirt", 
                    "Sauce Labs Fleece Jacket"]
        for item in products:
            product_name=item.find_element(*self.check_item_name).text
            if product_name in needed_items:
                price=item.find_element(*self.check_item_price).text
                item.find_element(*self.addTocart_button).click()
        return True
        
            

    def click_cart_button(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        
    #    element = self.wait.until(EC.element_to_be_clickable(self.cartButton))
    #    element.click()    
        time.sleep(2)
           


    def ClickCheckOutButton(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_button.click() 
        time.sleep(2)      
    
  
    # def ClickCheckOutButton(self):
    #     checkoutBUTTON=self.wait.until(EC.element_to_be_clickable(self.checkout_button))    
    #     checkoutBUTTON.click()
    #     time.sleep(2)




    def First_name(self,name):
        self.driver.find_element(*self.firstName).send_keys(name)

    def Last_name(self,name):
        self.driver.find_element(*self.lastName).send_keys(name)


    def Postal_code(self,number):
        self.driver.find_element(*self.postalCode).send_keys(number)



    def click_button(self):
        self.driver.find_element(By.ID,"continue").click()    

    #  Item total: $129.94
    def get_allPrice(self):
        sum_price=self.driver.find_element(*self.all_price).text
        total_value = float(sum_price.replace("Item total: $", ""))
        return total_value


    def price_check(self):
        pricess=self.driver.find_elements(*self.total_price)
        for price in pricess:
            price_value=float(price.text.replace("$", ""))
            self.price_count.append(price_value)
        print(sum(self.price_count))
        return sum(self.price_count)==self.get_allPrice()
    


    def Click_finishBUtton(self):
        self.driver.find_element(*self.finish_button).click()


    def sucess_msg(self):
        success_msg=self.driver.find_element(*self.succeussful_msg).text
        return success_msg=="Thank you for your order!"
    

        # Tax: $10.40
    def check_taxPrice(self):
        total_tax=self.driver.find_element(*self.tax).text
        tax=float(total_tax.replace ("Tax: $",""))
        return tax
    
       # Total: $140.34

    def all_price_check(self):
        gst=self.driver.find_element(*self.countPRICE).text
        gst_float=float(gst.replace("Total: $",""))

        return gst_float
    

    def checking_all(self):
        item_price=self.get_allPrice()
        tax_price=self.check_taxPrice()
        exp_sum=item_price+tax_price
        actual_sum=self.all_price_check()

        return exp_sum == actual_sum






        
        

       

    



        


    
    


    
        
    
              

    

    
        
              

              








        














        