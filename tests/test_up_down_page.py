from base.base_page import BasePage
from pages.up_down_page import Up_Down_page
from utils.driver import get_driver
import time


def test_download_button():
    driver = get_driver("https://demoqa.com/upload-download")
    up_down_page = Up_Down_page(driver)
    assert up_down_page.click_download_button()
    time.sleep(2)
    driver.quit()
# ------------------------------------------------------------------------------------------------------------------------------
def test_upload_file_to_page():
    driver = get_driver("https://demoqa.com/upload-download")#1. Browser ochish va upload-download sahifasiga borish
    up_down_page = Up_Down_page(driver)#2. Up_Down_page obyektini yaratish (locatorlar va methodlar bilan)
    file_path = r'C:\Users\user\Desktop\photo_2025-04-26_12-18-38.jpg'
    assert up_down_page.upload_file(up_down_page.upload_file_input, file_path)
    #                    ↑              ↑
    #               Method nomi     Locator nomi
    # BU XATO! Ikkalasi ham "upload_file" deb nomlangan

    assert up_down_page.verify_file_uploaded("photo_2025-04-26_12-18-38.jpg")
    time.sleep(2)
    driver.quit()
