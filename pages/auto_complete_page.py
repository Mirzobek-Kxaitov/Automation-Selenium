from base.base_page import BasePage
from selenium.webdriver.common.by import By

class AutoComplete_page(BasePage):
    SINGLE_COLOR_INPUT = (By.XPATH, "//input[@id='autoCompleteSingleInput']")
    MULTIPLE_COLOR_INPUT = (By.XPATH, "//input[@id='autoCompleteMultipleInput']")
    COLOR_SUGGESTIONS = (By.XPATH, "//div[@class='auto-complete__option']")
    SELECTED_COLOR_TAGS = (By.XPATH, "//div[@class='css-12jo7m5 auto-complete__multi-value__label']")
    REMOVE_COLOR_BUTTON = (By.XPATH, "//div[@class='css-xb97g8 auto-complete__multi-value__remove']")

    def input_single_color(self,color_text):
        try:
            self.input_text(self.SINGLE_COLOR_INPUT,color_text)
            self.logger.info(f"Successfully entered text in single color input: {color_text}")
        except Exception as e:
            self.logger.error(f"Failed to enter text in single color input: {str(e)}")
            self._take_screenshot("single_color_input_error")
            raise

    def input_multiple_color(self, color_text):
        """Multiple color input field ga rang nomini yozadi"""
        try:
            self.input_text(self.MULTIPLE_COLOR_INPUT, color_text)
            self.logger.info(f"Successfully entered text in multiple color input: {color_text}")
        except Exception as e:
            self.logger.error(f"Failed to enter text in multiple color input: {str(e)}")
            self._take_screenshot("multiple_color_input_error")
            raise


    def select_color_from_suggestions(self, color_name):
        try:
            suggestions = self.driver.find_elements(By.XPATH,"//div[contains(@class, 'auto-complete__option')]")
            for suggestion in suggestions:
                if color_name.lower() in suggestion.text.lower():
                    suggestion.click()
                    self.logger.info(f"Successfully selected color:{color_name}")
                    return True

            self.logger.error(f"Color {color_name} not found in suggestions")
            return False

        except Exception as e:
            self.logger.error(f"Failed to select color from suggestions: {str(e)}")
            self._take_screenshot("select_color_error")
            raise

    def get_selected_colors(self):
        try:
            color_tags = self.driver.find_elements(*self.SELECTED_COLOR_TAGS)
            colors = [tag.text for tag in color_tags]
            self.logger.info(f"Selected colors: {colors}")
            return colors
        except Exception as e:
            self.logger.error(f"Failed to get selected colors: {str(e)}")
            return []

    def remove_color(self, color_index=0):
        try:
            remove_buttons = self.driver.find_elements(*self.REMOVE_COLOR_BUTTON)
            if remove_buttons and len(remove_buttons) > color_index:
                remove_buttons[color_index].click()
                self.logger.info(f"Successfully removed color at index: {color_index}")
                return True
            else:
                self.logger.error(f"No color found at index: {color_index}")
                return False

        except Exception as e:
            self.logger.error(f"Failed to remove color {str(e)}")
            self._take_screenshot("remove_color_error")
            raise

