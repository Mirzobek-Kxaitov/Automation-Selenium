from base.base_page import BasePage
from selenium.webdriver.common.by import By

class Browser_windows_page(BasePage):
    NEW_TAB = (By.XPATH,"//button[@id='tabButton']")
    NEW_WINDOW = (By.XPATH,"//button[@id='windowButton']")
    NEW_WINDOW_MESSAGE = (By.XPATH,"//button[@id='messageWindowButton']")

    def click_new_tab(self):
        self.click(self.NEW_TAB)

    def click_new_window(self):
        self.click(self.NEW_WINDOW)

    def click_new_window_message(self):
        self.click(self.NEW_WINDOW_MESSAGE)
