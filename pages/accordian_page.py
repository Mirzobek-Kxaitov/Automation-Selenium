from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class Accordian_page(BasePage):
    FIRST_ACCORDION = (By.XPATH, "//div[@id='section1Heading']")
    SECOND_ACCORDION = (By.XPATH, "//div[@id='section2Heading']")
    THIRD_ACCORDION = (By.XPATH, "//div[@id='section3Heading']")

    FIRST_CONTENT_LOCATOR = (By.ID, "section1Content")
    SECOND_CONTENT_LOCATOR = (By.ID, "section2Content")
    THIRD_CONTENT_LOCATOR = (By.ID, "section3Content")

    def click_first_accordion(self):
        self.click(self.FIRST_ACCORDION)
        self.wait_for_element_visible(self.FIRST_CONTENT_LOCATOR)  # Wait for content

    def click_second_accordion(self):
        self.click(self.SECOND_ACCORDION)
        self.wait_for_element_visible(self.SECOND_CONTENT_LOCATOR)  # Wait for content

    def click_third_accordion(self):
        self.click(self.THIRD_ACCORDION)
        self.wait_for_element_visible(self.THIRD_CONTENT_LOCATOR)  # Wait for content

# githubda run qilish

    def is_first_content_visible(self):
        try:
            self.wait_for_element_visible(self.FIRST_CONTENT_LOCATOR)
            return True
        except:
            return False

    def is_second_content_visible(self):
        try:
            self.wait_for_element_visible(self.SECOND_CONTENT_LOCATOR)
            return True
        except:
            return False

    def is_third_content_visible(self):
        try:
            self.wait_for_element_visible(self.THIRD_CONTENT_LOCATOR)
            return True
        except:
            return False

    def get_first_content_text(self):
        return self.get_text(self.FIRST_CONTENT_LOCATOR)

    def get_second_content_text(self):
        return self.get_text(self.SECOND_CONTENT_LOCATOR)

    def get_third_content_text(self):
        return self.get_text(self.THIRD_CONTENT_LOCATOR)

    def wait_for_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def close_other_accordions(self):
        """Boshqa accordionlarni yopish"""
        if self.is_first_content_visible():
            self.click(self.FIRST_ACCORDION)  # Birinchi accordionni yopish
        if self.is_second_content_visible():
            self.click(self.SECOND_ACCORDION)  # Ikkinchi accordionni yopish


#Accordion elementlari bir-birini o‘zgartirishga (ya'ni, bitta ochilganda boshqasi yopilishi kerak) moslashgan. Demak, bir accordionni bosganingizda, boshqa accordion bo‘limlarini yopish kerak.
# Accordion bo‘limlari bir-birini yopish uchun quyidagi yondashuvni qo‘llash mumkin:
# Accordionni bosgandan keyin, faqatgina shu bo‘limning ochilganligini tekshirish.
# Boshqa bo‘limlarning yopilishini tekshirish.
# Kodni tuzatish
# Accordian_page sinfida yuqoridagi metodni qo‘shish kerak: