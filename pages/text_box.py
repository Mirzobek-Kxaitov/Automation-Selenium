from selenium.webdriver.common.by import By
from base.base_page import BasePage

class TexBoxPage(BasePage):
    # ------------------------------------------------------------------------------------------------------------------
    user_name_input = (By.XPATH, '//input[@id="userName"]')

    def enter_user_name(self, user_name):
        self.input_text(self.user_name_input, user_name)
    # ------------------------------------------------------------------------------------------------------------------
    user_email_input = (By.XPATH, '//input[@id="userEmail"]')

    def enter_user_email(self, user_email):
        self.input_text(self.user_email_input, user_email)
    # ------------------------------------------------------------------------------------------------------------------

    current_address_input = (By.XPATH,"//*[@id='currentAddress']")
    def enter_current_address(self, current_adress):
       self.input_text(self.current_address_input, current_adress)
    # ------------------------------------------------------------------------------------------------------------------

    permanent_address_input = (By.XPATH, "//*[@id='permanentAddress']")

    def enter_permanent_address(self, permanent_adress):
       self.input_text(self.permanent_address_input, permanent_adress)

    # ------------------------------------------------------------------------------------------------------------------

    submit_button = (By.XPATH, '//button[@id="submit"]')

    def click_submit_button(self):
        self.click(self.submit_button)
    # ---------------------------------------------------------------------------------------------------------------
    #######    verify text
    def get_output_name(self):
        return self.get_text((By.ID, "name"))

    def get_output_email(self):
        return self.get_text((By.ID, "email"))

    def get_output_current_address(self):
        return self.get_text((By.XPATH, '//p[@id="currentAddress"]'))

    def get_output_permanent_address(self):
        return self.get_text((By.XPATH, '//p[@id="permanentAddress"]'))