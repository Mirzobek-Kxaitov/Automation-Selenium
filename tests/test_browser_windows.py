from selenium.webdriver.support.wait import WebDriverWait
from pages.browser_windows import Browser_windows_page
from selenium.webdriver.support import expected_conditions as EC
import pytest

#------------------------------------------------------------------------------------------------------------
def test_new_tab_functionality(driver):
    browser_windows_page = Browser_windows_page(driver)
    browser_windows_page.logger.info("STARTING TEST: test_new_tab_functionality")
    driver.get("https://demoqa.com/browser-windows")
    initial_tab_count = len(driver.window_handles)
    browser_windows_page.logger.info(f" Initial tab count: {initial_tab_count}")
    browser_windows_page.click_new_tab()

    try:
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(initial_tab_count + 1))
        all_handles = driver.window_handles
        new_tab_handle = all_handles[-1]
        driver.switch_to.window(new_tab_handle)
        assert "This is a sample page" in driver.page_source
        browser_windows_page.logger.info("New tab opened and content verified successfully.")
        driver.close()
        driver.switch_to.window(all_handles[0])
    except Exception as e:
        pytest.fail(f"New tab test failed: {e}")
#------------------------------------------------------------------------------------------------------------
def test_new_window_functionality(driver):
    browser_windows_page = Browser_windows_page(driver)
    browser_windows_page.logger.info("STARTING TEST: test_new_window_functionality")
    driver.get("https://demoqa.com/browser-windows")
    initial_window_count = len(driver.window_handles)
    browser_windows_page.logger.info(f" Initial window count: {initial_window_count}")
    browser_windows_page.click_new_window()
    try:
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(initial_window_count + 1))
        all_handles = driver.window_handles
        new_window_handle = all_handles[-1]
        driver.switch_to.window(new_window_handle)
        assert "This is a sample page" in driver.page_source
        browser_windows_page.logger.info("New window opened and content verified successfully.")
        driver.close()
        driver.switch_to.window(all_handles[0])

    except Exception as e:
        pytest.fail(f"New window test failed: {e}")
# ------------------------------------------------------------------------------------------------------------
def test_new_window_message_functionality(driver):
    browser_windows_page = Browser_windows_page(driver)
    browser_windows_page.logger.info("STARTING TEST: test_new_window_message_functionality")
    driver.get("https://demoqa.com/browser-windows")
    initial_window_count = len(driver.window_handles)
    browser_windows_page.logger.info(f"Initial window count: {initial_window_count}")
    browser_windows_page.click_new_window_message()
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(initial_window_count + 1)
    )
    current_window_count = len(driver.window_handles)
    browser_windows_page.logger.info(f"Current window count: {current_window_count}")
    assert current_window_count > initial_window_count, \
        f"Yangi oyna ochilmadi. Kutilgan: {initial_window_count + 1}, Haqiqiy: {current_window_count}"
    browser_windows_page.logger.info("Test muvaffaqiyatli o'tdi!")


