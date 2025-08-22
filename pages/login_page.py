# pages/login_page.py

from selenium.webdriver.common.by import By
from base.base_page import BasePage
class LoginPage(BasePage):
    # Lokatorlar yanada samarali bo'lgan By.ID ga o'zgartirildi
    username_input = (By.ID, 'userName')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'login')
    error_message = (By.ID, 'name')

    def __init__(self, driver):
        super().__init__(driver)
        # Login sahifasining to'g'ri URL manzili
        self.url = "https://demoqa.com/login"

    def open(self):
        """Sahifani ochadi"""
        self.driver.get(self.url)

    def enter_username(self, username):
        """Foydalanuvchi nomini kiritish"""
        self.input_text(self.username_input, username)

    def enter_password(self, password):
        """Parolni kiritish"""
        self.input_text(self.password_input, password)

    def click_login(self):
        """Login tugmasini bosish"""
        self.click(self.login_button)

    def login(self, username, password):
        """To'liq login jarayonini amalga oshiradi"""
        self.logger.info(f"Attempting to log in with username: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Xatolik xabarini olish uchun metod"""
        # Element ko'rinadigan bo'lishini kutamiz va keyin matnni olamiz
        self.wait_for_element_visible(self.error_message)
        return self.get_text(self.error_message)