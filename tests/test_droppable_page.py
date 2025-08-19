import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from pages.droppable_page import DroppablePage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--headless')  # Istasangiz headless qilib qo‘shing
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://demoqa.com/droppable")
    yield driver
    driver.quit()

@pytest.fixture
def droppable_page(driver):
    return DroppablePage(driver)


def test_basic_drag_and_drop_with_explicit_wait(droppable_page):
    wait = WebDriverWait(droppable_page.driver, 10)
    drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
    droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
    time.sleep(1)
    droppable_page.drag_and_drop(droppable_page.DRAG_ME, droppable_page.DROP_HERE)
    text = droppable_page.get_drop_text(droppable_page.DROPPED_TEXT)
    assert text == "Dropped!"

def test_invalid_drop_attempt(droppable_page):
    wait = WebDriverWait(droppable_page.driver, 10)
    drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
    droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
    time.sleep(1)

    drag = droppable_page.wait_for_element_visible(droppable_page.DRAG_ME)
    actions = ActionChains(droppable_page.driver)
    actions.click_and_hold(drag).move_by_offset(300,0).release().perform()
    text = droppable_page.get_drop_text(droppable_page.DROPPED_TEXT)
    assert text == "Dropped!"

def test_accept_tab_acceptable(droppable_page):
    wait = WebDriverWait(droppable_page.driver, 10)
    drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
    droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
    time.sleep(1)


    droppable_page.switch_to_tab(droppable_page.TAB_ACCEPT)
    droppable_page.drag_and_drop(droppable_page.ACCEPTABLE, droppable_page.DROP_HERE_ACCEPT)
    t = droppable_page.get_drop_text(droppable_page.DROP_HERE_ACCEPT)
    assert t == "Dropped!"

def test_accept_tab_not_acceptable(droppable_page):
    wait = WebDriverWait(droppable_page.driver, 10)
    drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
    droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
    time.sleep(1)


    droppable_page.switch_to_tab(droppable_page.TAB_ACCEPT)
    droppable_page.drag_and_drop(droppable_page.NOT_ACCEPTABLE, droppable_page.DROP_HERE_ACCEPT)
    t = droppable_page.get_drop_text(droppable_page.DROP_HERE_ACCEPT)
    assert t == "Drop here"

def test_revert_draggable(droppable_page):
    wait = WebDriverWait(droppable_page.driver, 10)
    drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
    droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
    time.sleep(1)
    droppable_page.switch_to_revert_tab()
    # Will Revert-ni drop
    droppable_page.drag_and_drop(droppable_page.WILL_REVERT, droppable_page.DROP_AREA_REVERT)
    elem = droppable_page.wait_for_element_visible(droppable_page.WILL_REVERT)
    pos_after = elem.location
    time.sleep(1)
    pos_final = elem.location
    assert pos_after != pos_final
    #
    # Not Revert-ni drop
    droppable_page.drag_and_drop(droppable_page.NOT_REVERT, droppable_page.DROP_AREA_REVERT)
    elem2 = droppable_page.wait_for_element_visible(droppable_page.NOT_REVERT)
    pos2_after = elem2.location
    time.sleep(1)
    pos2_final = elem2.location
    assert pos2_after == pos2_final


# INNER ga drop qilinsa:
def test_prevent_propagation_inner_and_outer(droppable_page):
    wait = WebDriverWait(droppable_page.driver, 10)
    drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
    droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
    time.sleep(1)


    droppable_page.switch_to_prevent_prop_tab()
    droppable_page.drag_and_drop(droppable_page.PP_DRAG_BOX, droppable_page.INNER_DROPPABLE)
    text_outer = droppable_page.get_drop_text(droppable_page.OUTER_TEXT)
    text_inner = droppable_page.get_drop_text(droppable_page.INNER_TEXT)
    assert text_outer == "Dropped!"
    assert text_inner == "Dropped!"

def test_prevent_propagation_greedy_inner_and_outer(droppable_page):
    wait = WebDriverWait(droppable_page.driver, 10)
    drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
    droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
    time.sleep(1)


    droppable_page.switch_to_prevent_prop_tab()
    droppable_page.drag_and_drop(droppable_page.PP_DRAG_BOX, droppable_page.GREEDY_INNER_DROPPABLE)
    text_greedy_inner = droppable_page.get_drop_text(droppable_page.GREEDY_INNER_TEXT)
    text_greedy_outer = droppable_page.get_drop_text(droppable_page.GREEDY_OUTER_TEXT)
    assert text_greedy_inner == "Inner droppable (greedy)"
    assert text_greedy_outer == "Outer droppable"

