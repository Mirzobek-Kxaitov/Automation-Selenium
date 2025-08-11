from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Alerts_page(BasePage):
    """
    Alerts sahifasi uchun Page Object class

    Bu class 4 xil alert bilan ishlash uchun yaratilgan:
    1. Simple Alert - oddiy alert dialog
    2. Timer Alert - 5 soniyadan keyin chiqadigan alert
    3. Confirm Alert - OK/Cancel tanlov bilan alert
    4. Prompt Alert - text input bilan alert
    """
    # LOCATORS - Sahifadagi barcha elementlarning joylashuvini belgilaydi
    # ================================================================================

    # Alert button'lari uchun locator'lar
    SIMPLE_ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']") # "Click Button to see alert" button
    TIMER_ALERT_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")# "5 second timer alert" button
    CONFIRM_BUTTON = (By.XPATH, "//button[@id='confirmButton']")# "Confirm box" button
    CONFIRM_RESULT = (By.ID, "confirmResult") # Confirm alert natijasi ("You selected Ok/Cancel")
    PROMPT_BUTTON = (By.XPATH, "//button[@id='promtButton']") # "Prompt box" button (typo HTML'da)
    PROMPT_RESULT = (By.ID, "promptResult")# Prompt alert natijasi ("You entered XYZ")
 # --------------------------------------------------------------------------------------------------------------------


    # ================================================================================
    def click_simple_alert_button(self):
        self.click(self.SIMPLE_ALERT_BUTTON)

    def handle_simple_alert(self):#ozgarish
        alert = self.wait.until(EC.alert_is_present())
        _ = alert.text  # xohlasangiz logga yozing
        alert.accept()
        self.last_result_text = "Alert accepted"
# ---------------------------------------------------------------------------------------------------------------------

    def click_timer_alert_button(self):
        self.click(self.TIMER_ALERT_BUTTON)

    def handle_timer_alert(self):
        # 5s dan keyin chiqadi, 6s kifoya
        alert = WebDriverWait(self.driver, 6).until(EC.alert_is_present())
        _ = alert.text
        alert.accept()
        self.last_result_text = "Alert after 5 seconds"
# ------------------------------------------------------------------------------------------------------------------------------
    def click_confirm_button(self):
        self.click(self.CONFIRM_BUTTON)

    def get_confirm_result_text(self):
        return self.get_text(self.CONFIRM_RESULT)

    def handle_confirm_alert_accept(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        text = self.wait.until(EC.visibility_of_element_located(self.CONFIRM_RESULT)).text
        self.last_result_text = text  # "You selected Ok"

    def handle_confirm_alert_dismiss(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()
        text = self.wait.until(EC.visibility_of_element_located(self.CONFIRM_RESULT)).text
        self.last_result_text = text  # "You selected Cancel"
# ------------------------------------------------------------------------------------------------------------------------------

    def click_prompt_button(self):
        self.click(self.PROMPT_BUTTON)

    def get_prompt_result_text(self):
        return self.get_text(self.PROMPT_RESULT)

    def handle_prompt_alert(self, text):
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)
        alert.accept()
        text = self.wait.until(EC.visibility_of_element_located(self.PROMPT_RESULT)).text
        self.last_result_text = text  # "You entered Test User"

    def get_alert_result_text(self):
        return self.last_result_text

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.last_result_text = None