from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Bu Page Object Model (POM) sinfi bo'lib, DemoQA saytidagi "Droppable" sahifasining elementlari va ularning metodlarini o'z ichiga oladi.
class DroppablePage(BasePage):
    # Element locatorlari
    DRAG_ME = (By.ID, "draggable")
    PP_DRAG_BOX = (By.ID, "dragBox")  # Prevent Propagation tab uchun
    DROP_HERE = (By.ID, "droppable")  # Basic tab uchun
    DROPPED_TEXT = (By.XPATH, "//div[@id='droppable']/p")

    TAB_REVERT = (By.ID, "droppableExample-tab-revertable")
    WILL_REVERT = (By.ID, "revertable")
    NOT_REVERT = (By.ID, "notRevertable")
    DROP_AREA_REVERT = (By.XPATH, "//div[@id='revertableDropContainer']//div[@id='droppable']")

    TAB_PREVENT_PROP = (By.ID, "droppableExample-tab-preventPropogation")
    OUTER_DROPPABLE = (By.ID, "notGreedyDropBox")  # Outer droppable (not greedy)
    INNER_DROPPABLE = (By.ID, "notGreedyInnerDropBox")  # Inner droppable (not greedy)
    OUTER_TEXT = (By.XPATH, "//div[@id='notGreedyDropBox']/p")
    INNER_TEXT = (By.XPATH, "//div[@id='notGreedyInnerDropBox']/p")

    GREEDY_OUTER_DROPPABLE = (By.ID, "greedyDropBox")
    GREEDY_INNER_DROPPABLE = (By.ID, "greedyDropBoxInner")
    GREEDY_OUTER_TEXT = (By.XPATH, "//div[@id='greedyDropBox']/p")
    GREEDY_INNER_TEXT = (By.XPATH, "//div[@id='greedyDropBoxInner']/p")

    # 'Accept' tab locatorlari
    TAB_ACCEPT = (By.ID, "droppableExample-tab-accept")
    ACCEPTABLE = (By.ID, "acceptable")
    NOT_ACCEPTABLE = (By.ID, "notAcceptable")
    DROP_HERE_ACCEPT = (By.XPATH, "//div[@id='acceptDropContainer']//div[@id='droppable']")

    # ----------------------------------------------------------------------------------------------------------------------------
    def perform_drag_and_drop(self, source_locator, target_locator):
        """
        Manba elementni topib, maqsad elementga olib borib tashlash amalini bajaradi.
        Birinchi bo'lib ActionChains'dan foydalanadi, agar u ishlamasa,
        JavaScript yordamida olib borib tashlashga o'tadi.
        """
        source_element = self.get_element(source_locator)
        target_element = self.get_element(target_locator)

        try:
            # ActionChains bilan sinab ko'rish
            actions = ActionChains(self.driver)
            actions.click_and_hold(source_element).move_to_element(target_element).release().perform()
            self.logger.info("Drag-and-drop performed using ActionChains with explicit steps successfully.")
        except Exception as e:
            # Agar ActionChains muvaffaqiyatsiz bo'lsa, JS-ga o'tish
            self.logger.warning(f"ActionChains failed: {e}. Falling back to JavaScript drag-and-drop.")
            self.html5_drag_and_drop(source_element, target_element)
            self.logger.info("Drag-and-drop performed using JavaScript.")

    def get_drop_text(self, locator):
        """Elementning matnini oladi."""
        el = self.wait_for_element_visible(locator)
        return el.text

    def wait_for_text_in_element(self, locator, text, timeout=10):
        """Element ichidagi matnning belgilangan matnga o'zgarishini kutadi."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            return True
        except:
            return False

    # ----------------------------------------------------------------------------------------------------------------------------
    def switch_to_tab(self, tab_locator):
        """Berilgan locator bo'yicha tabga o'tish uchun ustiga bosadi."""
        self.click(tab_locator)

    def switch_to_revert_tab(self):
        """'Revert' tabiga o'tadi."""
        self.click(self.TAB_REVERT)

    def switch_to_prevent_prop_tab(self):
        """'Prevent Propagation' tabiga o'tadi."""
        self.click(self.TAB_PREVENT_PROP)

