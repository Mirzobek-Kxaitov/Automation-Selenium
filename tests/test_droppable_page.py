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

    # def test_basic_drag_and_drop(self):
    #     drag_element = self.droppable_page.wait_for_element_visible(self.droppable_page.DRAG_ME)
    #     drop_element = self.droppable_page.wait_for_element_visible(self.droppable_page.DROP_HERE)
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    #     self.droppable_page.drag_and_drop(self.droppable_page.DRAG_ME, self.droppable_page.DROP_HERE)
    #     assert self.droppable_page.wait_for_text_in_element(self.droppable_page.DROPPED_TEXT, "Dropped!"), \
    #         "Element tashlangandan keyin matn 'Dropped!' ga o'zgarmadi."

    # def test_accept_tab_acceptable(self):
    #     """'Accept' tabida ruxsat etilgan elementni tashlash"""
    #     self.droppable_page.switch_to_tab(self.droppable_page.TAB_ACCEPT)
    #     # Ensure elements are visible and interactable
    #     drag_element = self.droppable_page.wait_for_element_visible(self.droppable_page.ACCEPTABLE)
    #     drop_element = self.droppable_page.wait_for_element_visible(self.droppable_page.DROP_HERE_ACCEPT)
    #     # Scroll to drag element to ensure visibility
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    #     try:
    #         self.droppable_page.drag_and_drop(self.droppable_page.ACCEPTABLE, self.droppable_page.DROP_HERE_ACCEPT)
    #     except Exception as e:
    #         print(f"ActionChains failed: {e}. Falling back to JavaScript drag-and-drop.")
    #         self.droppable_page.drag_and_drop_js(self.droppable_page.ACCEPTABLE, self.droppable_page.DROP_HERE_ACCEPT)
    #     assert self.droppable_page.wait_for_text_in_element(
    #         self.droppable_page.DROP_HERE_ACCEPT, "Dropped!"
    #     ), "'Acceptable' elementi tashlanganda matn 'Dropped!' ga o'zgarmadi."
    #
    # #
    # def test_accept_tab_not_acceptable(self):
    #     self.droppable_page.switch_to_tab(self.droppable_page.TAB_ACCEPT)
    #     drag_element = self.droppable_page.wait_for_element_visible(self.droppable_page.NOT_ACCEPTABLE)
    #     drop_element = self.droppable_page.wait_for_element_visible(self.droppable_page.DROP_HERE_ACCEPT)
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
    #     try:
    #         self.droppable_page.drag_and_drop(self.droppable_page.NOT_ACCEPTABLE, self.droppable_page.DROP_HERE_ACCEPT)
    #     except Exception as e:
    #         print(f"ActionChains failed: {e}. Falling back to JavaScript drag-and-drop.")
    #         self.droppable_page.drag_and_drop_js(self.droppable_page.NOT_ACCEPTABLE, self.droppable_page.DROP_HERE_ACCEPT)
    #     text = self.droppable_page.get_drop_text(self.droppable_page.DROP_HERE_ACCEPT)
    #     assert text == "Drop here", "'Not Acceptable' elementini tashlaganda matn o'zgarib ketdi."

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
    def test_prevent_propagation_greedy_outer(self):
        """'Greedy' rejimida faqat tashqi qutiga tashlaganda, faqat tashqi quti matni o'zgarishini tekshiradi."""
        self.droppable_page.switch_to_prevent_prop_tab()
        drag_element = self.droppable_page.wait_for_element_visible(self.droppable_page.PP_DRAG_BOX)
        drop_element = self.droppable_page.wait_for_element_visible(self.droppable_page.GREEDY_OUTER_DROPPABLE)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drag_element)
        try:
            self.droppable_page.drag_and_drop(self.droppable_page.PP_DRAG_BOX,
                                              self.droppable_page.GREEDY_OUTER_DROPPABLE)
        except Exception as e:
            print(f"ActionChains failed: {e}. Falling back to JavaScript drag-and-drop.")
            self.droppable_page.drag_and_drop_js(self.droppable_page.PP_DRAG_BOX,
                                                 self.droppable_page.GREEDY_OUTER_DROPPABLE)
        outer_text = self.droppable_page.get_drop_text(self.droppable_page.GREEDY_OUTER_TEXT)
        inner_text = self.droppable_page.get_drop_text(self.droppable_page.GREEDY_INNER_TEXT)
        # assert outer_text == "Dropped!", "Tashqi quti matni 'Dropped!' bo‘lmadi."
        # assert inner_text == self.droppable_page.get_drop_text(self.droppable_page.GREEDY_INNER_TEXT, initial=True), \
        #     "Ichki quti matni o‘zgardi, lekin o‘zgarmasligi kerak edi."



