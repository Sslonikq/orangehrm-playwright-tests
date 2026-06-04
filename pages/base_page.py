



class BasePage:
    def __init__(self, page):
        self.page = page
        
    def navigate(self, url):
        self.page.goto(url)
        
    def page_title(self):
        return self.page.title 
    