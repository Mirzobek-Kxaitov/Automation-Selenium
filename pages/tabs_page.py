from selenium.webdriver.common.by import By
from base.base_page import BasePage

class TabsPage(BasePage):
    WHAT_TAB = (By.ID, "demo-tab-what")
    ORIGIN_TAB = (By.ID, "demo-tab-origin")
    USE_TAB = (By.ID, "demo-tab-use")

    WHAT_CONTENT = (By.ID, "demo-tabpane-what")
    ORIGIN_CONTENT = (By.ID, "demo-tabpane-origin")
    USE_CONTENT = (By.ID, "demo-tabpane-use")

    def click_what_tab(self):
        self.click(self.WHAT_TAB)

    def click_origin_tab(self):
        self.click(self.ORIGIN_TAB)

    def click_use_tab(self):
        self.click(self.USE_TAB)

    def get_what_text(self):
        return self.wait_for_element_visible(self.WHAT_CONTENT).text.strip()

    def get_origin_text(self):
        return self.wait_for_element_visible(self.ORIGIN_CONTENT).text.strip()

    def get_use_text(self):
        return self.wait_for_element_visible(self.USE_CONTENT).text.strip()
