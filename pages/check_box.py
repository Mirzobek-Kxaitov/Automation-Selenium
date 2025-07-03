from selenium.webdriver.common.by import By
from base.base_page import BasePage

class Check_box_page(BasePage):

    check_box_button = (By.CSS_SELECTOR, "button.rct-collapse.rct-collapse-btn")
    def click_check_box(self):
        self.click(self.check_box_button)

    ch_b_desktop_button = (By.XPATH, "(//button[@aria-label='Toggle'])[2]")
    def click_check_box_d_b(self):
        self.click(self.ch_b_desktop_button)

    ch_b_documents_button = (By.XPATH, "(//button[@aria-label='Toggle'])[3]")
    def click_check_box_doc_button(self):
        self.click(self.ch_b_documents_button)

    ch_b_downloads_button = (By.XPATH, "(//button[@aria-label='Toggle'])[4]")
    def click_check_box_download_button(self):
        self.click(self.ch_b_downloads_button)

    ch_b_button_one = (By.XPATH, "//label[@for='tree-node-desktop']")
    def click_button_one(self):
        self.click(self.ch_b_button_one)

    ch_b_button_two = (By.XPATH, "//label[@for='tree-node-documents']")
    def click_button_two(self):
        self.click(self.ch_b_button_two)

    ch_b_button_three = (By.XPATH, "//label[@for='tree-node-downloads']")
    def click_button_three(self):
        self.click(self.ch_b_button_three)


