from pages.menu_page import Menu_Page
from utils.driver import get_driver
from selenium.webdriver.common.by import By
import pytest
import time



@pytest.fixture()
def setup():
    driver = get_driver("https://demoqa.com/menu")
    page = Menu_Page(driver)
    yield page
    driver.quit()

def test_menu_items_display(setup):
    page = setup
    assert page.wait_for_element_visible(page.MAIN_ITEM_1)
    assert page.wait_for_element_visible(page.MAIN_ITEM_2)
    assert page.wait_for_element_visible(page.MAIN_ITEM_3)

def test_hover_effects(setup):
    page = setup

    page.hover_main_item_one()
    page.hover_main_item_two()
    page.hover_main_item_three()

    assert True

def test_submenu_appears_on_hover(setup):
    page = setup
    page.hover_main_item_two()
    assert page.is_submenu_visible()

def test_submenu_items_clickable(setup):
    page = setup
    page.hover_main_item_two()
    page.wait_for_submenu_to_appear()
    page.hover_sub_item_one()
    page.hover_sub_sub_list()
    assert page.is_nested_submenu_visible()

def test_menu_timing_behavior(setup):
    page = setup
    start_time = time.time()
    page.hover_main_item_two()
    page.wait_for_submenu_to_appear()
    end_time = time.time()

    assert (end_time - start_time) < 2.0