from selenium.webdriver.common.by import By

class dashboard_page:
    def __init__(self,driver):
        self.driver=driver
        self.expected_url="https://www.saucedemo.com/inventory.html"
        self.menu_button=(By.ID,"react-burger-menu-btn")
        self.dropdown_visible=(By.CLASS_NAME,"product_sort_container")
        self.dashboard_title=(By.CLASS_NAME, "app_logo")
        self.cart_visible=(By.CLASS_NAME,"shopping_cart_link")
    def Check_cart(self):
        return self.driver.find_element(*self.cart_visible).is_displayed() 

    def dashboardTitle(self):
        return self.driver.find_element(*self.dashboard_title).text

    def is_url_correct(self):
        return self.driver.current_url == self.expected_url    

    def sort_menu(self):
        return self.driver.find_element(*self.menu_button).is_displayed()
    def is_dropdown_visible(self):
        return self.driver.find_element(*self.dropdown_visible).is_displayed()
    










        

        