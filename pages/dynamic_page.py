import time
from logging import exception
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from selenium.webdriver.common.by import By

class Dynamic_page(BasePage):
    after_enable_button = (By.XPATH, "//button[@id='enableAfter']")
    color_change = (By.XPATH, "//button[@id='colorChange']")
    after_visible_button = (By.XPATH, "//button[@id='visibleAfter']")
    random_text = (By.XPATH, "//p[contains(text(), 'This text has random Id')]")
# ------------------------------------------------------------------------------------------------------------------------

    def click_after_enable_button(self):
        try:
            time.sleep(5)
            element = self._element_to_be_clickable(self.after_enable_button)
            element.click()
            self.logger.info("Enable button clicked successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error clicking enable button : {str(e)}")
            return False

    # ------------------------------------------------------------------------------------------------------------------------
    def click_colour_change_button(self):
        try:
            element = self.wait_for_element_visible(self.color_change)
            color = element.value_of_css_property("background-color")
            element.click()
            self.logger.info(f"Button clicked, colour: {color}")
            return True

        except Exception as e:
            self.logger.error(f"Error checking colour {str(e)}")
            return False

    # ------------------------------------------------------------------------------------------------------------------------------

    def click_visible_after(self):
        try:
            time.sleep(5)
            element = self.wait_for_element_visible(self.after_visible_button)
            element.click()
            self.logger.info("Visible button clicked successfully")
            return True

        except Exception as e:
            self.logger.error(f" Error visible button {str(e)}")
            return False
# ------------------------------------------------------------------------------------------------------------------------------

    def verify_random_text_displayed(self):
        try:
            text_element = self.wait_for_element_visible(self.random_text)
            current_text = text_element.text
            # DEBUG: Nima topilganini ko'rish
            print(f"DEBUG - Found text: '{current_text}'")
            print(f"DEBUG - Looking for: 'This text has random id'")

            if "This text has random Id" in current_text:
                self.logger.info("Random text verification successfully")
                return True
            else:
                self.logger.error(f"Random text not found. Found: {current_text} ")
                return False

        except Exception as e:
            self.logger.error(f"Error verifying random text: {str(e)}")
            print(f"DEBUG - Exception: {str(e)}")  # DEBUG
            return False
    # -------------------------------------------------------------------------------------------------------------------------------
    def verify_enable_button_clickable(self):
        try:
            # Avval buttonni topish
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.presence_of_element_located(self.after_enable_button))

            # Buttonning boshlang'ich holatini tekshirish
            if not element.is_enabled():
                self.logger.info("Button is initially disabled")
                print("DEBUG - Button is initially disabled")

                # 5 soniya kutish
                wait.until(EC.element_to_be_clickable(self.after_enable_button))
#
                # Qayta tekshirish
                if element.is_enabled():
                    self.logger.info("Button became enabled after waiting")
                    print("DEBUG - Button became enabled")
                    return True
                else:
                    self.logger.error("Button didn't become enabled")
                    print("DEBUG - Button still disabled")
                    return False
            else:
                self.logger.error("Button was already enabled initially")
                print("DEBUG - Button was already enabled")
                return False

        except Exception as e:
            self.logger.error(f"Error verifying enable button: {str(e)}")
            print(f"DEBUG - Exception in enable button: {str(e)}")
            return False
    # ------------------------------------------------------------------------------------------------------------------------------

    def verify_color_change(self):
        try:
            element = self.wait_for_element_visible(self.color_change)
            original_color = element.value_of_css_property("background-color")
            self.logger.info(f"Original color: {original_color}")

            element.click()
            time.sleep(1)

            new_color = element.value_of_css_property("background-color")
            self.logger.info(f"New color{new_color}")

            if original_color != new_color:
                self.logger.info("Color change verified succesfully")
                return True
            else:
                self.logger.error("Color didn'nt change")
                return False

        except Exception as e:
            self.logger.error(f"Error verifying color change {str(e)}")
            return False

    # ------------------------------------------------------------------------------------------------------------------------------

    def verification_visible_button(self):
        try:
            wait = WebDriverWait(self.driver, 10)

            # Element topilguncha kutamiz
            element = wait.until(EC.presence_of_element_located(self.after_visible_button))

            # Agar button allaqachon visible bo'lsa, bu normal - test pass bo'lishi kerak
            if element.is_displayed():
                self.logger.info("Button is visible (this is expected behavior)")
                print("DEBUG - Button is visible - TEST PASSED")
                return True
            else:
                # Agar ko'rinmasa, 5 soniya kutib ko'ramiz
                self.logger.info("Button is initially not visible, waiting...")
                print("DEBUG - Button is initially not visible")

                # 5 soniya kutamiz
                time.sleep(5)

                # Qayta tekshiramiz
                if element.is_displayed():
                    self.logger.info("Button became visible after 5 seconds")
                    print("DEBUG - Button became visible")
                    return True
                else:
                    self.logger.error("Button didn't become visible")
                    print("DEBUG - Button still not visible")
                    return False

        except Exception as e:
            self.logger.error(f"Error verifying button visibility: {str(e)}")
            print(f"DEBUG - Exception in visible button: {str(e)}")
            return False