from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from base.base_page import BasePage


class Resizable_Page(BasePage):
    RESIZE_HANDLE = (By.XPATH, "//span[contains(@class, 'react-resizable-handle')]")
    RESIZABLE_BOX = (By.ID, "resizableBoxWithRestriction")

    def get_box_size(self):
        box =self.wait_for_element_visible(self.RESIZABLE_BOX)
        return box.size

    def resize_box(self, x_offset, y_offset):
        handle = self.wait_for_element_visible(self.RESIZE_HANDLE)
        actions = ActionChains(self.driver)
        actions.click_and_hold(handle).move_by_offset(x_offset, y_offset).release().perform()

    def is_resize_handle_displayed(self):
        handle = self.wait_for_element_visible(self.RESIZE_HANDLE)
        return handle.is_displayed()
