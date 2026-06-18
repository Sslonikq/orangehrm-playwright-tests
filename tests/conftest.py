import pytest 
import os 
from dotenv import load_dotenv 
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage
import allure

load_dotenv()



@pytest.fixture(scope="session")
def admin_credentials():
    return {
        "username": os.getenv("ADMIN_USERNAME"), 
        'password': os.getenv("ADMIN_PASSWORD")
    }
    
    
@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    return login_page


@pytest.fixture()
def dashboard_page(page):
    dashboard_page = DashboardPage(page)
    return dashboard_page


@pytest.fixture()
def my_info_page(page):
    my_info_page = MyInfoPage(page)
    return my_info_page



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture()
def logged_in(login_page,dashboard_page,admin_credentials):
    login_page.open()
    login_page.enter_login(admin_credentials['username'])
    login_page.enter_password(admin_credentials['password'])
    login_page.click_submit_button()
    return dashboard_page