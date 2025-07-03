from base.base_page import BasePage
from pages.text_box import TexBoxPage
from utils.driver import get_driver


def test_text_box():
    driver = get_driver("https://demoqa.com/text-box")
    base_page = BasePage(driver)
    text_box_page = TexBoxPage(driver)

    user_name = "Mirzobek"
    user_email = "mirzobek@gmail.com"
    current_address = "Tashkent"
    permanent_address = "Denau"

    text_box_page.enter_user_name(user_name)
    base_page.logger.info("user_name kiritildi")

    text_box_page.enter_user_email(user_email)
    base_page.logger.info("user_email kiritildi")

    text_box_page.enter_current_address(current_address)
    base_page.logger.info("current_address kiritildi")

    text_box_page.enter_permanent_address(permanent_address)
    base_page.logger.info("permanent_address kiritildi")

    text_box_page.click_submit_button()


    assert user_name in text_box_page.get_output_name()
    assert user_email in text_box_page.get_output_email()
    assert current_address in text_box_page.get_output_current_address()
    assert permanent_address in text_box_page.get_output_permanent_address()

    base_page._take_screenshot()


    driver.quit()
