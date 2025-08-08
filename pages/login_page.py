from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    username_input = (By.XPATH, '//input[@id="userName"]')
    password_input = (By.XPATH, '//input[@id="password"]')
    login_button = (By.XPATH, '//button[@id="login"]')
    error_message = (By.XPATH, '//p[@id="name"]')

    def enter_username(self, username):
        self.input_text(self.username_input, username)

    def enter_password(self, password):
        self.input_text(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def get_error_message(self):
        return self.   get_text(self.error_message)