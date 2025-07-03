from base.base_page import BasePage
from pages.web_tables_page import Web_tables_page
from utils.driver import get_driver
import time


def test_search_text():
    driver = get_driver("https://demoqa.com/webtables")
    base_page = BasePage(driver)
    web_tables_page = Web_tables_page(driver)
    web_tables_page.search_in_table("Alden")
    time.sleep(3)
    web_tables_page.verify_search_result(search_text="Alden")
    time.sleep(3)# keyword argument
    driver.quit()

def test_add_new_record():
    driver = get_driver("https://demoqa.com/webtables")
    base_page =BasePage(driver)
    web_tables_page = Web_tables_page(driver)

    web_tables_page.click_add_button()
    web_tables_page.fill_first_name("Ahmad")
    web_tables_page.fill_last_name("Ahmadov")
    web_tables_page.fill_email("Ahmadov_ahmad@gmail.com")
    web_tables_page.fill_age("40")
    web_tables_page.fill_salary("2000")
    web_tables_page.fill_department("Toshkent filiali")
    web_tables_page.click_submit_button()
    web_tables_page.verify_record_added("Ahmad", "Ahmadov")
    driver.quit()

def test_edit_record():
    driver = get_driver("https://demoqa.com/webtables")
    base_page =BasePage(driver)
    web_tables_page = Web_tables_page(driver)

    web_tables_page.click_edit_button()
    web_tables_page.fill_first_name("Ahmad")
    web_tables_page.fill_last_name("Ahmadov")
    web_tables_page.fill_email("Ahmadov_ahmad@gmail.com")
    web_tables_page.fill_age("40")
    web_tables_page.fill_salary("2000")
    web_tables_page.click_submit_button()
    web_tables_page.verify_record_added("Ahmad", "Ahmadov")
    web_tables_page.verify_record_edited("Ahmad", "Ahmadov")
    time.sleep(5)
    driver.quit()


def test_delete_button():
    driver = get_driver("https://demoqa.com/webtables")
    base_page = BasePage(driver)
    web_tables_page = Web_tables_page(driver)
    web_tables_page.click_delete_button()
    web_tables_page.verify_record_deleted("Kierra")
    time.sleep(5)
    driver.quit()