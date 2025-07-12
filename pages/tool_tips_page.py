from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class ToolTipsPage(BasePage):

    HOVER_BUTTON = (By.ID,"toolTipButton")
    HOVER_INPUT = (By.ID, "toolTipTextField")
    TOOLTIP_TEXT = (By.CLASS_NAME, "tooltip-inner")

    def hover_over_button(self):
        try:
            element = self.wait_for_element_visible(self.HOVER_BUTTON)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("Successfully hovered over button")
        except Exception as e:
            self.logger.error(f"Failed to hover button: {str(e)}")
            self._take_screenshot("hover_button_error")
            raise

    def click_hover_button(self):
        """Click the hover button"""
        try:
            self.click(self.HOVER_BUTTON)
            self.logger.info("Successfully clicked hover button")
        except Exception as e:
            self.logger.error(f"Failed to click hover button: {str(e)}")
            raise

    def get_tooltip_text(self):
        try:
            tooltip_element = self.wait_for_element_visible(self.TOOLTIP_TEXT)
            tooltip_text = tooltip_element.text
            self.logger.info(f"Successfully got tooltip text: {tooltip_text}")
            return tooltip_text
        except Exception as e:
            self.logger.error(f"Failed to get tooltip text: {str(e)}")
            self._take_screenshot("tooltip_text_error")
            raise

    def is_tooltip_visible(self):
        try:
            self.wait_for_element_visible(self.TOOLTIP_TEXT)
            return True
        except:
            return False

    def hover_over_input(self):
        try:
            element = self.wait_for_element_visible(self.HOVER_INPUT)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("Successfully hovered over input field")
        except Exception as e:
            self.logger.error(f"Failed to hover over input: {str(e)}")
            self._take_screenshot("hover_input_error")
            raise

    def input_text_to_field(self, text):
        try:
            self.input_text(self.HOVER_INPUT, text)
            self.logger.info(f"Successfully entered text: {text}")
        except Exception as e:
            self.logger.error(f"Failed to enter text in input: {str(e)}")
            raise

    def move_mouse_away(self):
        try:
            ActionChains(self.driver).move_by_offset(-100, -100).perform()
            self.logger.info("Successfully moved mouse away")
        except Exception as e:
            self.logger.error(f"Failed to move mouse away: {str(e)}")
            raise
