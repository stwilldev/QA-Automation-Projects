import os
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Automatically switch to headless mode in Github Actions CI
    if os.environ.get("CI"):
        options.add_argument(--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument(--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
    else:
        options.add_argument("--start-maximized")
        
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
