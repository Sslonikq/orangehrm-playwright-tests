from pages.base_page import BasePage
import random
import allure
class MyInfoPage(BasePage):
    
    PERSONAL_FIELD = '//h6[text()="Personal Details"]'
    FIRSTNAME_FIELD = "//input[@name='firstName']"
    MIDDLENAME_FIELD = "//input[@name='middleName']"
    LASTNAME_FIELD = "//input[@name='lastName']"
    EMPLOYEE_ID_FIELD = "//label[text()='Employee Id']/../..//input"
    OTHER_ID_FIELD = "//label[text()='Other Id']/../..//input"
    DRIVERS_LICENSE_FIELD = '//label[text()="Driver\'s License Number"]/../..//input'
    LICENSE_EXPIRY_FIELD = "//label[text()='License Expiry Date']/../..//input"
    NATIONALY_FIELD = "(//div[@tabindex='0'])[1]"
    SAVE_FIELD = "(//button[@type='submit'])[1]"
    NATIONALITY_OPTIONS = "//div[@role='option']"
    SUCCES_MESSAGE = "//div[@class='oxd-toast-content oxd-toast-content--success']"
    SPINNER_FIELD = "//div[@class='oxd-loading-spinner']"
    
    @allure.step("Click save button")   
    def save(self):
        self.page.wait_for_selector(self.SAVE_FIELD).click()

        
    def is_loaded(self):
        return self.page.wait_for_selector(self.PERSONAL_FIELD).is_visible()
    
    def is_saved(self):
        return self.page.wait_for_selector(self.SUCCES_MESSAGE).is_visible()
    
    @allure.step("Enter firstname")
    def enter_firstname(self,firstname):
        return self.page.wait_for_selector(self.FIRSTNAME_FIELD).fill(firstname)
    
    @allure.step("Enter middlename")
    def enter_middlename(self,middlename):
        return self.page.wait_for_selector(self.MIDDLENAME_FIELD).fill(middlename)
    
    @allure.step("Enter lastname")
    def enter_lastname(self,lastname):
        return self.page.wait_for_selector(self.LASTNAME_FIELD).fill(lastname)
    
    @allure.step("Enter employee id")
    def enter_employee_id(self,employee_id):
        return self.page.wait_for_selector(self.EMPLOYEE_ID_FIELD).fill(employee_id)
    
    @allure.step("Enter other id")
    def enter_other_id(self,other_id):
        return self.page.wait_for_selector(self.OTHER_ID_FIELD).fill(other_id)
    
    @allure.step("Enter drivers license")
    def enter_drivers_license(self,drivers_license):
        return self.page.wait_for_selector(self.DRIVERS_LICENSE_FIELD).fill(drivers_license)
    
    @allure.step("Enter license expiry")
    def enter_license_expiry(self,license_expiry):
        return self.page.wait_for_selector(self.LICENSE_EXPIRY_FIELD).fill(license_expiry)
    
    
    def wait_for_spinner(self):
        self.page.wait_for_selector(self.SPINNER_FIELD, state = 'hidden')
    
    @allure.step("Enter nationality")
    def enter_nationality(self):
        self.page.wait_for_selector(self.NATIONALY_FIELD).click()
        options = self.page.query_selector_all(self.NATIONALITY_OPTIONS)
        option = random.choice(options)
        nationality = option.inner_text()
        option.click()
        return nationality
    
    

    def fill_person_data(self,data):
        self.wait_for_spinner()
        self.enter_firstname(data['firstname'])
        self.enter_middlename(data['middlename'])
        self.enter_lastname(data['lastname'])
        self.enter_employee_id(data['employee_id'])
        self.enter_other_id(data['other_id'])
        self.enter_drivers_license(data['drivers_license'])
        self.enter_license_expiry(data['license_expiry'])
        self.page.keyboard.press("Escape")
        data['nationality'] = self.enter_nationality()



    def get_data(self):
        data = {}
        data['firstname'] = self.page.wait_for_selector(self.FIRSTNAME_FIELD).input_value()
        data['middlename'] = self.page.wait_for_selector(self.MIDDLENAME_FIELD).input_value()
        data['lastname'] = self.page.wait_for_selector(self.LASTNAME_FIELD).input_value()
        data['employee_id'] = self.page.wait_for_selector(self.EMPLOYEE_ID_FIELD).input_value()
        data['other_id'] = self.page.wait_for_selector(self.OTHER_ID_FIELD).input_value()
        data['drivers_license'] = self.page.wait_for_selector(self.DRIVERS_LICENSE_FIELD).input_value()
        data['license_expiry'] = self.page.wait_for_selector(self.LICENSE_EXPIRY_FIELD).input_value()
        data['nationality'] = self.page.wait_for_selector(self.NATIONALY_FIELD).inner_text()
        return data