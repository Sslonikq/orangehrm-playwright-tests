from pages.base_page import BasePage
import random
import allure


class MyInfoPage(BasePage):

    PERSONAL_FIELD = '//h6[text()="Personal Details"]'
    NATIONALITY_FIELD = "(//div[@tabindex='0'])[1]"
    SAVE_FIELD = "(//button[@type='submit'])[1]"
    NATIONALITY_OPTIONS = "//div[@role='option']"
    SUCCESS_MESSAGE = "//div[@class='oxd-toast-content oxd-toast-content--success']"
    SPINNER_FIELD = "//div[@class='oxd-loading-spinner']"

    _FIELD_MAP = {
        "firstname":       "//input[@name='firstName']",
        "middlename":      "//input[@name='middleName']",
        "lastname":        "//input[@name='lastName']",
        "employee_id":     "//label[text()='Employee Id']/../..//input",
        "other_id":        "//label[text()='Other Id']/../..//input",
        "drivers_license": '//label[text()="Driver\'s License Number"]/../..//input',
        "license_expiry":  "//label[text()='License Expiry Date']/../..//input",
    }

    @allure.step("Click save button")
    def save(self):
        self.page.wait_for_selector(self.SAVE_FIELD).click()

    def is_loaded(self):
        return self.page.wait_for_selector(self.PERSONAL_FIELD).is_visible()

    def is_saved(self):
        return self.page.wait_for_selector(self.SUCCESS_MESSAGE).is_visible()

    def wait_for_spinner(self):
        self.page.wait_for_selector(self.SPINNER_FIELD, state='hidden')

    @allure.step("Enter nationality")
    def enter_nationality(self):
        self.page.wait_for_selector(self.NATIONALITY_FIELD).click()
        options = self.page.query_selector_all(self.NATIONALITY_OPTIONS)
        option = random.choice(options)
        nationality = option.inner_text()
        option.click()
        return nationality

    def fill_person_data(self, data):
        self.wait_for_spinner()
        for key, selector in self._FIELD_MAP.items():
            with allure.step(f"Enter {key}: {data[key]}"):
                self.page.wait_for_selector(selector).fill(data[key])
        self.page.keyboard.press("Escape")
        data['nationality'] = self.enter_nationality()

    def get_data(self):
        data = {}
        for key, selector in self._FIELD_MAP.items():
            data[key] = self.page.wait_for_selector(selector).input_value()
        data['nationality'] = self.page.wait_for_selector(self.NATIONALITY_FIELD).inner_text()
        return data