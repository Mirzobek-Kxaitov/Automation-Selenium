from base.base_page import BasePage
from selenium.webdriver.common.by import By

class Modals_page(BasePage):
    SMALL_MODAL = (By.XPATH, "//button[@id='showSmallModal']")
    LARGE_MODAL = (By.XPATH, "//button[@id='showLargeModal']")
    MODAL_DIALOG = (By.CLASS_NAME, "modal-dialog")
    MODAL_CONTENT = (By.CLASS_NAME, "modal-content")
    SMALL_MODAL_TITLE = (By.ID, "example-modal-sizes-title-sm")
    LARGE_MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "close")
    MODAL_BODY = (By.CLASS_NAME, "modal-body")

    def click_small_modal(self):
        self.click(self.SMALL_MODAL)

    def click_large_modal(self):
        self.click(self.LARGE_MODAL)

    def is_modal_visible(self):
        try:
            self.wait_for_element_visible(self.MODAL_DIALOG)
            return True
        except:
            return False

    def close_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    def get_modal_title_text(self):
        try:
            return self.get_text(self.SMALL_MODAL_TITLE)
        except:
            return self.get_text(self.LARGE_MODAL_TITLE)

    def get_modal_body_text(self):
        return self.get_text(self.MODAL_BODY)