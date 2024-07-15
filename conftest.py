import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1280,720')
    driver = webdriver.Chrome(options=options)
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.delete_all_cookies()
    driver.quit()
