from base.base_page import BasePage
from pages.browser_windows import Browser_windows_page
from utils.driver import get_driver
import logging


def test_new_tab_functionality():
    driver = get_driver("https://demoqa.com/browser-windows")
    browser_windows_page = Browser_windows_page(driver)

    # BasePage logger'ni ishlatish
    browser_windows_page.logger.info("STARTING TEST: test_new_tab_functionality")

    initial_tab_count = len(driver.window_handles)
    browser_windows_page.logger.info(f" Initial tab count: {initial_tab_count}")

    browser_windows_page.click_new_tab()

    current_tab_count = len(driver.window_handles)
    browser_windows_page.logger.info(f" Current tab count: {current_tab_count}")

    assert current_tab_count > initial_tab_count
    browser_windows_page.logger.info(" Test passed!")

    driver.quit()

def test_new_window_functionality():
    driver = get_driver("https://demoqa.com/browser-windows")
    browser_windows_page = Browser_windows_page(driver)
    browser_windows_page.logger.info("STARTING TEST: test_new_window_functionality")
    initial_window_count = len(driver.window_handles)
    browser_windows_page.logger.info(f" Initial window count: {initial_window_count}")
    browser_windows_page.click_new_window()
    current_window_count = len(driver.window_handles)
    browser_windows_page.logger.info(f" Current window count: {current_window_count}")
    assert current_window_count > initial_window_count
    browser_windows_page.logger.info(" Test passed!")

    driver.quit()

def test_new_window_message_functionality():
    driver = get_driver("https://demoqa.com/browser-windows")
    browser_windows_page = Browser_windows_page(driver)
    browser_windows_page.logger.info("STARTING TEST: test_new_window_message_functionality")
    initial_new_window_message = len(driver.window_handles)
    browser_windows_page.logger.info(f" Initial new_window_message count: {initial_new_window_message}")
    browser_windows_page.click_new_window_message()
    current_new_window_message_count  = len(driver.window_handles)
    browser_windows_page.logger.info(f" Current new_window_message count: {current_new_window_message_count}")
    assert current_new_window_message_count > initial_new_window_message
    browser_windows_page.logger.info(" Test passed!")

    driver.quit()


