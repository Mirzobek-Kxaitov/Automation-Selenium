from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException


class Select_Menu_Page(BasePage):

    SELECT_VALUE = (By.XPATH,'//div[@id="withOptGroup"]')
    GROUP_1_OPTION_1 = (By.XPATH, "//div[text()='Group 1, option 1']")
    GROUP_1_OPTION_2 = (By.XPATH, "//div[text()='Group 1, option 2']")
    GROUP_2_OPTION_1 = (By.XPATH, "//div[text()='Group 2, option 1']")
    GROUP_2_OPTION_2 = (By.XPATH, "//div[text()='Group 2, option 2']")
    A_ROOT_OPTION = (By.XPATH, "//div[text()='A root option']")
    ANOTHER_ROOT_OPTION = (By.XPATH, "//div[text()='Another root option']")
# -----------------------------------------------------------------------------------------------------------------------
    SELECT_ONE = (By.XPATH, '//div[@id="selectOne"]')
    TITLE_DR = (By.XPATH, "//div[text()='Dr.']")
    TITLE_MR = (By.XPATH, "//div[text()='Mr.']")
    TITLE_MRS = (By.XPATH, "//div[text()='Mrs.']")
    TITLE_MS = (By.XPATH, "//div[text()='Ms.']")
    TITLE_PROF = (By.XPATH, "//div[text()='Prof.']")
    TITLE_OTHER = (By.XPATH, "//div[text()='Other']")
#-----------------------------------------------------------------------------------------------------------------------
    OLD_SELECT_MENU = (By.XPATH, "//select[@id='oldSelectMenu']")
# ----------------------------------------------------------------------------------------------------------------------
    MULTISELECT_DROP_DOWN = (By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div[1]/div[1]')
    MULTISELECT_GREEN = (By.XPATH, '//div[@id="react-select-4-option-0"]')
    MULTISELECT_BLUE = (By.XPATH, '//div[@id="react-select-4-option-1"]')
    MULTISELECT_BLACK = (By.XPATH, '//div[@id="react-select-4-option-2"]')
    MULTISELECT_RED = (By.XPATH, '//div[@id="react-select-4-option-3"]')

# ----------------------------------------------------------------------------------------------------------------------
    STANDARD_MULTI_SELECT = (By.XPATH, "//select[@id='cars']")
# -----------------------------------------------------------------------------------------------------------------------

    def select_group1_option1(self):
        try:
            self.click(self.SELECT_VALUE)
            self.click(self.GROUP_1_OPTION_1)
            self.logger.info(f"Successfully selected Group 1, option 1")

        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise

    def select_group1_option2(self):
        try:
            self.click(self.SELECT_VALUE)
            self.click(self.GROUP_1_OPTION_2)
            self.logger.info("Successfully selected Group 1, option 2")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise
    def select_group2_option1(self):
        try:
            self.click(self.SELECT_VALUE)
            self.click(self.GROUP_2_OPTION_1)
            self.logger.info("Successfully selected Group 2, option 1")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise

    def select_group2_option2(self):
        try:
            self.click(self.SELECT_VALUE)
            self.click(self.GROUP_2_OPTION_2)
            self.logger.info("Successfully selected Group 2, option 2")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise

    def select_a_root_option(self):
        try:
            self.click(self.SELECT_VALUE)
            self.click(self.A_ROOT_OPTION)
            self.logger.info("Successfully selected A root option")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise


    def select_another_root_option(self):
        try:
            self.click(self.SELECT_VALUE)
            self.click(self.ANOTHER_ROOT_OPTION)
            self.logger.info("Successfully selected Another root option")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise
# -----------------------------------------------------------------------------------------------------------------------
    def select_one_option_dr(self):
        try:
            self.click(self.SELECT_ONE)
            self.click(self.TITLE_DR)
            self.logger.info(f"Successfully selected Dr")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise

    def select_one_option_mr(self):
        try:
            self.click(self.SELECT_ONE)
            self.click(self.TITLE_MR)
            self.logger.info(f"Successfully selected Mr")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise
    def select_one_option_mrs(self):
        try:
            self.click(self.SELECT_ONE)
            self.click(self.TITLE_MRS)
            self.logger.info(f"Successfully selected Mrs")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise
    def select_one_option_ms(self):
        try:
            self.click(self.SELECT_ONE)
            self.click(self.TITLE_MS)
            self.logger.info(f"Successfully selected Ms")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise
    def select_one_option_prof(self):
        try:
            self.click(self.SELECT_ONE)
            self.click(self.TITLE_PROF)
            self.logger.info(f"Successfully selected Prof")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise
    def select_one_option_other(self):
        try:
            self.click(self.SELECT_ONE)
            self.click(self.TITLE_OTHER)
            self.logger.info(f"Successfully selected Other")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise

# -----------------------------------------------------------------------------------------------------------------------

    def select_old_style_color(self, color):
        try:
            element = self.wait_for_element_visible(self.OLD_SELECT_MENU)
            select = Select(element)
            select.select_by_visible_text(color)
            self.logger.info(f"Successfully selected {color}")
        except Exception as e:
            self.logger.error(f"Failed to select color: {str(e)}")
            self._take_screenshot("old_select_error")
            raise

# -----------------------------------------------------------------------------------------------------------------------

    def select_multiselect_option(self):
        try:
            # Dropdown ochish
            self.click(self.MULTISELECT_DROP_DOWN)
            # Biroz kutish (option'lar yuklanishi uchun)
            self.click(self.MULTISELECT_GREEN)
            self.click(self.MULTISELECT_BLUE)
            self.click(self.MULTISELECT_BLACK)
            self.click(self.MULTISELECT_RED)
            self.logger.info("Successfully selected Green and Blue")
            return True

        except TimeoutException:
            self.logger.error("Multiselect elements not found within timeout")
            self._take_screenshot("multiselect_timeout")
            return False
        except Exception as e:
            self.logger.error(f"Failed to select multiselect: {str(e)}")
            self._take_screenshot("multiselect_error")
            return False

    def verify_multiselect_selections(self):
        """Multiselect tanlanganligini tekshiradi"""
        try:
            results = {
                'green_selected': False,
                'blue_selected': False,
                'total_selected': 0
            }

            # Green tekshirish
            green_element = self.find_element(self.MULTISELECT_GREEN)
            if green_element.get_attribute('aria-selected') == 'true':
                results['green_selected'] = True
                results['total_selected'] += 1

            # Blue tekshirish
            blue_element = self.find_element(self.MULTISELECT_BLUE)
            if blue_element.get_attribute('aria-selected') == 'true':
                results['blue_selected'] = True
                results['total_selected'] += 1

            return results

        except Exception as e:
            self.logger.error(f"Failed to verify selections: {str(e)}")
            return None

# -----------------------------------------------------------------------------------------------------------------------

    def select_standard_multi_cars(self):
        try:
            element = self.wait_for_element_visible(self.STANDARD_MULTI_SELECT)
            select = Select(element)
            # Multiple cars select
            select.select_by_visible_text("Volvo")
            select.select_by_visible_text("Saab")
            select.select_by_visible_text("Opel")
            select.select_by_visible_text("Audi")
            return True
        except Exception as e:
            self.logger.error(f"Failed to select cars: {str(e)}")
            self._take_screenshot("standard_multi_error")
            raise