import pytest
from utils.driver import get_driver
from pages.accordian_page import Accordian_page


# --- Pytest fixture'lar ---

@pytest.fixture
def driver():
    driver = get_driver("https://demoqa.com/accordian")
    yield driver
    driver.quit()

@pytest.fixture
def accordian_page(driver):
    return Accordian_page(driver)


# --- TESTLAR ---

def test_first_accordion(accordian_page):
    accordian_page.logger.info("START first accordion")

    accordian_page.click_first_accordion()
    accordian_page.logger.info("First accordion clicked")


    # Verify visible
    assert accordian_page.is_first_content_visible(), "First accordian is not visible!"

    # Verify content text
    content = accordian_page.get_first_content_text()
    assert "Lorem Ipsum" in content, f"Expected 'Lorem Ipsum', got '{content}'"

    # Verify other sections closed
    assert not accordian_page.is_second_content_visible(), "Second accordion should be closed"
    assert not accordian_page.is_third_content_visible(), "Third accordion should be closed"

    accordian_page.logger.info("First accordion test PASSED")


def test_second_accordion(accordian_page):
    accordian_page.logger.info("START second accordion")

    accordian_page.close_other_accordions()  # Boshqa accordionlarni yopish
    accordian_page.click_second_accordion()
    accordian_page.logger.info("Second accordion clicked")

    # Verify visible
    assert accordian_page.is_second_content_visible(), "Second accordian is not visible!"

    content = accordian_page.get_second_content_text()
    assert "Lorem Ipsum" in content, f"Expected 'Lorem Ipsum', got '{content}'"

    # Verify first accordion is closed
    assert not accordian_page.is_first_content_visible(), "First accordion should be closed"

    accordian_page.logger.info("Second accordion test PASSED")


def test_third_accordion(accordian_page):
    accordian_page.logger.info("START third accordion")

    accordian_page.close_other_accordions()  # Boshqa accordionlarni yopish
    accordian_page.click_third_accordion()
    accordian_page.logger.info("Third accordion clicked")

    # Verify visible
    assert accordian_page.is_third_content_visible(), "Third accordian is not visible!"

    content = accordian_page.get_third_content_text()
    assert "Lorem Ipsum" in content, f"Expected 'Lorem Ipsum', got '{content}'"

    # Verify first accordion is closed
    assert not accordian_page.is_first_content_visible(), "First accordion should be closed"

    accordian_page.logger.info("Third accordion test PASSED")

