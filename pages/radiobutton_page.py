from selenium.webdriver.common.by import By
from base.base_page import BasePage

class Radiobutton_page(BasePage):

    radiobutton_yes = (By.XPATH,"//label[@for='yesRadio']")
    def click_radiobutton(self):
        self.click(self.radiobutton_yes)
        self.logger.info(" Clicked on the 'Impressive' radio button.")

    radiobutton_imp = (By.XPATH,"//label[@for='impressiveRadio']")
    def click_radiobutton_imp(self):
        self.click(self.radiobutton_imp)
        self.logger.info(" Clicked on the 'Yes' radio button.")

    radiobutton_no = (By.ID, "noRadio")
    def is_radiobutton_no_disabled(self):
        return self.driver.find_element(*self.radiobutton_no).get_attribute("disabled") == "true"

        if disabled:
            self.logger.info("  The 'No' radio button is disabled as expected.")
        else:
            self.logger.warning("  The 'No' radio button is enabled, which is unexpected.")
        return disabled