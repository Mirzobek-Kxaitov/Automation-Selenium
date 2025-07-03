from base.base_page import BasePage
from pages.dynamic_page import Dynamic_page
from utils.driver import get_driver
import time


def test_random_text_verification():
    driver = get_driver("https://demoqa.com/dynamic-properties")
    dynamic_page =Dynamic_page(driver)
    assert dynamic_page.verify_random_text_displayed()
    driver.quit()

def test_enable_button_functionality():
    driver = get_driver("https://demoqa.com/dynamic-properties")
    dynamic_page = Dynamic_page(driver)
    assert  dynamic_page.verify_enable_button_clickable()
    driver.quit()

def test_color_change_functionality():
    driver = get_driver("https://demoqa.com/dynamic-properties")
    dynamic_page = Dynamic_page(driver)
    assert  dynamic_page.verify_color_change()
    driver.quit()


def test_visible_button_functionality():
    driver = get_driver("https://demoqa.com/dynamic-properties")
    dynamic_page = Dynamic_page(driver)
    assert  dynamic_page.verification_visible_button()
    driver.quit()

