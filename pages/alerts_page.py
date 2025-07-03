# ================================================================================
# ALERTS PAGE OBJECT MODEL
# ================================================================================
# Bu file demoqa.com/alerts sahifasidagi barcha elementlar va funksiyalarni
# boshqarish uchun yaratilgan. Page Object Model pattern ishlatilgan.


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
    # ================================================================================
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
    # SIMPLE ALERT METHODS - Oddiy alert bilan ishlash
    # ================================================================================
    def click_simple_alert_button(self):
        """
         Simple alert button'ini bosadi
         Bu button bosilganda oddiy alert dialog chiqadi
         """
        self.click(self.SIMPLE_ALERT_BUTTON)

    def handle_simple_alert(self):
        """
         Simple alert'ni handle qiladi (OK tugmasini bosadi)
         Alert chiqgandan keyin uni yopish uchun ishlatiladi   ?????????
         """
        alert = self.driver.switch_to.alert# Alert'ga switch qilish
        alert.accept()# OK button bosish
# ---------------------------------------------------------------------------------------------------------------------


    # ================================================================================
    # TIMER ALERT METHODS - 5 soniyalik timer alert bilan ishlash
    # ================================================================================
    def click_timer_alert_button(self):
        """
        Timer alert button'ini bosadi
        Bu button bosilgandan 5 soniya keyin alert chiqadi
        """
        self.click(self.TIMER_ALERT_BUTTON)

    def handle_timer_alert(self):
        """
        Timer alert'ni handle qiladi
        5 soniya kutib, alert chiqgandan keyin uni yopadi
        WebDriverWait ishlatilgan - alert chiqishini kutish uchun
        """
        # 6 soniya ichida alert chiqishini kutadi (5 soniya + 1 soniya buffer)
        alert = WebDriverWait(self.driver, 6).until(EC.alert_is_present())
        alert.accept()

# ------------------------------------------------------------------------------------------------------------------------------
    def click_confirm_button(self):
        """
        Confirm alert button'ini bosadi
        Bu button bosilganda OK/Cancel tanlov bilan dialog chiqadi
        """
        self.click(self.CONFIRM_BUTTON)

    def get_confirm_result_text(self):
        """
        Confirm alert natijasini oladi
        Confirm dialog'da OK yoki Cancel bosilgandan keyin
        sahifada result text chiqadi - uni o'qiydi
        Returns:
        str: Result text ("You selected Ok" yoki "You selected Cancel")
                """
        return self.get_text(self.CONFIRM_RESULT)

    def handle_confirm_alert_accept(self):
        """
        Confirm alert'da OK tugmasini bosadi
        OK bosilganda "You selected Ok" message chiqadi
        """
        alert = self.driver.switch_to.alert
        alert.accept()# OK tugmasini bosish

    def handle_confirm_alert_dismiss(self):
        """
        Confirm alert'da Cancel tugmasini bosadi
        Cancel bosilganda "You selected Cancel" message chiqadi
                """
        alert = self.driver.switch_to.alert
        alert.dismiss()
# ------------------------------------------------------------------------------------------------------------------------------
    # ================================================================================
    # PROMPT ALERT METHODS - Text input bilan alert'lar uchun
    # ================================================================================

    def click_prompt_button(self):
        """
        Prompt alert button'ini bosadi
        Bu button bosilganda text input field'i bilan dialog chiqadi
        """
        self.click(self.PROMPT_BUTTON)

    def get_prompt_result_text(self):
        """
        Prompt alert natijasini oladi
        Prompt dialog'da text kiritib OK bosilgandan keyin
        sahifada "You entered [text]" message chiqadi - uni o'qiydi
        Returns:
        str: Result text ("You entered [kiritilgan_text]")
                """
        return self.get_text(self.PROMPT_RESULT)

    def handle_prompt_alert(self, text):
        """Prompt alert'ga text kiritib OK tugmasini bosadi
        Args:
        text (str): Alert'ga kiritilishi kerak bo'lgan text
        Example:
        handle_prompt_alert("John Doe")  # "John Doe" textini kiritadi
        """
        alert = self.driver.switch_to.alert
        alert.send_keys(text)# Text kiritish
        alert.accept()# OK tugmasini bosish
