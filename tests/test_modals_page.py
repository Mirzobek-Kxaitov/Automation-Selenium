import time

from base.base_page import BasePage
from utils.driver import get_driver
from pages.modals_page import Modals_page

# def test_modals_page_functionality():
#     driver = get_driver("https://demoqa.com/modal-dialogs")
#     modals_page = Modals_page(driver)
#
#     modals_page.logger.info("STARTING TEST: test_small_modal_functionality")
#     modals_page.logger.info("Clicking small modal button")
#     modals_page.click_small_modal()
#
#     modals_page.logger.info("Verfying modal is visible...")
#     is_visible = modals_page.is_modal_visible()
#     assert is_visible, "Modal is not visible"
#
#     modals_page.logger.info("Verfying modal title...")
#     title = modals_page.get_modal_title_text()
#     assert "Small Modal" in title, f"Expected 'Small Modal', got '{title}'"
#
#     modals_page.logger.info("Verfying modal content...")
#     content = modals_page.get_modal_body_text()
#     assert "small modal" in content.lower(), f"Expected small modal content, got '{content}'"
#     time.sleep(2)
#     modals_page.logger.info("Closing modal...")
#     modals_page.close_modal()
#     time.sleep(5)
#
#     driver.quit()


def test_large_modal_functionality():
    driver = get_driver("https://demoqa.com/modal-dialogs")
    modals_page = Modals_page(driver)

    modals_page.logger.info("STARTING TEST: test_large_modal_functionality")

    # STEP 1: Large modal button'ni bosish
    modals_page.logger.info("Clicking large modal button...")
    modals_page.click_large_modal()  # ← Bu farq

    # STEP 2: Modal ochilganini tekshirish
    modals_page.logger.info("Verifying modal is visible...")
    is_visible = modals_page.is_modal_visible()
    assert is_visible, "Modal is not visible!"

    # STEP 3: Modal title'ni tekshirish
    modals_page.logger.info("Verifying modal title...")
    title = modals_page.get_modal_title_text()
    assert "Large Modal" in title, f"Expected 'Large Modal', got '{title}'"  # ← Bu farq

    # STEP 4: Modal content'ni tekshirish
    modals_page.logger.info("Verifying modal content...")
    content = modals_page.get_modal_body_text()
    assert "lorem ipsum" in content.lower(), f"Expected large modal content, got '{content}'"  # ← Bu farq
    time.sleep(2)
    # STEP 5: Modal'ni yopish
    modals_page.logger.info("Closing modal...")
    modals_page.close_modal()

    modals_page.logger.info("Test completed successfully!")
    driver.quit()