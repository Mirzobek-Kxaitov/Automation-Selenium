import pytest
from pages.droppable_page import DroppablePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class TestDroppablePage:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.droppable_page = DroppablePage(self.driver)
        self.driver.get("https://demoqa.com/droppable")

    def test_basic_drag_and_drop(self):
        drag_element = self.droppable_page.wait_for_element_visible(self.droppable_page.DRAG_ME)
        drop_element = self.droppable_page.wait_for_element_visible(self.droppable_page.DROP_HERE)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
        self.droppable_page.drag_and_drop(self.droppable_page.DRAG_ME, self.droppable_page.DROP_HERE)
        assert self.droppable_page.wait_for_text_in_element(self.droppable_page.DROPPED_TEXT, "Dropped!"), \
            "Element tashlangandan keyin matn 'Dropped!' ga o'zgarmadi."

    #
    # def test_accept_tab_acceptable(self):
    #     """'Accept' tabida ruxsat etilgan elementni tashlash"""
    #     self.droppable_page.switch_to_tab(self.droppable_page.TAB_ACCEPT)
    #     self.droppable_page.drag_and_drop(self.droppable_page.ACCEPTABLE, self.droppable_page.DROP_HERE_ACCEPT)
    #     assert self.droppable_page.wait_for_text_in_element(
    #         self.droppable_page.DROP_HERE_ACCEPT, "Dropped!"
    #     ), "'Acceptable' elementi tashlanganda matn 'Dropped!' ga o'zgarmadi."
    #
    #
    # def test_accept_tab_not_acceptable(self):
    #     self.droppable_page.switch_to_tab(self.droppable_page.TAB_ACCEPT)
    #     self.droppable_page.drag_and_drop(self.droppable_page.NOT_ACCEPTABLE, self.droppable_page.DROP_HERE_ACCEPT)
    #     text = self.droppable_page.get_drop_text(self.droppable_page.DROP_HERE_ACCEPT)
    #     assert text == "Drop here", "'Not Acceptable' elementini tashlaganda matn o'zgarib ketdi."
    #
    #
    #
    # def test_revert_draggable_behavior(self):
    #     self.droppable_page.switch_to_revert_tab()
    #     will_revert_element = self.droppable_page.wait_for_element_visible(self.droppable_page.WILL_REVERT)
    #     initial_pos = will_revert_element.location
    #     self.droppable_page.drag_and_drop(self.droppable_page.WILL_REVERT, self.droppable_page.DROP_AREA_REVERT)
    #     try:
    #         wait = WebDriverWait(self.driver, 10)  # 10 soniyagacha kutish
    #         wait.until(
    #             lambda driver: driver.find_element(*self.droppable_page.WILL_REVERT).location == initial_pos
    #         )
    #     except TimeoutException:
    #         # Agar 10 soniyada qaytmasa, testni xatolik bilan yakunlash
    #         pytest.fail("'Will Revert' elementi 10 soniya ichida o'z joyiga qaytmadi.")
    #
    # def test_revert_not_revertable_behavior(self):
    #     """'Not Revert' elementining tashlangan joyida qolishini tekshiradi."""
    #     self.droppable_page.switch_to_revert_tab()
    #     not_revert_element = self.droppable_page.wait_for_element_visible(self.droppable_page.NOT_REVERT)
    #     initial_pos = not_revert_element.location
    #     self.droppable_page.drag_and_drop(self.droppable_page.NOT_REVERT, self.droppable_page.DROP_AREA_REVERT)
    #     final_pos = self.droppable_page.wait_for_element_visible(self.droppable_page.NOT_REVERT).location
    #     assert initial_pos != final_pos, "'Not Revert' elementi joyidan siljimadi."
    #
    # def test_prevent_propagation_not_greedy_inner(self):
    #     """'Not Greedy' rejimida ichki qutiga tashlaganda, ikkala qutining matni ham o'zgarishini tekshiradi."""
    #     self.droppable_page.switch_to_prevent_prop_tab()
    #     self.droppable_page.drag_and_drop(self.droppable_page.PP_DRAG_BOX, self.droppable_page.INNER_DROPPABLE)
    #     outer_text = self.droppable_page.get_drop_text(self.droppable_page.OUTER_TEXT)
    #     inner_text = self.droppable_page.get_drop_text(self.droppable_page.INNER_TEXT)
    #     assert inner_text == "Dropped!", "'Not Greedy'da ichki matn o'zgarmadi."
    #     assert outer_text == "Dropped!", "'Not Greedy'da tashqi matn ham o'zgarishi kerak edi."
    #
    #
    #
    # def test_prevent_propagation_greedy(self):
    #     self.droppable_page.switch_to_prevent_prop_tab()
    #     self.droppable_page.drag_and_drop(self.droppable_page.PP_DRAG_BOX, self.droppable_page.GREEDY_INNER_DROPPABLE)
    #     outer_text = self.droppable_page.get_drop_text(self.droppable_page.GREEDY_OUTER_TEXT)
    #     inner_text = self.droppable_page.get_drop_text(self.droppable_page.GREEDY_INNER_TEXT)
    #     assert inner_text == "Dropped!", "Greedy ichki elementga tashlanganda matni o'zgarmadi."
    #     assert outer_text == "Outer droppable", "Greedy ichki elementga tashlanganda tashqi element matni ham o'zgarib ketdi."
    #
    # #
    #
    # def test_prevent_propagation_greedy_outer(self):
    #     """'Greedy' rejimida faqat tashqi qutiga tashlaganda, faqat tashqi quti matni o'zgarishini tekshiradi."""
    #     self.droppable_page.switch_to_prevent_prop_tab()
    #     self.droppable_page.drag_and_drop(self.droppable_page.PP_DRAG_BOX, self.droppable_page.GREEDY_OUTER_DROPPABLE)
    #     outer_text = self.droppable_page.get_drop_text(self.droppable_page.GREEDY_OUTER_TEXT)
    #     inner_text = self.droppable_page.get_drop_text(self.droppable_page.GREEDY_INNER_TEXT)
    #     # assert outer_text == "Inner droppable (greedy)", "'Greedy'da tashqi matn o'zgarmadi."
    #     # assert inner_text == "Dropped!", "Tashqi qutiga tashlaganda ichki matn o'zgarmasligi kerak edi."
    #     #
    #
    #
    #






















# def test_basic_drag_and_drop_with_explicit_wait(droppable_page):
#     wait = WebDriverWait(droppable_page.driver, 10)
#     drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
#     droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
#     drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
#     time.sleep(1)
#     droppable_page.drag_and_drop(droppable_page.DRAG_ME, droppable_page.DROP_HERE)
#     text = droppable_page.get_drop_text(droppable_page.DROPPED_TEXT)
#     assert text == "Dropped!"
#
# def test_invalid_drop_attempt(droppable_page):
#     wait = WebDriverWait(droppable_page.driver, 10)
#     drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
#     droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
#     drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
#     time.sleep(1)
#
#     drag = droppable_page.wait_for_element_visible(droppable_page.DRAG_ME)
#     actions = ActionChains(droppable_page.driver)
#     actions.click_and_hold(drag).move_by_offset(300,0).release().perform()
#     text = droppable_page.get_drop_text(droppable_page.DROPPED_TEXT)
#     assert text == "Dropped!"
#
# def test_accept_tab_acceptable(droppable_page):
#     wait = WebDriverWait(droppable_page.driver, 10)
#     drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
#     droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
#     drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
#     time.sleep(1)
#
#
#     droppable_page.switch_to_tab(droppable_page.TAB_ACCEPT)
#     droppable_page.drag_and_drop(droppable_page.ACCEPTABLE, droppable_page.DROP_HERE_ACCEPT)
#     t = droppable_page.get_drop_text(droppable_page.DROP_HERE_ACCEPT)
#     assert t == "Dropped!"
#
# def test_accept_tab_not_acceptable(droppable_page):
#     wait = WebDriverWait(droppable_page.driver, 10)
#     drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
#     droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
#     drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
#     time.sleep(1)
#
#
#     droppable_page.switch_to_tab(droppable_page.TAB_ACCEPT)
#     droppable_page.drag_and_drop(droppable_page.NOT_ACCEPTABLE, droppable_page.DROP_HERE_ACCEPT)
#     t = droppable_page.get_drop_text(droppable_page.DROP_HERE_ACCEPT)
#     assert t == "Drop here"
#
# def test_revert_draggable(droppable_page):
#     wait = WebDriverWait(droppable_page.driver, 10)
#     drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
#     droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
#     drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
#     time.sleep(1)
#     droppable_page.switch_to_revert_tab()
#     # Will Revert-ni drop
#     droppable_page.drag_and_drop(droppable_page.WILL_REVERT, droppable_page.DROP_AREA_REVERT)
#     elem = droppable_page.wait_for_element_visible(droppable_page.WILL_REVERT)
#     pos_after = elem.location
#     time.sleep(1)
#     pos_final = elem.location
#     assert pos_after != pos_final
#     #
#     # Not Revert-ni drop
#     droppable_page.drag_and_drop(droppable_page.NOT_REVERT, droppable_page.DROP_AREA_REVERT)
#     elem2 = droppable_page.wait_for_element_visible(droppable_page.NOT_REVERT)
#     pos2_after = elem2.location
#     time.sleep(1)
#     pos2_final = elem2.location
#     assert pos2_after == pos2_final
#
#
# # INNER ga drop qilinsa:
# def test_prevent_propagation_inner_and_outer(droppable_page):
#     wait = WebDriverWait(droppable_page.driver, 10)
#     drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
#     droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
#     drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
#     time.sleep(1)
#
#
#     droppable_page.switch_to_prevent_prop_tab()
#     droppable_page.drag_and_drop(droppable_page.PP_DRAG_BOX, droppable_page.INNER_DROPPABLE)
#     text_outer = droppable_page.get_drop_text(droppable_page.OUTER_TEXT)
#     text_inner = droppable_page.get_drop_text(droppable_page.INNER_TEXT)
#     assert text_outer == "Dropped!"
#     assert text_inner == "Dropped!"
#
# def test_prevent_propagation_greedy_inner_and_outer(droppable_page):
#     wait = WebDriverWait(droppable_page.driver, 10)
#     drag_element = wait.until(EC.element_to_be_clickable(droppable_page.DRAG_ME))
#     droppable_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
#     drop_element = wait.until(EC.element_to_be_clickable(droppable_page.DROP_HERE))
#     time.sleep(1)
#
#
#     droppable_page.switch_to_prevent_prop_tab()
#     droppable_page.drag_and_drop(droppable_page.PP_DRAG_BOX, droppable_page.GREEDY_INNER_DROPPABLE)
#     text_greedy_inner = droppable_page.get_drop_text(droppable_page.GREEDY_INNER_TEXT)
#     text_greedy_outer = droppable_page.get_drop_text(droppable_page.GREEDY_OUTER_TEXT)
#     assert text_greedy_inner == "Inner droppable (greedy)"
#     assert text_greedy_outer == "Outer droppable"
#
