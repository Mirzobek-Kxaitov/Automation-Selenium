from base.base_page import BasePage
from utils.driver import get_driver
from pages.nested_frames_page import Nested_frames_page

def test_switch_to_parent_frame():
    driver = get_driver("https://demoqa.com/nestedframes")
    nested_pages = Nested_frames_page(driver)

    nested_pages.logger.info("STARTING TEST: test_switch_to_parent_frame")
    nested_pages.switch_to_parent_frame()

    try:
        content = nested_pages.get_frame_content_text()
        nested_pages.logger.info(f"Found content: {content}")
    except:
        nested_pages.logger.error("Element not found in parent frame")

    driver.quit()


def test_switch_to_child_frame():
    driver = get_driver("https://demoqa.com/nestedframes")
    nested_pages = Nested_frames_page(driver)

    nested_pages.logger.info("STARTING TEST: test_switch_to_parent_frame")
    nested_pages.switch_to_parent_frame()

    nested_pages.switch_to_child_frame()
    nested_pages.logger.info("Switched to child frame")

    try:
        content = nested_pages.get_frame_content_text()
        nested_pages.logger.info(f"Found child content {content}")
    except:
        nested_pages.logger.error("Element not found in child frame")
    driver.quit()