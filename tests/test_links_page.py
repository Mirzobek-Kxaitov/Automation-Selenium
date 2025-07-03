from base.base_page import BasePage
from pages.links_page import Links_page
from utils.driver import get_driver
import time

# def test_home_button():
#     driver = get_driver("https://demoqa.com/links")
#     base_page = BasePage(driver)
#     links_page = Links_page(driver)
#
#     links_page.click_home_button()
#     time.sleep(5)
#     driver.quit()
#
# def test_new_tab_functionality():
#     driver = get_driver("https://demoqa.com/links")
#     links_page = Links_page(driver)
#     links_page.logger.info("Starting test...")  # Log yozish
#     links_page.click_home_button()
#     links_page.logger.info("Home button clicked")
#     time.sleep(3)
#     links_page.switch_to_new_tab()
#     links_page.logger.info("Switched to new tab")
#     links_page.logger.info(f"Current URL: {driver.current_url}")
#     time.sleep(3)
#     assert driver.current_url == "https://demoqa.com/"
#     links_page.logger.info("Assertion passed!")
#     time.sleep(3)
#     driver.quit()
#     links_page.logger.info("Test completed")

#
# def test_multiple_windows_handling():
#     driver = get_driver("https://demoqa.com/links")
#     links_page = Links_page(driver)
#     links_page.logger.info("Starting multiple windows handling test")
#     original_window = links_page.get_original_window()
#     links_page.logger.info(f"Original window saved: {original_window}")
#     links_page.click_home_button()
#     links_page.logger.info("Home button clicked - new tab should open")
#     links_page.switch_to_new_tab()
#     links_page.logger.info("Switched to new tab")
#     links_page.logger.info(f"Current URL in new tab: {driver.current_url}")
#     links_page.close_current_tab()
#     links_page.logger.info("New tab closed")
#     links_page.switch_to_original_tab(original_window)
#     links_page.logger.info("Switched back to original tab")
#     links_page.logger.info(f"Back to original URL: {driver.current_url}")
#     links_page.logger.info("Multiple windows handling test completed")
#     time.sleep(3)
#     driver.quit()

def test_api_response_functionality():
    driver = get_driver("https://demoqa.com/links")
    links_page = Links_page(driver)
    links_page.logger.info("Starting API response test")
# ------------------------------------------------------------------------------------------------------------------------------
    links_page.click_created_button()
    links_page.logger.info("Created button clicked")
    time.sleep(3)
    response_text = links_page.verify_response_message()
    links_page.logger.info(f"Response message: {response_text}")
    assert "201" in response_text and "Created" in response_text
    links_page.logger.info("API response verification passed!")
# ------------------------------------------------------------------------------------------------------------------------------
    links_page.click_no_content_button()
    links_page.logger.info("No content button clicked")
    time.sleep(3)
    response_text = links_page.verify_response_message()
    links_page.logger.info(f"Response message: {response_text}")
    assert "204" in response_text and "No Content" in response_text
    links_page.logger.info("API response verification passed!")
# ------------------------------------------------------------------------------------------------------------------------------
    links_page.click_moved_button()
    links_page.logger.info("Moved Permanently button clicked")
    time.sleep(3)
    response_text = links_page.verify_response_message()
    links_page.logger.info(f"Response message: {response_text}")
    assert "301" in response_text and "Moved Permanently" in response_text
    links_page.logger.info("API response verification passed")
# ------------------------------------------------------------------------------------------------------------------------------
    links_page.click_bad_request_button()
    links_page.logger.info("Bad request button clicked")
    time.sleep(3)
    response_text = links_page.verify_response_message()
    links_page.logger.info(f"Response message: {response_text}")
    assert "400 " in response_text and "Bad Request" in response_text
    links_page.logger.info("API response verification passed!")
# ------------------------------------------------------------------------------------------------------------------------------
    links_page.click_unauthorized_button()
    links_page.logger.info("Unauthorized button clicked")
    time.sleep(3)
    response_text = links_page.verify_response_message()
    links_page.logger.info(f"Response message: {response_text}")
    assert "401 " in response_text and "Unauthorized" in response_text
    links_page.logger.info("API response verification passed!")
# ------------------------------------------------------------------------------------------------------------------------------
    links_page.click_forbidden_button()
    links_page.logger.info("Forbidden button clicked")
    time.sleep(3)
    response_text = links_page.verify_response_message()
    links_page.logger.info(f"Response message: {response_text}")
    assert "403 " in response_text and "Forbidden" in response_text
    links_page.logger.info("API response verification passed!")
# ------------------------------------------------------------------------------------------------------------------------------
    links_page.click_not_found_button()
    links_page.logger.info("Not found button clicked")
    time.sleep(3)
    response_text = links_page.verify_response_message()
    links_page.logger.info(f"Response message: {response_text}")
    assert "404 " in response_text and "Not Found" in response_text
    links_page.logger.info("API response verification passed!")
# ------------------------------------------------------------------------------------------------------------------------------


    driver.quit()