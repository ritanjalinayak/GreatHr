from selenium.webdriver.common.by import By


class sidebarpage:
    def __init__(self,driver):
        self.driver=driver
        self.menu_items = (By.CSS_SELECTOR, "nav.bm-item-list a")
        self.click_sideBar=(By.ID, "react-burger-menu-btn")


    def check_sideBar(self):
        self.driver.find_element(*self.click_sideBar).click()

    def check_naveItem(self):
        items=self.driver.find_elements(*self.menu_items)
        print(len(items))  
        return (len(items))==4






        
        






        