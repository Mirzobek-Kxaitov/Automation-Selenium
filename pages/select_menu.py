from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support.ui import Select


class Select_Menu_Page(BasePage):
    SELECT_VALUE = (By.XPATH,'//div[@id="withOptGroup"]')
    GROUP_1_OPTION_1 = (By.XPATH, "//div[text()='Group 1, option 1']")
    GROUP_1_OPTION_2 = (By.XPATH, "//div[text()='Group 1, option 2']")
    GROUP_2_OPTION_1 = (By.XPATH, "//div[text()='Group 2, option 1']")
    GROUP_2_OPTION_2 = (By.XPATH, "//div[text()='Group 2, option 2']")
    A_ROOT_OPTION = (By.XPATH, "//div[text()='A root option']")
    ANOTHER_ROOT_OPTION = (By.XPATH, "//div[text()='Another root option']")

    SELECT_ONE = (By.XPATH, '//div[@id="selectOne"]')
    TITLE_DR = (By.XPATH, '//div[@id="react-select-11-option-0-0"]')
    TITLE_MR = (By.XPATH, '//div[@id="react-select-11-option-0-1"]')
    TITLE_MRS = (By.XPATH, '//div[@id="react-select-11-option-0-2"]')
    TITLE_MS = (By.XPATH, '//div[@id="react-select-11-option-0-3"]')
    TITLE_PROF = (By.XPATH, '//div[@id="react-select-11-option-0-4"]')
    TITLE_OTHER = (By.XPATH, '//div[@id="react-select-11-option-0-5"]')



    OLD_SELECT_MENU = (By.XPATH, "//select[@id='oldSelectMenu']")
    MULTISELECT_DROP_DOWN = (By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div[1]/div[1]')

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



    def select_one_option(self):
        try:
            self.click(self.SELECT_ONE)
            self.click(self.TITLE_DR)
            self.logger.info(f"Successfully selected Dr")
        except Exception as e:
            self.logger.error(f"Failed to select option: {str(e)}")
            self._take_screenshot("select_value_error")
            raise