from test_data.user_data import get_personal_data
import allure 



@allure.feature("My info")
@allure.story("Edit personal details")
def test_my_info(logged_in,my_info_page):
    logged_in.go_to_my_info()
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



@allure.feature("My info")
@allure.story("Validation - required fields")
def test_my_info_required_fields(logged_in,my_info_page):
    logged_in.go_to_my_info()
    assert my_info_page.is_loaded()
    my_info_page.clear_field('firstname')
    my_info_page.clear_field('lastname')
    firstname_error, lastname_error = my_info_page.get_validation_errors()    
    assert firstname_error == 'Required'
    assert lastname_error == 'Required'
    my_info_page.make_screenshot("Required fields")
    
