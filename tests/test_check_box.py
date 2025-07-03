from base.base_page import BasePage
from pages.check_box import Check_box_page
from utils.driver import get_driver

def test_check_box():
    driver = get_driver("https://demoqa.com/checkbox")
    base_page =BasePage(driver)
    check_box_page = Check_box_page(driver)

    check_box_page.click_check_box()
    check_box_page.click_check_box_d_b()
    check_box_page.click_check_box_doc_button()
    check_box_page.click_check_box_download_button()
    check_box_page.click_button_one()
    check_box_page.click_button_two()
    check_box_page.click_button_three()
