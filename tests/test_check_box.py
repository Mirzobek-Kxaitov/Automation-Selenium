from base.base_page import BasePage
from pages.check_box import Check_box_page
import time


def test_select_home_checkbox(driver):
    """
    'Home' checkboxini tanlash va natijani tekshirish testi.
    'Home' ni tanlash barcha ichki elementlarni ham tanlaydi.
    """
    driver.get("https://demoqa.com/checkbox")
    check_box_page = Check_box_page(driver)

    # 'Home' checkboxini tanlash
    check_box_page.select_checkbox("home")

    # Natija matnini olish va tekshirish
    result_text = check_box_page.get_selected_items_text()

    assert "home" in result_text
    assert "desktop" in result_text
    assert "documents" in result_text
    assert "downloads" in result_text

    time.sleep(1)


def test_select_desktop_checkbox(driver):
    """
    'Desktop' checkboxini tanlash va natijani tekshirish testi.
    Buning uchun avval papka ochilishi kerak.
    """
    driver.get("https://demoqa.com/checkbox")
    check_box_page = Check_box_page(driver)

    # 'Home' papkasini ochish
    check_box_page.click(check_box_page.main_toggle_button)

    # 'Desktop' checkboxini tanlash
    check_box_page.select_checkbox("desktop")

    # Natija matnini olish va tekshirish
    result_text = check_box_page.get_selected_items_text()

    assert "desktop" in result_text
    assert "notes" in result_text
    assert "commands" in result_text
    assert "documents" not in result_text  # Bu element tanlanmaganini tekshiramiz

    time.sleep(1)


def test_select_documents_checkbox(driver):
    """
    'Documents' checkboxini tanlash va natijani tekshirish testi.
    """
    driver.get("https://demoqa.com/checkbox")
    check_box_page = Check_box_page(driver)

    # 'Home' papkasini ochish
    check_box_page.click(check_box_page.main_toggle_button)

    # 'Documents' checkboxini tanlash
    check_box_page.select_checkbox("documents")

    # Natija matnini olish va tekshirish
    result_text = check_box_page.get_selected_items_text()

    assert "documents" in result_text
    assert "workspace" in result_text
    assert "react" in result_text
    assert "desktop" not in result_text  # Bu element tanlanmaganini tekshiramiz

    time.sleep(1)


def test_select_downloads_checkbox(driver):
    """
    'Downloads' checkboxini tanlash va natijani tekshirish testi.
    """
    driver.get("https://demoqa.com/checkbox")
    check_box_page = Check_box_page(driver)

    # 'Home' papkasini ochish
    check_box_page.click(check_box_page.main_toggle_button)

    # 'Downloads' checkboxini tanlash
    check_box_page.select_checkbox("downloads")

    # Natija matnini olish va tekshirish
    result_text = check_box_page.get_selected_items_text()

    assert "downloads" in result_text
    assert "wordFile" in result_text
    assert "excelFile" in result_text
    assert "documents" not in result_text  # Bu element tanlanmaganini tekshiramiz

    time.sleep(1)


#OTHER WAYS - CLICK EVERYTHING
#from base.base_page import BasePage
# from pages.check_box import Check_box_page
# from utils.driver import get_driver
#
# def test_check_box():
#     driver = get_driver("https://demoqa.com/checkbox")
#     base_page =BasePage(driver)
#     check_box_page = Check_box_page(driver)
#
#     check_box_page.click_check_box()
#     check_box_page.click_check_box_d_b()
#     check_box_page.click_check_box_doc_button()
#     check_box_page.click_check_box_download_button()
#     check_box_page.click_button_one()
#     check_box_page.click_button_two()
#     check_box_page.click_button_three()