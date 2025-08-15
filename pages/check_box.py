from selenium.webdriver.common.by import By
from base.base_page import BasePage

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class Check_box_page(BasePage):
    main_toggle_button = (By.CSS_SELECTOR, "button.rct-collapse.rct-collapse-btn")
    # Har bir papka/fayl oldidagi o'chirish/yoqish tugmasi
    home_checkbox = (By.CSS_SELECTOR, "label[for='tree-node-home'] span.rct-checkbox")
    desktop_checkbox = (By.CSS_SELECTOR, "label[for='tree-node-desktop'] span.rct-checkbox")
    documents_checkbox = (By.CSS_SELECTOR, "label[for='tree-node-documents'] span.rct-checkbox")
    downloads_checkbox = (By.CSS_SELECTOR, "label[for='tree-node-downloads'] span.rct-checkbox")

    result_text = (By.ID, "result")

    def __init__(self, driver):
        super().__init__(driver)

    def toggle_node(self, node_name):
        """Berilgan tugunni ochish yoki yopish uchun toggle tugmasini bosadi."""
        locator = (By.XPATH, f"//label[@for='tree-node-{node_name}']//button[@aria-label='Toggle']")
        self.click(locator)

    def select_checkbox(self, checkbox_name):
        """Berilgan nomdagi checkboxni tanlaydi yoki bekor qiladi."""
        locator = (By.XPATH, f"//label[@for='tree-node-{checkbox_name}']")
        self.click(locator)

    def get_selected_items_text(self):
        """Natija qutisidagi tanlangan elementlarning matnini oladi."""
        result_locator = (By.ID, "result")
        return self.get_text(result_locator)

# OTHER WAYS - CLICK EVERYTHING
#
# from selenium.webdriver.common.by import By
# from base.base_page import BasePage
#
# class Check_box_page(BasePage):
#
#     check_box_button = (By.CSS_SELECTOR, "button.rct-collapse.rct-collapse-btn")
#     def click_check_box(self):
#         self.click(self.check_box_button)
#
#     ch_b_desktop_button = (By.XPATH, "(//button[@aria-label='Toggle'])[2]")
#     def click_check_box_d_b(self):
#         self.click(self.ch_b_desktop_button)
#
#     ch_b_documents_button = (By.XPATH, "(//button[@aria-label='Toggle'])[3]")
#     def click_check_box_doc_button(self):
#         self.click(self.ch_b_documents_button)
#
#     ch_b_downloads_button = (By.XPATH, "(//button[@aria-label='Toggle'])[4]")
#     def click_check_box_download_button(self):
#         self.click(self.ch_b_downloads_button)
#
#     ch_b_button_one = (By.XPATH, "//label[@for='tree-node-desktop']")
#     def click_button_one(self):
#         self.click(self.ch_b_button_one)
#
#     ch_b_button_two = (By.XPATH, "//label[@for='tree-node-documents']")
#     def click_button_two(self):
#         self.click(self.ch_b_button_two)
#
#     ch_b_button_three = (By.XPATH, "//label[@for='tree-node-downloads']")
#     def click_button_three(self):
#         self.click(self.ch_b_button_three)
#




























#
# class Check_box_page(BasePage):
#
#     check_box_button = (By.CSS_SELECTOR, "button.rct-collapse.rct-collapse-btn")
#     def click_check_box(self):
#         self.click(self.check_box_button)
#
#     ch_b_desktop_button = (By.XPATH, "(//button[@aria-label='Toggle'])[2]")
#     def click_check_box_d_b(self):
#         self.click(self.ch_b_desktop_button)
#
#     ch_b_documents_button = (By.XPATH, "(//button[@aria-label='Toggle'])[3]")
#     def click_check_box_doc_button(self):
#         self.click(self.ch_b_documents_button)
#
#     ch_b_downloads_button = (By.XPATH, "(//button[@aria-label='Toggle'])[4]")
#     def click_check_box_download_button(self):
#         self.click(self.ch_b_downloads_button)
#
#     ch_b_button_one = (By.XPATH, "//label[@for='tree-node-desktop']")
#     def click_button_one(self):
#         self.click(self.ch_b_button_one)
#
#     ch_b_button_two = (By.XPATH, "//label[@for='tree-node-documents']")
#     def click_button_two(self):
#         self.click(self.ch_b_button_two)
#
#     ch_b_button_three = (By.XPATH, "//label[@for='tree-node-downloads']")
#     def click_button_three(self):
#         self.click(self.ch_b_button_three)
#

