from pages.base_page import BasePage
import allure 

class DashboardPage(BasePage):
    
    URL = '/web/index.php/dashboard/index'
    
    MY_INFO_FIELD = "//span[text()='My Info']"
    DASHBOARD_FIELD = '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]'
    
    
    @allure.step("Go to my info")
    def go_to_my_info(self):
        self.page.wait_for_selector(self.MY_INFO_FIELD).click()
        
    @allure.step("Check if dashboard page is loaded")
    def is_loaded(self):
        return self.page.wait_for_selector(self.DASHBOARD_FIELD).is_visible()