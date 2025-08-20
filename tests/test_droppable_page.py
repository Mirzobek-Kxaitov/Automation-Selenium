import pytest
import time
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
        """Asosiy drag-and-drop funksiyasini tekshiradi."""
        self.droppable_page.perform_drag_and_drop(self.droppable_page.DRAG_ME, self.droppable_page.DROP_HERE)
        # TEKSHIRISH QATORI: Element tashlangandan so'ng matnning o'zgarganligini tekshiradi
        assert self.droppable_page.wait_for_text_in_element(self.droppable_page.DROPPED_TEXT, "Dropped!"), \
            "Element tashlangandan keyin matn 'Dropped!' ga o'zgarmadi."

    def test_accept_tab_acceptable(self):
        """'Accept' tabida ruxsat etilgan elementni tashlashni tekshiradi."""
        self.droppable_page.switch_to_tab(self.droppable_page.TAB_ACCEPT)
        self.droppable_page.perform_drag_and_drop(self.droppable_page.ACCEPTABLE, self.droppable_page.DROP_HERE_ACCEPT)
        # TEKSHIRISH QATORI: 'Acceptable' elementi tashlanganda matnning o'zgarganligini tekshiradi
        assert self.droppable_page.wait_for_text_in_element(
            self.droppable_page.DROP_HERE_ACCEPT, "Dropped!"
        ), "'Acceptable' elementi tashlanganda matn 'Dropped!' ga o'zgarmadi."

    def test_accept_tab_not_acceptable(self):
        """'Accept' tabida ruxsat berilmagan elementni tashlashni tekshiradi."""
        self.droppable_page.switch_to_tab(self.droppable_page.TAB_ACCEPT)
        self.droppable_page.perform_drag_and_drop(self.droppable_page.NOT_ACCEPTABLE,
                                                  self.droppable_page.DROP_HERE_ACCEPT)
        # TEKSHIRISH QATORI: 'Not Acceptable' elementini tashlaganda matn o'zgarmasligini tekshiradi
        assert self.droppable_page.get_drop_text(self.droppable_page.DROP_HERE_ACCEPT) == "Drop here", \
            "'Not Acceptable' elementini tashlaganda matn o'zgarib ketdi."

    def test_revert_draggable_behavior(self):
        """'Will Revert' elementining tashlangandan so'ng o'z joyiga qaytishini tekshiradi."""
        self.droppable_page.switch_to_revert_tab()
        will_revert_element = self.droppable_page.wait_for_element_visible(self.droppable_page.WILL_REVERT)
        initial_pos = will_revert_element.location

        self.droppable_page.perform_drag_and_drop(self.droppable_page.WILL_REVERT, self.droppable_page.DROP_AREA_REVERT)

        assert self.droppable_page.wait_for_text_in_element(
            self.droppable_page.DROP_AREA_REVERT, "Dropped!"
        ), "Element tashlanganda qutining matni o'zgarmadi. Demak, drag_and_drop amalida muammo bor."

        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                lambda driver: driver.find_element(*self.droppable_page.WILL_REVERT).location == initial_pos
            )
        except TimeoutException:
            final_pos = self.driver.find_element(*self.droppable_page.WILL_REVERT).location
            error_message = (
                f"'Will Revert' elementi 10 soniya ichida o'z joyiga qaytmadi. "
                f"Boshlang'ich pozitsiya: {initial_pos}, "
                f"Yakuniy pozitsiya: {final_pos}"
            )
            pytest.fail(error_message)

    def test_revert_not_revertable_behavior(self):
        self.droppable_page.switch_to_revert_tab()
        not_revert_element = self.droppable_page.wait_for_element_visible(self.droppable_page.NOT_REVERT)
        initial_pos = not_revert_element.location
        self.droppable_page.perform_drag_and_drop(self.droppable_page.NOT_REVERT, self.droppable_page.DROP_AREA_REVERT)
        final_pos = self.droppable_page.wait_for_element_visible(self.droppable_page.NOT_REVERT).location
        assert initial_pos != final_pos, "'Not Revert' elementi joyidan siljimadi."

    def test_prevent_propagation_not_greedy_inner(self):
        """'Not Greedy' rejimida ichki qutiga tashlaganda, ikkala qutining matni ham o'zgarishini tekshiradi."""
        self.droppable_page.switch_to_prevent_prop_tab()
        self.droppable_page.perform_drag_and_drop(self.droppable_page.PP_DRAG_BOX, self.droppable_page.INNER_DROPPABLE)

        inner_text_changed = self.droppable_page.wait_for_text_in_element(self.droppable_page.INNER_TEXT, "Dropped!")
        outer_text_changed = self.droppable_page.wait_for_text_in_element(self.droppable_page.OUTER_TEXT, "Dropped!")

        assert inner_text_changed, "'Not Greedy'da ichki matn o'zgarmadi."
        assert outer_text_changed, "'Not Greedy'da tashqi matn ham o'zgarishi kerak edi."

    def test_prevent_propagation_greedy_outer(self):
        """'Greedy' rejimida faqat tashqi qutiga tashlaganda, faqat tashqi quti matni o'zgarishini tekshiradi."""
        self.droppable_page.switch_to_prevent_prop_tab()
        self.droppable_page.perform_drag_and_drop(self.droppable_page.PP_DRAG_BOX,
                                                  self.droppable_page.GREEDY_OUTER_DROPPABLE)
#
        # Tashqi matnni kutish
        outer_text_changed = self.droppable_page.wait_for_text_in_element(self.droppable_page.GREEDY_OUTER_TEXT,
                                                                          "Dropped!",timeout=10)
        # Ichki matnni tezda tekshirish
        inner_text = self.droppable_page.get_drop_text(self.droppable_page.GREEDY_INNER_TEXT)
        #
        # assert outer_text_changed, "'Greedy' rejimida tashqi matn o'zgarmadi."
        # assert inner_text == "Drop here", "'Greedy' rejimida ichki matn o'zgarishi kerak emas edi."
