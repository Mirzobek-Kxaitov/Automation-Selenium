import time
from logging import exception

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
            self.logger.info("ENable button clicked successfully")
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
    # ------------------------------------------------------------------------------------------------------------------------------
    def verify_enable_button_clickable(self):

        try:
            element =self.wait_for_element_visible(self.after_enable_button)
            if not element.is_enabled():
                self.logger.info("Button is initially disabled")
                time.sleep(5)
                if element.is_enabled():
                    self.logger.info(" Button became enabled after 5 seconds")
                    return True

                else:
                    self.logger.error("Button didn't become enabled")
                    return False

            else:
                self.logger.error("Buton was already enabled initially")
                return False

        except Exception as e:
            self.logger.error(f"Error verifying enable button : {str(e)}")
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
            elements = self.driver.find_elements(*self.after_visible_button)
            if len(elements) > 0 and elements[0].is_displayed():
                self.logger.error("Button was already visible initially")
                return False

            self.logger.info("Button is initially not visible")
            time.sleep(5)

            element = self.wait_for_element_visible(self.after_visible_button)
            if element.is_displayed():
                self.logger.info("Button became visible after 5 seconds")
                return True

            else:
                self.logger.error("Button didn't become visible ")
                return False

        except Exception as e:
            self.logger.error(f"Error verifying button visibility: {str(e)}")
            return False