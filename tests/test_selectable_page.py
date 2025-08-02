from pages.selectable_page import Selectable_Page
from utils.driver import get_driver
import pytest
import time

@pytest.fixture()
def setup():
    driver = get_driver("https://demoqa.com/selectable")
    page = Selectable_Page(driver)
    yield page
    driver.quit()

# def test_click_vertical_list_1(setup):
#     page = setup
#     page.click_vertical_list(1)
#     assert page.is_vertical_item_selected(1)
#
# def test_click_vertical_list_2(setup):
#     page = setup
#     page.click_vertical_list(2)
#     assert page.is_vertical_item_selected(2)
#
# def test_click_vertical_list_3(setup):
#     page = setup
#     page.click_vertical_list(3)
#     assert page.is_vertical_item_selected(3)
#
# def test_click_vertical_list_4(setup):
#     page = setup
#     page.click_vertical_list(4)
#     assert page.is_vertical_item_selected(4)

def test_click_grid_one(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_ONE)
    assert page.is_grid_item_selected(1, 1)

def test_click_grid_two(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_TWO)
    assert page.is_grid_item_selected(1, 2)

def test_click_grid_three(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_THREE)
    assert page.is_grid_item_selected(1, 3)

def test_click_grid_four(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_FOUR)
    assert page.is_grid_item_selected(2, 1)

def test_click_grid_five(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_FIVE)
    assert page.is_grid_item_selected(2, 2)

def test_click_grid_six(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_SIX)
    assert page.is_grid_item_selected(2, 3)

def test_click_grid_seven(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_SEVEN)
    assert page.is_grid_item_selected(3, 1)

def test_click_grid_eight(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_EIGHT)
    assert page.is_grid_item_selected(3, 2)

def test_click_grid_nine(setup):
    page = setup
    page.click_grid_button()
    page.click(page.SELECT_NINE)
    assert page.is_grid_item_selected(3, 3)
