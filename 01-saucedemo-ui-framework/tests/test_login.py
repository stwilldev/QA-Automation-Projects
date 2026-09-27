import json
import os
import pytest
from pages.login_page import LoginPage

# Load test data from JSON file safely relative to this file's path
data_file_path = os.path.join(os.path.dirname(__file__), "..", "test_data.json")
with open(data_file_path, "r") as f:
    test_data = json.load(f)

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    
    # Pulling data dynamically from JSON
    user = test_data["users"]["valid"]
    login_page.login(user["username"], user["password"])
    
    # Verify login success by checking target URL
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    
    # Pulling locked user data dynamically from JSON
    user = test_data["users"]["locked"]
    login_page.login(user["username"], user["password"])
    
    # Verify error message for locked out user
    error_msg = login_page.get_error_text()
    assert "Epic sadface: Sorry, this user has been locked out." in error_msg