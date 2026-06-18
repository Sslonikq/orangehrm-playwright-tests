import allure
import pytest



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
@pytest.mark.parametrize('username, password', 
                         [
                             ('incorrect_username' , 'incorrect_password') ,
                             ('Admin' , 'wrong_password') , 
                             ('wrong_username' , 'admin1234')
                         ])
def test_login_incorrect(login_page, username, password):
    login_page.open()
    with allure.step(f"Enter login: {username}"):
        login_page.enter_login(username)
    with allure.step(f"Enter password: {password}"):
        login_page.enter_password(password)
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