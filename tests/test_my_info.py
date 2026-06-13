from test_data.user_data import get_personal_data
import allure 



@allure.feature("My info")
@allure.story("Edit personal details")
def test_my_info(admin_credentials,login_page,dashboard_page,my_info_page):
    login_page.open()
    login_page.enter_login(admin_credentials['username'])
    login_page.enter_password(admin_credentials['password'])
    login_page.click_submit_button()
    dashboard_page.go_to_my_info()
    assert my_info_page.is_loaded()
    data = get_personal_data()
    my_info_page.fill_person_data(data)
    my_info_page.save() 
    assert my_info_page.is_saved()
    actual = my_info_page.get_data()
    assert actual['firstname'] == data['firstname']
    assert actual['lastname'] == data['lastname']
    assert actual['middlename'] == data['middlename']
    assert actual['employee_id'] == data['employee_id']
    assert actual['other_id'] == data['other_id']
    assert actual['drivers_license'] == data['drivers_license']
    assert actual['license_expiry'] == data['license_expiry']
    assert actual['nationality'] == data['nationality']
    my_info_page.wait_for_spinner()
    my_info_page.make_screenshot("after_save")
