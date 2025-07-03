from base.base_page import BasePage
from pages.broken_links_page import Broken_list_page
from utils.driver import get_driver
import time

def test_verify_valid_image():
    driver = get_driver("https://demoqa.com/broken")
    base_page = BasePage(driver)
    broken_links_page = Broken_list_page(driver)
    assert broken_links_page.verify_valid_image()
    driver.quit()
# ------------------------------------------------------------------------------------------------------------------------------
def test_verify_broken_image():
    driver = get_driver("https://demoqa.com/broken")
    base_page = BasePage(driver)
    broken_links_page = Broken_list_page(driver)
    assert broken_links_page.verify_broken_image()
    driver.quit()

def test_click_valid_link():
    driver = get_driver("https://demoqa.com/broken")
    base_page = BasePage(driver)
    broken_links_page = Broken_list_page(driver)
    assert broken_links_page.click_valid_link()
    driver.quit()

def test_click_broken_link():
    driver = get_driver("https://demoqa.com/broken")
    base_page = BasePage(driver)
    broken_links_page = Broken_list_page(driver)
    assert broken_links_page.click_broken_link()
    driver.quit()