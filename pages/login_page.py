from pages.base_page import BasePage
import allure 
from allure_commons.types import ParameterMode

class LoginPage(BasePage):
    
    URL = '/web/index.php/auth/login'
    
    USER_NAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    ALERT_FIELD = "//div[@role='alert']"
    EMPTY_LOGIN_FIELD = "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'])[1]"
    EMPTY_PASSWORD_FIELD = "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'])[2]"
    
    
    def open(self):
        self.navigate(self.URL)
    
    

    def enter_login(self,login):
        with allure.step("Enter login"):
            self.page.wait_for_selector(self.USER_NAME_FIELD).fill(login)
        
        
  
    def enter_password(self,password):
        with allure.step("Enter password"):
            self.page.wait_for_selector(self.PASSWORD_FIELD).fill(password)
        
        
    @allure.step("Click submit button")
    def click_submit_button(self):
        self.page.wait_for_selector(self.LOGIN_BUTTON).click()
        
    @allure.step("Get alert message")
    def get_alert(self):
        return self.page.wait_for_selector(self.ALERT_FIELD).inner_text()

    @allure.step("Get empty login message")
    def empty_login(self):
        return self.page.wait_for_selector(self.EMPTY_LOGIN_FIELD).inner_text()
    
    @allure.step("Get empty password message")
    def empty_password(self):
        return self.page.wait_for_selector(self.EMPTY_PASSWORD_FIELD).inner_text()


 
        