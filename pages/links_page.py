from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Links_page(BasePage):
    # Simple link (new tab ochish uchun)
    home_button = (By.ID, "simpleLink")
    # API call links
    created_button = (By.ID, "created")
    no_content_button = (By.ID, "no-content")
    moved_button = (By.ID, "moved")
    bad_request_button = (By.ID, "bad-request")
    unauthorized_button = (By.ID, "unauthorized")
    forbidden_button = (By.ID, "forbidden")
    not_found_button = (By.ID, "invalid-url")

    # Response message area
    response_message = (By.ID, "linkResponse")

    def click_home_button(self):
        """Home linkni bosish (yangi tab ochadi)"""
        try:
            element = self.wait_for_element_visible(self.home_button)
            element.click()
            self.logger.info("Home button clicked successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking home button: {str(e)}")
            return False

    def switch_to_new_tab(self):
        """Yangi tabga o'tish"""
        try:
            original_window = self.driver.current_window_handle
            # Yangi tab ochilishini kutamiz
            WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)

            all_windows = self.driver.window_handles
            for window in all_windows:
                if window != original_window:
                    self.driver.switch_to.window(window)
                    self.logger.info("Successfully switched to new tab")
                    return True
            return False
        except Exception as e:
            self.logger.error(f"Error switching to new tab: {str(e)}")
            return False

    def get_original_window(self):
        """Dastlabki window handle ni olish"""
        return self.driver.current_window_handle

    def close_current_tab(self):
        """Hozirgi tabni yopish"""
        try:
            self.driver.close()
            self.logger.info("Current tab closed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error closing current tab: {str(e)}")
            return False

    def switch_to_original_tab(self, original_window):
        """Dastlabki tabga qaytish"""
        try:
            self.driver.switch_to.window(original_window)
            self.logger.info("Successfully switched back to original tab")
            return True
        except Exception as e:
            self.logger.error(f"Error switching to original tab: {str(e)}")
            return False

    # API call methods
    def click_created_button(self):
        """Created (201) API call"""
        try:
            element = self.wait_for_element_visible(self.created_button)
            element.click()
            self.logger.info("Created button clicked")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking created button: {str(e)}")
            return False

    def click_no_content_button(self):
        """No Content (204) API call"""
        try:
            element = self.wait_for_element_visible(self.no_content_button)
            element.click()
            self.logger.info("No Content button clicked")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking no content button: {str(e)}")
            return False

    def click_moved_button(self):
        """Moved Permanently (301) API call"""
        try:
            element = self.wait_for_element_visible(self.moved_button)
            element.click()
            self.logger.info("Moved button clicked")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking moved button: {str(e)}")
            return False

    def click_bad_request_button(self):
        """Bad Request (400) API call"""
        try:
            element = self.wait_for_element_visible(self.bad_request_button)
            element.click()
            self.logger.info("Bad Request button clicked")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking bad request button: {str(e)}")
            return False

    def click_unauthorized_button(self):
        """Unauthorized (401) API call"""
        try:
            element = self.wait_for_element_visible(self.unauthorized_button)
            element.click()
            self.logger.info("Unauthorized button clicked")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking unauthorized button: {str(e)}")
            return False

    def click_forbidden_button(self):
        """Forbidden (403) API call"""
        try:
            element = self.wait_for_element_visible(self.forbidden_button)
            element.click()
            self.logger.info("Forbidden button clicked")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking forbidden button: {str(e)}")
            return False

    def click_not_found_button(self):
        """Not Found (404) API call"""
        try:
            element = self.wait_for_element_visible(self.not_found_button)
            element.click()
            self.logger.info("Not Found button clicked")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking not found button: {str(e)}")
            return False

    def verify_response_message(self, timeout=5):
        """API response message ni tekshirish"""
        try:
            # Response kelishini kutamiz
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(self.response_message))

            # Text bo'sh emasligini tekshiramiz
            text = element.text.strip()
            if not text:
                # Agar text bo'sh bo'lsa, qisqa kutamiz
                time.sleep(1)
                text = element.text.strip()

            self.logger.info(f"Response message received: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Error getting response message: {str(e)}")
            return ""

    def verify_api_call_response(self, api_call_method, expected_code, expected_text):
        """API call va response ni tekshirish"""
        try:
            # API call qilish
            if not api_call_method():
                return False

            # Response kutish
            response_text = self.verify_response_message()

            # Response tekshirish
            if expected_code in response_text and expected_text in response_text:
                self.logger.info(f"API response verification passed: {response_text}")
                return True
            else:
                self.logger.error(
                    f"API response verification failed. Expected: {expected_code} {expected_text}, Got: {response_text}")
                return False

        except Exception as e:
            self.logger.error(f"Error in API call response verification: {str(e)}")
            return False

    def test_new_tab_functionality(self):
        """Yangi tab ochish funksionalligini tekshirish"""
        try:
            original_window = self.get_original_window()

            # Home button bosamiz
            if not self.click_home_button():
                return False

            # Yangi tabga o'tamiz
            if not self.switch_to_new_tab():
                return False

            # URL tekshiramiz (DemoQA home page bo'lishi kerak)
            current_url = self.driver.current_url
            expected_url_part = "demoqa.com"

            if expected_url_part in current_url:
                self.logger.info(f"New tab opened successfully: {current_url}")
                result = True
            else:
                self.logger.error(f"Wrong URL in new tab: {current_url}")
                result = False

            # Tabni yopamiz va originalga qaytamiz
            self.close_current_tab()
            self.switch_to_original_tab(original_window)

            return result

        except Exception as e:
            self.logger.error(f"Error in new tab functionality test: {str(e)}")
            return False