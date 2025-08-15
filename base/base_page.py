import logging
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self._configure_logging()

# ---------------- Asosiy funksiyalar ----------------

    def click(self, locator):
        try:
            element = self._element_to_be_clickable(locator)
            self._scroll_to_element(element)
            self._click(element)
            self.logger.info(f"Successfully clicked element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element {locator}: {str(e)}")
            self._take_screenshot("click_error")
            raise

# ------------------------------------------------------------------------------------------------------------------------------

    def input_text(self, locator, text):
        try:
            element = self._visibility_of_element_located(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Successfully entered text: {text}")
        except Exception as e:
            self.logger.error(f"Failed to enter text in {locator}: {str(e)}")
            self._take_screenshot("input_error")
            raise
# ------------------------------------------------------------------------------------------------------------------------------

    def get_text(self, locator):
        try:
            element = self._visibility_of_element_located(locator)
            text = element.text
            self.logger.info(f"Successfully got text: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Failed to get text from {locator}: {str(e)}")
            self._take_screenshot("get_text_error")
            raise
# ------------------------------------------------------------------------------------------------------------------------------

    def wait_for_element_visible(self, locator):
        return self._visibility_of_element_located(locator)


# ---------------- Yordamchi funksiyalar ----------------

    def _click(self, element):
        element.click()

# ------------------------------------------------------------------------------------------------------------------------------

    def _element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator))

# ------------------------------------------------------------------------------------------------------------------------------

    def _visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator))

# ------------------------------------------------------------------------------------------------------------------------------

    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

# ------------------------------------------------------------------------------------------------------------------------------

    def _take_screenshot(self, file_name=None):
        if not os.path.exists("screenshots"):
            os.mkdir("screenshots")
        if not file_name:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"screenshots/screenshot_{timestamp}.png"
        else:
            file_name = f"screenshots/{file_name}.png"
        self.driver.save_screenshot(file_name)
        self.logger.info(f"Screenshot saved: {file_name}")

# ------------------------------------------------------------------------------------------------------------------------------

    def _configure_logging(self):
        if not os.path.exists("logs"):
            os.mkdir("logs")

        self.logger = logging.getLogger("BasePageLogger")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            file_handler = logging.FileHandler("logs/test_log.txt")
            formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

# ------------------------------------------------------------------------------------------------------------------------------

    # base_page.py da
    def get_original_window(self):
        return self.driver.current_window_handle

# ------------------------------------------------------------------------------------------------------------------------------

    def close_current_tab(self):
        self.driver.close()

# ------------------------------------------------------------------------------------------------------------------------------

    def switch_to_original_tab(self, original_window):
        self.driver.switch_to.window(original_window)

# ------------------------------------------------------------------------------------------------------------------------------

    def switch_to_new_tab(self):
        original_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != original_window:
                new_window = window
                break
        self.driver.switch_to.window(new_window)
# ------------------------------------------------------------------------------------------------------------------------------

    def upload_file(self,locator,file_path):
        try:
            element = self.wait_for_element_visible(locator)
            element.send_keys(file_path)
            self.logger.info(f"File uploaded successfully: {file_path}")
            return True

        except Exception as e:
            self.logger.error(f" Error uploading file : {str(e)}")
            return False
# ------------------------------------------------------------------------------------------------------------------------------

    def select_dropdown_by_text(self, locator, text):
        try:
            element = self._visibility_of_element_located(locator)
            select = Select(element)
            select.select_by_visible_text(text)
            self.logger.info(f"Successfully selected '{text}' from dropdown")
        except Exception as e:
            self.logger.error(f"Failed to select '{text}' from dropdown: {str(e)}")
            self._take_screenshot("dropdown_error")
            raise

    def select_checkbox(self, locator):
        try:
            element = self._element_to_be_clickable(locator)
            if not element.is_selected():
                element.click()
                self.logger.info(f"Successfully selected checkbox: {locator}")
            else:
                self.logger.info(f"Checkbox already selected: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to select checkbox {locator}: {str(e)}")
            self._take_screenshot("checkbox_error")
            raise
    # ------------------------------------------------------------------------------------------------------------------------------
   #ALERT BILAN ISHLASH
    def get_alert_text(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())  # Alertni kutish
            alert = self.driver.switch_to.alert
            return alert.text
        except Exception as e:
            self.logger.error(f"Error while getting alert text: {e}")
            return None

    def handle_alert(self, action='accept'):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())  # Alertni kutish
            alert = self.driver.switch_to.alert
            if action == 'accept':
                alert.accept()
                self.logger.info("Alert accepted")
            elif action == 'dismiss':
                alert.dismiss()
                self.logger.info("Alert dismissed")
        except Exception as e:
            self.logger.error(f"Error while handling alert: {e}")

    def handle_prompt_alert(self, text, action='accept'):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())  # Alertni kutish
            alert = self.driver.switch_to.alert
            alert.send_keys(text)  # Foydalanuvchi kiritadigan matn
            if action == 'accept':
                alert.accept()
                self.logger.info("Prompt alert accepted with text: " + text)
            elif action == 'dismiss':
                alert.dismiss()
                self.logger.info("Prompt alert dismissed")
        except Exception as e:
            self.logger.error(f"Error while handling prompt alert: {e}")

    # BasePage ga qo'shilishi kerak bo'lgan metodlar:

    def _save_page_source(self, file_name=None):
        """Sahifa manbasini saqlash"""
        if not os.path.exists("logs/page_sources"):
            os.makedirs("logs/page_sources")

        if not file_name:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"logs/page_sources/page_source_{timestamp}.html"
        else:
            file_name = f"logs/page_sources/{file_name}.html"

        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
            self.logger.info(f"Page source saved: {file_name}")
        except Exception as e:
            self.logger.error(f"Failed to save page source: {str(e)}")

    def is_element_present(self, locator):
        """Element mavjudligini tekshirish"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def wait_for_url_contains(self, text, timeout=None):
        """URL da ma'lum matn borligini kutish"""
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: text in driver.current_url
            )
            return True
        except:
            return False

    def click_with_js(self, locator):
        try:
            element = self._element_to_be_clickable(locator)
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"Successfully clicked element with JS: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element with JS {locator}: {str(e)}")
            self._take_screenshot("js_click_error")
            raise

    def wait_for_text_in_element(self, locator, expected_text, timeout=None):
        """Wait for specific text to appear in an element"""
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: expected_text.lower() in
                               driver.find_element(*locator).text.lower()
            )
            return True
        except Exception as e:
            self.logger.error(f"Text '{expected_text}' not found in element {locator}: {str(e)}")
            return False