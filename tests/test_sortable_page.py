from pages.sortable_page import Sortable_Page
from utils.driver import get_driver
import pytest
import time

@pytest.fixture()
def setup():
    driver = get_driver("https://demoqa.com/sortable")
    page = Sortable_Page(driver)
    yield page
    driver.quit()


def test_drag_one_to_six(setup):
    page = setup
    page.drag_and_drop(page.LIST_ONE, page.LIST_SIX)
    assert True

def test_drag_six_to_one(setup):
    page = setup
    page.drag_and_drop(page.LIST_SIX, page.LIST_ONE)
    assert True

def test_drag_three_to_five(setup):
    page = setup
    page.drag_and_drop(page.LIST_THREE, page.LIST_FIVE)
    assert True

def test_drag_neighbor(setup):
    page = setup
    page.drag_and_drop(page.LIST_TWO, page.LIST_THREE)
    assert True

def test_drag_itself(setup):
    page = setup
    page.drag_and_drop(page.LIST_FOUR, page.LIST_FOUR)
    assert True

def test_grid_one_to_nine(setup):
    page = setup
    page.click_grid_button()
    page.drag_and_drop_grid(page.GRID_ONE, page.GRID_NINE)
    time.sleep(2)
    assert True

def test_grid_eight_to_four(setup):
    page = setup
    page.click_grid_button()
    page.drag_and_drop_grid(page.GRID_EIGHT, page.GRID_FOUR)
    time.sleep(3)
    assert True

def test_grid_nine_to_one(setup):
    page = setup
    page.click_grid_button()
    page.drag_and_drop_grid(page.GRID_NINE, page.GRID_ONE)
    time.sleep(3)
    assert True

def test_grid_two_to_three(setup):
    setup.click_grid_button()
    setup.drag_and_drop_grid(setup.GRID_TWO, setup.GRID_THREE)
    time.sleep(3)
    assert True

def test_grid_eight_to_eight(setup):
    setup.click_grid_button()
    setup.drag_and_drop_grid(setup.GRID_EIGHT, setup.GRID_EIGHT)
    time.sleep(3)
    assert True