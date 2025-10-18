from selenium.webdriver.common.by import By
class Login_page:
    def __init__(self,driver):
    
        self.driver=driver
        self.username=(By.ID, "user-name")
        self.password=(By.ID, "password")
        self.login=(By.ID, "login-button")
        self.errormsg=(By.TAG_NAME,"h3")
        

    def username_field(self,username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def  password_field(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def login_click(self):
        self.driver.find_element(*self.login).click()

    def error_msg(self):
        msg=self.driver.find_element(*self.errormsg).text
        print(msg)
        return msg

         


        
    