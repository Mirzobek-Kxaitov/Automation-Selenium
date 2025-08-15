from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Browser_windows_page(BasePage):
    NEW_TAB = (By.XPATH,"//button[@id='tabButton']")
    NEW_WINDOW = (By.XPATH,"//button[@id='windowButton']")
    NEW_WINDOW_MESSAGE = (By.XPATH,"//button[@id='messageWindowButton']")
    NEW_WINDOW_BODY_TEXT = (By.TAG_NAME, "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization.")

    def click_new_tab(self):
        self.click(self.NEW_TAB)

    def click_new_window(self):
        self.click(self.NEW_WINDOW)

    def click_new_window_message(self):
        self.click(self.NEW_WINDOW_MESSAGE)

    def get_new_window_message_text(self):
        try:
            element = self._visibility_of_element_located(self.NEW_WINDOW_BODY_TEXT)
            return self.get_text(self.NEW_WINDOW_BODY_TEXT)
        except Exception as e:
            self.logger.error(f"Yanggi oyna matnini olishda xato: {e}")
            self._take_screenshot("get_new_window_message_text_error")
            raise