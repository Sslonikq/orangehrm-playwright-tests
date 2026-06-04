from pages.base_page import BasePage



class LoginPage(BasePage):
    
    URL = '/web/index.php/auth/login'
    
    USER_NAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    
    
    def open(self):
        self.navigate(self.URL)
    
    
    
    def enter_login(self,login):
        self.page.wait_for_selector(self.USER_NAME_FIELD).fill(login)
        
        
        
    def enter_password(self,password):
        self.page.wait_for_selector(self.PASSWORD_FIELD).fill(password)
        
        
        
    def click_submit_button(self):
        self.page.wait_for_selector(self.LOGIN_BUTTON).click()



    def login(self, username, password):
        self.enter_login(username)
        self.enter_password(password)
        self.click_submit_button()
        