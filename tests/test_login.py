import allure



@allure.feature("Authentication")
@allure.story("Successful login")
def test_login_successfully(login_page, admin_credentials,dashboard_page):
    login_page.open()
    login_page.enter_login(admin_credentials['username'])
    login_page.enter_password(admin_credentials['password'])
    login_page.click_submit_button()
    assert dashboard_page.is_loaded()
    login_page.make_screenshot("login successfully")
    
@allure.feature("Authentication")
@allure.story("Incorrect credentials")
def test_login_incorrect(login_page):
    login_page.open()
    with allure.step("Enter login: incorrect_username"):
        login_page.enter_login('incorrect_username')
    with allure.step("Enter password: incorrect_password"):
        login_page.enter_password('incorrect_password')
    login_page.click_submit_button()
    assert login_page.get_alert() == 'Invalid credentials'
    login_page.make_screenshot("login incorrect")
   
   
@allure.feature("Authentication") 
@allure.story("Empty fields validation")
def test_login_empty(login_page):
    login_page.open()
    login_page.click_submit_button()
    assert login_page.empty_login() == 'Required' 
    assert login_page.empty_password() == 'Required'
    login_page.make_screenshot("login or password empty")