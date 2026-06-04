from pages.base_page import BasePage


class DashboardPage(BasePage):
    
    URL = '/web/index.php/dashboard/index'
    
    MY_INFO_FIELD = "//span[text()='My Info']"
    
    
    def go_to_my_info(self):
        self.page.wait_for_selector(self.MY_INFO_FIELD).click()
        
    def is_loaded(self):
        return self.page.get_by_text('Dashboard').is_visible()