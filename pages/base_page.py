import allure



class BasePage:
    def __init__(self, page):
        self.page = page
        
    def navigate(self, url):
        self.page.goto(url)
        
    
    def make_screenshot(self,screen_name):
        allure.attach(
            body=self.page.screenshot(),
            name=screen_name,
            attachment_type=allure.attachment_type.PNG
        )