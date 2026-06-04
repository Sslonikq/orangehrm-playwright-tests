from pages.base_page import BasePage


class MyInfoPage(BasePage):
    
    
    FIRSTNAME_FIELD = "//input[@name='firstName']"
    MIDDLENAME_FIELD = "//input[@name='middleName']"
    LASTNAME_FIELD = "//input[@name='lastName']"
    EMPLOYEE_ID_FIELD = '(//input[@class="oxd-input oxd-input--active"])[2]'
    OTHER_ID_FIELD = '(//input[@class="oxd-input oxd-input--active"])[3]'
    DRIVERS_LICENSE_FIELD = '(//input[@class="oxd-input oxd-input--active"])[4]'
    LICENSE_EXPIRY_FIELD = '(//input[@class="oxd-input oxd-input--active"])[5]'
    NATIONALY_FIELD = "(//div[@tabindex='0'])[1]"
    SAVE_FIELD = "(//button[@type='submit'])[1]"
    
    
        
    def save(self):
        self.page.wait_for_selector(self.SAVE_FIELD).click()
        
    def is_loaded(self):
        return self.page.get_by_text('Personal Details').is_visible()