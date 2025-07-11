from base.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ProgressBarPage(BasePage):
    START_STOP_BUTTON = (By.ID, "startStopButton")
    RESET_BUTTON = (By.ID, "resetButton")
    PROGRESS_BAR = (By.ID, "progressBar")

    def click_start_stop_button(self):
        self.click(self.START_STOP_BUTTON)

    def click_reset_button(self):
        self.click(self.RESET_BUTTON)

    def get_progress_value(self):
        element = self.wait_for_element_visible(self.PROGRESS_BAR)
        progress_text = element.text.strip()

        if not progress_text:
            return 0

        return int(progress_text.replace("%", ""))

    def wait_until_complete(self, timeout=30):
        start_time = time.time()
        while time.time() - start_time < timeout:
            progress = int(self.get_progress_value())
            if progress >= 100:
                break
            time.sleep(0.5)