from base.base_page import BasePage
from selenium.webdriver.common.by import By

class Accordian_page(BasePage):
    FIRST_ACCORDION = (By.XPATH, "//div[@id='section1Heading']")
    SECOND_ACCORDION = (By.XPATH, "//div[@id='section2Heading']")
    THIRD_ACCORDION = (By.XPATH, "//div[@id='section3Heading']")

    FIRST_CONTENT = (By.ID, "section1Content")
    SECOND_CONTENT = (By.ID, "section2Content")
    THIRD_CONTENT = (By.ID, "section3Content")

    def click_first_accordion(self):
        self.click(self.FIRST_ACCORDION)

    def click_second_accordion(self):
        self.click(self.SECOND_ACCORDION)

    def click_third_accordion(self):
        self.click(self.THIRD_ACCORDION)

    def is_first_content_visible(self):
        try:
            self.wait_for_element_visible(self.FIRST_CONTENT)
            return True
        except:
            return False

    def is_second_content_visible(self):
        try:
            self.wait_for_element_visible(self.SECOND_CONTENT)
            return True
        except:
            return False

    def is_third_content_visible(self):
        try:
            self.wait_for_element_visible(self.THIRD_CONTENT)
            return True
        except:
            return False

    def get_first_content_text(self):
        return self.get_text(self.FIRST_CONTENT)
    def get_second_content_text(self):
        return self.get_text(self.SECOND_CONTENT)
    def get_third_content_text(self):
        return self.get_text(self.THIRD_CONTENT)





