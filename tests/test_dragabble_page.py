import pytest
from pages.dragabble_page import DragabblePage
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils.driver import get_driver


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--headless')  # Istasangiz headless qilib qo‘shing
    driver = webdriver.Chrome(options=options)
    driver.get("https://demoqa.com/dragabble")
    yield driver
    driver.quit()

@pytest.fixture
def dragabble_page(driver):
    return DragabblePage(driver)

def test_basic_drag_operation(dragabble_page):
    """Basic Drag: Element 100px o‘ngga suriladi"""
    start = dragabble_page.get_location(dragabble_page.DRAG_BASIC)
    dragabble_page.drag_by_offset(dragabble_page.DRAG_BASIC, 100, 0)
    end = dragabble_page.get_location(dragabble_page.DRAG_BASIC)
    assert end['x'] - start['x'] > 80  # 100px dan kichik siljishi mumkin, browserga bog‘liq

def test_axis_restricted_x(dragabble_page):
    """Axis Restricted: Only X bo‘yicha harakat"""
    dragabble_page.switch_to_tab(dragabble_page.TAB_AXIS)
    start = dragabble_page.get_location(dragabble_page.AXIS_X)
    dragabble_page.drag_by_offset(dragabble_page.AXIS_X, 100, 100)
    end = dragabble_page.get_location(dragabble_page.AXIS_X)
    assert end['y'] == start['y']
    assert end['x'] - start['x'] > 50

def test_axis_restricted_y(dragabble_page):
    """Axis Restricted: Only Y bo‘yicha harakat"""
    dragabble_page.switch_to_tab(dragabble_page.TAB_AXIS)
    start = dragabble_page.get_location(dragabble_page.AXIS_Y)
    dragabble_page.drag_by_offset(dragabble_page.AXIS_Y, 100, 100)
    end = dragabble_page.get_location(dragabble_page.AXIS_Y)
    assert end['x'] == start['x']
    assert end['y'] - start['y'] > 50

def test_container_restricted_drag(dragabble_page):
    """Container Restricted: Box konteynerdan chiqmaydi"""
    dragabble_page.switch_to_tab(dragabble_page.TAB_CONTAINER)
    start = dragabble_page.get_location(dragabble_page.BOX_PARENT)
    dragabble_page.drag_by_offset(dragabble_page.BOX_PARENT, 300, 0)
    end = dragabble_page.get_location(dragabble_page.BOX_PARENT)
    # Box konteynerdan tashqariga chiqmasligi kerak, mustaqil siljimaydi (farq 200 px dan katta emas)
    assert end['x'] - start['x'] < 210

def test_cursor_style_center(dragabble_page):
    """Cursor Style: Center"""
    dragabble_page.switch_to_tab(dragabble_page.TAB_CURSOR)
    start = dragabble_page.get_location(dragabble_page.DRAG_CENTER)
    dragabble_page.drag_by_offset(dragabble_page.DRAG_CENTER, 50, 0)
    end = dragabble_page.get_location(dragabble_page.DRAG_CENTER)
    assert end['x'] - start['x'] > 30

def test_drag_to_negative_coordinates(dragabble_page):
    """Elementni manfiy koordinatalarga surish"""
    start = dragabble_page.get_location(dragabble_page.DRAG_BASIC)
    dragabble_page.drag_by_offset(dragabble_page.DRAG_BASIC, -200, -200)
    end = dragabble_page.get_location(dragabble_page.DRAG_BASIC)
    # Element sahifa chegarasidan chiqmasligi kerak
    assert end['x'] >= 0 and end['y'] >= 0

def test_drag_zero_offset(dragabble_page):
    """0 offset bilan drag qilish"""
    start = dragabble_page.get_location(dragabble_page.DRAG_BASIC)
    dragabble_page.drag_by_offset(dragabble_page.DRAG_BASIC, 0, 0)
    end = dragabble_page.get_location(dragabble_page.DRAG_BASIC)
    assert start == end

def test_container_boundary_all_directions(dragabble_page):
    """Container chegaralarini barcha yo'nalishlarda tekshirish"""
    dragabble_page.switch_to_tab(dragabble_page.TAB_CONTAINER)

    # Yuqoriga
    start = dragabble_page.get_location(dragabble_page.BOX_CONTAINER)
    dragabble_page.drag_by_offset(dragabble_page.BOX_CONTAINER, 0, -300)
    end = dragabble_page.get_location(dragabble_page.BOX_CONTAINER)
    assert abs(end['y'] - start['y']) < 150  # Container ichida qolishi kerak

def test_multiple_rapid_drags(dragabble_page):
    for i in range(5):
        dragabble_page.drag_by_offset(dragabble_page.DRAG_BASIC, 20, 0)
        time.sleep(0.1)

