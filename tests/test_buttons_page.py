from base.base_page import BasePage
from pages.buttons_page import Buttons_page
from utils.driver import get_driver
import time

def test_double_click():
    driver = get_driver("https://demoqa.com/buttons")
    base_page = BasePage(driver)
    buttons_page = Buttons_page(driver)
    buttons_page.double_click_button_action()
    time.sleep(5)
    driver.quit()

def test_right_click():
    driver = get_driver("https://demoqa.com/buttons")
    base_page = BasePage(driver)
    buttons_page = Buttons_page(driver)
    buttons_page.right_click_button_action()
    time.sleep(5)
    driver.quit()


def test_simple_click():
    driver = get_driver("https://demoqa.com/buttons")
    base_page = BasePage(driver)
    buttons_page = Buttons_page(driver)
    buttons_page.simple_click_button_action()
    time.sleep(3)
    driver.quit()