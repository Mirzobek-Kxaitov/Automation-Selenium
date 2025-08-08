import pytest
from utils.driver import get_driver
from pages.login_page import LoginPage
import time

@pytest.fixture
def driver():
    driver = get_driver("https://demoqa.com/login")
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def test_login_invalid_credentials(login_page):
    login_page.enter_username("mirzobek")
    login_page.logger.info("username kiritildi")

    login_page.enter_password("cDN!!asaCxbxva4")
    login_page.logger.info("password kiritildi")

    login_page.click_login()
    login_page.logger.info("login button bosildi")
    time.sleep(3)  # Error xabari chiqishini kutamiz
    login_page._take_screenshot()
