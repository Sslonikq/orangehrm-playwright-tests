import pytest 
import os 
from dotenv import load_dotenv 

load_dotenv()



@pytest.fixture()
def admin_credentials():
    return {
        "username": os.getenv("ADMIN_USERNAME"), 
        'password': os.getenv("ADMIN_PASSWORD")
    }