from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Links_page(BasePage):

    home_button = (By.XPATH, "//a[@id='simpleLink']")
    def click_home_button(self):
        element = self.driver.find_element(*self.home_button)
        element.click()


    def switch_to_new_tab(self):
        original_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles


        for window in all_windows:
            if window != original_window:
                new_window = window
                break
        self.driver.switch_to.window(new_window)

    def get_original_window(self):
        return self.driver.current_window_handle

    def close_current_tab(self):
        self.driver.close()

    def switch_to_original_tab(self,original_window):
        self.driver.switch_to.window(original_window)


    created_button = (By.XPATH, "//a[@id='created']")  # Created link
    no_content_button = (By.XPATH,"//a[@id='no-content']")
    moved_button = (By.XPATH,"//a[@id='moved']")
    bad_request_button = (By.XPATH,"//a[@id='bad-request']")
    unauthorized_button = (By.XPATH,"//a[@id='unauthorized']")
    forbidden_button = (By.XPATH,"//a[@id='forbidden']")
    not_found_button = (By.XPATH,"//a[@id='invalid-url']")

# ------------------------------------------------------------------------------------------------------------------------------
    response_message = (By.XPATH, "//p[@id='linkResponse']")  # Response area
# ------------------------------------------------------------------------------------------------------------------------------
    def click_created_button(self):
        self.click(self.created_button)

    def click_no_content_button(self):
        self.click(self.no_content_button)

    def click_moved_button(self):
        self.click(self.moved_button)

    def click_bad_request_button(self):
        self.click(self.bad_request_button)

    def click_unauthorized_button(self):
        self.click(self.unauthorized_button)

    def click_forbidden_button(self):
        self.click(self.forbidden_button)

    def click_not_found_button(self):
        self.click(self.not_found_button)

    def verify_response_message(self):
        return self.get_text(self.response_message)

# ------------------------------------------------------------------------------------------------------------------------------

