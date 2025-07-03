import time

from base.base_page import BasePage
from pages.radiobutton_page import Radiobutton_page
from utils.driver import get_driver

def test_radiobutton():
    driver = get_driver("https://demoqa.com/radio-button")
    base_page =BasePage(driver)
    radio_button_page = Radiobutton_page(driver)

    radio_button_page.click_radiobutton()
    radio_button_page.click_radiobutton_imp()
    radio_button_page.is_radiobutton_no_disabled()
    time.sleep(5)