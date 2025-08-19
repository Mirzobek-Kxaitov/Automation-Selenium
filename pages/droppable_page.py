from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class DroppablePage(BasePage):
    # Element locatorlari
    DRAG_ME = (By.ID, "draggable")
    PP_DRAG_BOX = (By.ID, "dragBox")   # Prevent Propagation tab uchun
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
    def scroll_to_element(self, locator: tuple):
        """Element ekranga ko'rinadigan bo'lguncha skroll qiladi."""
        element: WebElement = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_for_element_visible(source_locator)
        target = self.wait_for_element_visible(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def get_drop_text(self, locator):
        el = self.wait_for_element_visible(locator)
        return el.text
# ----------------------------------------------------------------------------------------------------------------------------
    def switch_to_tab(self, tab_locator):
        self.click(tab_locator)

    def switch_to_revert_tab(self):
        self.click(self.TAB_REVERT)

    def switch_to_prevent_prop_tab(self):
        self.click(self.TAB_PREVENT_PROP)

# --------------------------------------------------
