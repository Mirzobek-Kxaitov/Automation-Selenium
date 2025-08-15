import time
from pages.date_picker_page import DatePickerPage
import pytest

@pytest.fixture
def date_picker_page(driver):
    driver.get("https://demoqa.com/date-picker")
    return DatePickerPage(driver)


def test_date_picker_typing(date_picker_page):
    date_to_type = "07/09/2025"
    date_picker_page.set_date_by_typing(date_to_type)
    input_value = date_picker_page.get_element_attribute("value", date_picker_page.SELECT_DATE)
    assert input_value == date_to_type
    time.sleep(1)

def test_date_picker_calendar(date_picker_page):
    day = "15"
    month = "August"
    year = "2025"
    date_picker_page.set_date_by_calendar(day, month, year)
    input_value = date_picker_page.get_element_attribute("value", date_picker_page.SELECT_DATE)
    expected_value = "08/15/2025"
    assert input_value == expected_value
    time.sleep(1)

#OTHER WAYS TO FILL PAGE:
# import time
# import logging
# from pages.date_picker_page import DatePickerPage
# from utils.driver import get_driver
#
# # Configure logging for tests
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
#     handlers=[
#         logging.FileHandler('logs/test_execution.log'),
#         logging.StreamHandler()
#     ]
# )
#
# logger = logging.getLogger(__name__)
#
#
# def test_date_picker_typing():
#     """Test date picker functionality using direct typing method"""
#     logger.info("=== Starting Date Picker Typing Test ===")
#
#     try:
#         logger.info("Initializing driver and navigating to date picker page")
#         driver = get_driver("https://demoqa.com/date-picker")
#         page_set_date = DatePickerPage(driver)
#
#         logger.info("Testing direct typing method with date: 7/9/2025")
#         page_set_date.set_date_by_typing("7/9/2025")
#
#         logger.info("Date picker typing test completed successfully")
#
#     except Exception as e:
#         logger.error(f"Date picker typing test failed: {str(e)}")
#         raise
#     finally:
#         logger.info("Cleaning up: Closing driver")
#         driver.quit()
#         logger.info("=== Date Picker Typing Test Finished ===\n")
#
#
# def test_date_picker_calendar():
#     """Test date picker functionality using calendar selection method"""
#     logger.info("=== Starting Date Picker Calendar Test ===")
#
#     try:
#         logger.info("Initializing driver and navigating to date picker page")
#         driver = get_driver("https://demoqa.com/date-picker")
#         page_set_date = DatePickerPage(driver)
#
#         logger.info("Testing calendar selection method - Day: 7, Month: May, Year: 2024")
#         page_set_date.set_date_by_calendar(day="7", month="May", year="2024")
#
#         logger.info("Date picker calendar test completed successfully")
#
#     except Exception as e:
#         logger.error(f"Date picker calendar test failed: {str(e)}")
#         raise
#     finally:
#         logger.info("Cleaning up: Closing driver")
#         driver.quit()
#         logger.info("=== Date Picker Calendar Test Finished ===\n")
#
#
# def test_wrapper_methods():
#     """Test date picker functionality using wrapper methods (both typing and calendar)"""
#     logger.info("=== Starting Wrapper Methods Test ===")
#
#     try:
#         logger.info("Initializing driver and navigating to date picker page")
#         driver = get_driver("https://demoqa.com/date-picker")
#         page = DatePickerPage(driver)
#
#         logger.info("Testing wrapper method with typing approach - Date: 08/15/2025")
#         page.set_date("08/15/2025", method="typing")
#
#         logger.info("Testing wrapper method with calendar approach - Day: 15, Month: August, Year: 2025")
#         page.set_date("", method="calendar", day="15", month="August", year="2025")
#
#         logger.info("Wrapper methods test completed successfully")
#
#     except Exception as e:
#         logger.error(f"Wrapper methods test failed: {str(e)}")
#         raise
#     finally:
#         logger.info("Cleaning up: Closing driver")
#         driver.quit()
#         logger.info("=== Wrapper Methods Test Finished ===\n")
#
#
# if __name__ == "__main__":
#     """Run all date picker tests when script is executed directly"""
#     logger.info("Starting Date Picker Test Suite")
#
#     try:
#         test_date_picker_typing()
#         test_date_picker_calendar()
#         test_wrapper_methods()
#         logger.info("All date picker tests completed successfully!")
#
#     except Exception as e:
#         logger.error(f"Test suite execution failed: {str(e)}")
#         raise