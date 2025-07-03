from utils.driver import get_driver
from base.base_page import BasePage
import time
from pages.accordian_page import Accordian_page

def test_first_accordion():
    driver = get_driver("https://demoqa.com/accordian")
    accordian_page_test = Accordian_page(driver)
    accordian_page_test.logger.info("START first accordion")
    accordian_page_test.click_first_accordion()
    accordian_page_test.logger.info("first accordion is clicked")
    accordian_page_test.click_first_accordion()


    accordian_page_test.logger.info("Verifying accordion is visible...")
    is_visible = accordian_page_test.is_first_content_visible()
    assert is_visible, "Accordian is not visible!"

    accordian_page_test.logger.info("Verfying accordion title")
    content = accordian_page_test.get_first_content_text()
    assert "Lorem Ipsum" in content, f"Expected 'Lorem Ipsum' got '{content}'"

    # Boshqa accordion'lar yopiq ekanligini tekshirish:
    accordian_page_test.logger.info("Verifying other sections are closed")
    assert not accordian_page_test.is_second_content_visible(), "Second accordion should be closed"
    assert not accordian_page_test.is_third_content_visible(), "Third accordion should be closed"

    accordian_page_test.logger.info("Test completed successfully!")
    driver.quit()

def test_second_accordion():
    driver = get_driver("https://demoqa.com/accordian")
    accordian_page_test = Accordian_page(driver)
    accordian_page_test.logger.info("START second accordion")
    accordian_page_test.click_second_accordion()
    accordian_page_test.logger.info("second accordion is clicked")
    time.sleep(2)



    accordian_page_test.logger.info("Verifying second accordion is visible...")
    is_visible = accordian_page_test.is_second_content_visible()
    assert is_visible, "Accordian is not visible!"

    accordian_page_test.logger.info("Verfying accordion title")
    content = accordian_page_test.get_second_content_text()
    assert "Lorem Ipsum" in content, f"Expected 'Lorem Ipsum' got '{content}'"

    # Boshqa accordion'lar yopiq ekanligini tekshirish:
    accordian_page_test.logger.info("Verifying other sections are closed")
    assert not accordian_page_test.is_first_content_visible(), "First accordion should be closed"
    assert not accordian_page_test.is_third_content_visible(), "Third accordion should be closed"

    accordian_page_test.logger.info("Test completed successfully!")
    driver.quit()

def test_third_accordion():
    driver = get_driver("https://demoqa.com/accordian")
    accordian_page_test = Accordian_page(driver)
    accordian_page_test.logger.info("START third accordion")
    accordian_page_test.click_third_accordion()
    accordian_page_test.logger.info("Third accordion is clicked")
    time.sleep(2)



    accordian_page_test.logger.info("Verifying third accordion is visible...")
    is_visible = accordian_page_test.is_third_content_visible()
    assert is_visible, "Accordian is not visible!"

    accordian_page_test.logger.info("Verfying accordion title")
    content = accordian_page_test.get_third_content_text()
    assert "Lorem Ipsum" in content, f"Expected 'Lorem Ipsum' got '{content}'"

    # Boshqa accordion'lar yopiq ekanligini tekshirish:
    accordian_page_test.logger.info("Verifying other sections are closed")
    assert not accordian_page_test.is_first_content_visible(), "First accordion should be closed"
    assert not accordian_page_test.is_second_content_visible(), "Second accordion should be closed"

    accordian_page_test.logger.info("Test completed successfully!")
    driver.quit()

