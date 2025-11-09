import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="function")
def setup_browser():

    options = Options()
    # ✅ Incognito mode
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    yield driver
    time.sleep(1)
    driver.quit()
