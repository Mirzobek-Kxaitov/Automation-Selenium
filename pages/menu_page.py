from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class Menu_Page(BasePage):
    MAIN_ITEM_1 = (By.XPATH,'//*[@id="nav"]/li[1]/a')
    MAIN_ITEM_2 = (By.XPATH,'//*[@id="nav"]/li[2]/a')
    MAIN_ITEM_3 = (By.XPATH,'//*[@id="nav"]/li[3]/a')
    SUB_ITEM_1 = (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[1]/a')
    SUB_ITEM_2 = (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[2]/a')
    SUB_SUB_LIST= (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
    SUB_SUB_ITEM_1 = (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[1]/a')
    SUB_SUB_ITEM_2 = (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')

    def hover_main_item_one(self):
        try:
            element = self.wait_for_element_visible(self.MAIN_ITEM_1)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("Successfully hovered Main Item 1 button")
        except Exception as e:
            self.logger.error(f"Failed to hover : {str(e)}")
            self._take_screenshot("hover_button_error")
            raise


    def hover_main_item_two(self):
        try:
            element = self.wait_for_element_visible(self.MAIN_ITEM_2)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("Successfully hovered Main Item 2 button")
        except Exception as e:
            self.logger.error(f"Failed to hover : {str(e)}")
            self._take_screenshot("hover_button_error")
            raise


    def hover_main_item_three(self):
        try:
            element = self.wait_for_element_visible(self.MAIN_ITEM_3)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("Successfully hovered Main Item 3 button")
        except Exception as e:
            self.logger.error(f"Failed to hover : {str(e)}")
            self._take_screenshot("hover_button_error")
            raise


    def hover_sub_item_one(self):
        try:
            element = self.wait_for_element_visible(self.SUB_ITEM_1)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("Successfully hovered Sub Item 1 button")
        except Exception as e:
            self.logger.error(f"Failed to hover : {str(e)}")
            self._take_screenshot("hover_button_error")
            raise

    def is_submenu_visible(self):
        try:
            element = self.wait_for_element_visible(self.SUB_ITEM_1)
            self.logger.info("Sub-menu is visible")
            return element.is_displayed()
        except Exception as e:
            self.logger.info("Sub-menu is not visible")
            return False

    def wait_for_submenu_to_appear(self):
        try:
            element = self.wait_for_element_visible(self.SUB_ITEM_1)
            self.logger.info("Sub-menu appeared successfully")
            return element
        except Exception as e:
            self.logger.error(f"Sub-menu did not appear: {str(e)}")
            self._take_screenshot("submenu_not_appeared")
            raise

    def hover_sub_sub_list(self):
        try:
            element = self.wait_for_element_visible(self.SUB_SUB_LIST)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("Successfully hovered SUB SUB LIST")
        except Exception as e:
            self.logger.error(f"Failed to hover SUB SUB LIST: {str(e)}")
            self._take_screenshot("hover_sub_sub_list_error")
            raise

    def hover_sub_sub_item_one(self):
        try:
            element = self.wait_for_element_visible(self.SUB_SUB_ITEM_1)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("Successfully hovered Sub Sub Item 1")
        except Exception as e:
            self.logger.error(f"Failed to hover Sub Sub Item 1: {str(e)}")
            self._take_screenshot("hover_sub_sub_item_error")
            raise

    def is_nested_submenu_visible(self):
        try:
            element = self.wait_for_element_visible(self.SUB_SUB_ITEM_1)
            self.logger.info("Nested sub-menu is visible")
            return element.is_displayed()
        except Exception as e:
            self.logger.info("Nested sub-menu is not visible")
            return False