import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




class filter_visible_test:
    def __init__(self,driver):
        self.driver=driver
        self.username=(By.ID, "user-name")
        self.password=(By.ID, "password")
        self.login=(By.ID, "login-button")
        self.dropdown=(By.TAG_NAME,"select")
        self.name=(By.CLASS_NAME,"inventory_item_name")
        self.checking_price=(By.CLASS_NAME, "inventory_item_price")
        self.sorting_checking=[]
        self.current_prices=[]
        


    def dropdown_clicking(self,index):      
      dropdown_element = self.driver.find_element(*self.dropdown)
      select = Select(dropdown_element)
      select.select_by_index(index)    

    
      
    def sorting_order(self):
        self.getproduct_name()
        return self.sorting_checking == sorted(self.sorting_checking)

      
    def reverse_true(self):
        self.getproduct_name()
        return self.sorting_checking == sorted(self.sorting_checking,reverse=True) 
    

    def getproduct_name(self):
        self.sorting_checking =[]
        total=self.driver.find_elements(*self.name)
        for x in total:
            self.sorting_checking.append(x.text)


    
    def price_checking(self):
        self.getPrices()
        return self.current_prices == sorted(self.current_prices)
    

    def CheckingPrice_H_to_low(self):
        self.getPrices()
        return self.current_prices ==sorted(self.current_prices,reverse=True)
    
    # common function for get the price of product

    def getPrices(self):
        self.current_prices=[]
        all_price=self.driver.find_elements(*self.checking_price)
        for y in all_price:
            a=y.text[1:]
            b=float(a)
            self.current_prices.append(b)


        
            
        


    



    

    
    


     
     




        








        
           



        