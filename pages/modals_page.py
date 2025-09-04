from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Modals_page(BasePage):
    # Button locators
    SMALL_MODAL_BUTTON = (By.ID, "showSmallModal")
    LARGE_MODAL_BUTTON = (By.ID, "showLargeModal")

    # Modal locators
    MODAL_DIALOG = (By.CLASS_NAME, "modal-dialog")
    MODAL_CONTENT = (By.CLASS_NAME, "modal-content")
    MODAL_BACKDROP = (By.CLASS_NAME, "modal-backdrop")

    # Modal content locators
    MODAL_TITLE = (By.CLASS_NAME, "modal-title")
    MODAL_BODY = (By.CLASS_NAME, "modal-body")
    MODAL_FOOTER = (By.CLASS_NAME, "modal-footer")

    # Close button locators
    CLOSE_BUTTON = (By.CLASS_NAME, "close")
    CLOSE_BUTTON_ALT = (By.CSS_SELECTOR, "button[data-dismiss='modal']")
    CLOSE_X_BUTTON = (By.CSS_SELECTOR, ".modal-header .close")

    def click_small_modal(self):
        """Small modal buttonini bosish"""
        try:
            self.click(self.SMALL_MODAL_BUTTON)
            self.logger.info("Small modal button clicked successfully")
            # Modal ochilishini kutish
            self.wait_for_modal_to_appear()
        except Exception as e:
            self.logger.error(f"Failed to click small modal button: {e}")
            self._take_screenshot("small_modal_click_error")
            raise

    def click_large_modal(self):
        """Large modal buttonini bosish"""
        try:
            self.click(self.LARGE_MODAL_BUTTON)
            self.logger.info("Large modal button clicked successfully")
            # Modal ochilishini kutish
            self.wait_for_modal_to_appear()
        except Exception as e:
            self.logger.error(f"Failed to click large modal button: {e}")
            self._take_screenshot("large_modal_click_error")
            raise

    def wait_for_modal_to_appear(self, timeout=10):
        """Modal ochilishini kutish"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.MODAL_DIALOG)
            )
            # CSS animation tugashini kutish
            time.sleep(0.5)
            self.logger.info("Modal appeared successfully")
            return True
        except Exception as e:
            self.logger.error(f"Modal did not appear: {e}")
            return False

    def is_modal_visible(self):
        """Modal ko'rinadigan yoki yo'qligini tekshirish"""
        try:
            modal_elements = self.driver.find_elements(*self.MODAL_DIALOG)
            if len(modal_elements) == 0:
                return False

            modal = modal_elements[0]
            return modal.is_displayed() and modal.size['width'] > 0
        except Exception as e:
            self.logger.error(f"Error checking modal visibility: {e}")
            return False

    def get_modal_title_text(self):
        """Modal title textini olish"""
        try:
            title_element = self.wait_for_element_visible(self.MODAL_TITLE)
            title = title_element.text.strip()
            self.logger.info(f"Modal title: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Failed to get modal title: {e}")
            return ""

    def get_modal_body_text(self):
        """Modal body textini olish"""
        try:
            body_element = self.wait_for_element_visible(self.MODAL_BODY)
            body = body_element.text.strip()
            self.logger.info(f"Modal body length: {len(body)} characters")
            return body
        except Exception as e:
            self.logger.error(f"Failed to get modal body text: {e}")
            return ""

    def close_modal(self):
        """Modal'ni yopish (bir necha usul bilan)"""
        try:
            # Method 1: X button
            close_buttons = self.driver.find_elements(*self.CLOSE_X_BUTTON)
            if len(close_buttons) > 0:
                close_buttons[0].click()
                self.logger.info("Modal closed using X button")
                self.wait_for_modal_to_disappear()
                return True

            # Method 2: Generic close button
            close_buttons = self.driver.find_elements(*self.CLOSE_BUTTON)
            if len(close_buttons) > 0:
                close_buttons[0].click()
                self.logger.info("Modal closed using close button")
                self.wait_for_modal_to_disappear()
                return True

            # Method 3: ESC key
            from selenium.webdriver.common.keys import Keys
            self.driver.find_element('tag name', 'body').send_keys(Keys.ESCAPE)
            self.logger.info("Modal closed using ESC key")
            self.wait_for_modal_to_disappear()
            return True

        except Exception as e:
            self.logger.error(f"Failed to close modal: {e}")
            self._take_screenshot("modal_close_error")
            return False

    def wait_for_modal_to_disappear(self, timeout=10):
        """Modal yopilishini kutish"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(self.MODAL_DIALOG)
            )
            self.logger.info("Modal disappeared successfully")
            return True
        except Exception as e:
            self.logger.warning(f"Modal may still be visible: {e}")
            return False

    def click_modal_backdrop(self):
        """Modal backdrop'ni bosib modal yopish"""
        try:
            backdrop_elements = self.driver.find_elements(*self.MODAL_BACKDROP)
            if len(backdrop_elements) > 0:
                backdrop_elements[0].click()
                self.logger.info("Clicked modal backdrop")
                self.wait_for_modal_to_disappear()
                return True
            else:
                self.logger.warning("Modal backdrop not found")
                return False
        except Exception as e:
            self.logger.error(f"Failed to click modal backdrop: {e}")
            return False

    def get_modal_info(self):
        """Modal haqida to'liq ma'lumot olish"""
        try:
            info = {
                'is_visible': self.is_modal_visible(),
                'title': self.get_modal_title_text(),
                'body_length': len(self.get_modal_body_text()),
                'has_close_button': len(self.driver.find_elements(*self.CLOSE_BUTTON)) > 0,
                'has_backdrop': len(self.driver.find_elements(*self.MODAL_BACKDROP)) > 0
            }
            self.logger.info(f"Modal info: {info}")
            return info
        except Exception as e:
            self.logger.error(f"Failed to get modal info: {e}")
            return {}