from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver import ActionChains


class Sortable_Page(BasePage):
    LIST_BUTTON = (By.XPATH, "//a[text()='List']")
    LIST_ONE = (By.XPATH, "(//div[text()='One'])[1]")
    LIST_TWO = (By.XPATH, "(//div[text()='Two'])[1]")
    LIST_THREE = (By.XPATH, "(//div[text()='Three'])[1]")
    LIST_FOUR = (By.XPATH, "(//div[text()='Four'])[1]")
    LIST_FIVE = (By.XPATH, "(//div[text()='Five'])[1]")
    LIST_SIX = (By.XPATH, "(//div[text()='Six'])[1]")
    LIST_SEVEN = (By.XPATH, "(//div[text()='Seven'])[1]")
    LIST_EIGHT = (By.XPATH, "(//div[text()='Eight'])[1]")
    LIST_NINE = (By.XPATH, "(//div[text()='Nine'])[1]")
# -----------------------------------------------------------------------------------------------------------------------
    GRID_BUTTON = (By.XPATH, "//a[text()='Grid']")
    GRID_ONE = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='One']")
    GRID_TWO = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Two']")
    GRID_THREE = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Three']")
    GRID_FOUR = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Four']")
    GRID_FIVE = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Five']")
    GRID_SIX = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Six']")
    GRID_SEVEN = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Seven']")
    GRID_EIGHT = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Eight']")
    GRID_NINE = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Nine']")
# -----------------------------------------------------------------------------------------------------------------------
    def click_list_button(self):
        self.click(self.LIST_BUTTON)
    def drag_and_drop_list(self, source_locator, target_locator):
        source = self.wait_for_element_visible(source_locator)
        target = self.wait_for_element_visible(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        self.logger.info(f"Dragged {source_locator} to {target_locator}")
# -----------------------------------------------------------------------------------------------------------------------
    def click_grid_button(self):
        self.click(self.GRID_BUTTON)
    def drag_and_drop_grid(self, source_locator, target_locator):
        source = self.wait_for_element_visible(source_locator)
        target = self.wait_for_element_visible(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        self.logger.info(f"Dragged {source_locator} to {target_locator}")
