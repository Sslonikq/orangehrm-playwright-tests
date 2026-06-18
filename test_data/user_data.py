from faker import Faker
from datetime import date
fake = Faker()


def get_personal_data():
    firstname = fake.first_name()
    middlename = fake.first_name()
    lastname = fake.last_name()
    employee_id = str(fake.random_number(digits=4))
    other_id = str(fake.random_number(digits=4))
    drivers_license = fake.bothify(text="??######")
    license_expiry = fake.date_between(start_date=date.today(), end_date=date(2030, 1, 1)).strftime("%Y-%m-%d")
    return {
        "firstname": firstname,
        "middlename": middlename,
        "lastname": lastname,
        "employee_id": employee_id,
        "other_id": other_id,
        "drivers_license": drivers_license,
        "license_expiry": license_expiry,
    }

    