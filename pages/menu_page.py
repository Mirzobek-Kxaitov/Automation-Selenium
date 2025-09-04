# pages/menu_page.py - BUTUNLAY ALMASHTIRING

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class MenuPage(BasePage):
    # Lokatorlar
    MAIN_ITEM_1 = (By.CSS_SELECTOR, '#nav > li:nth-child(1) > a')
    MAIN_ITEM_2 = (By.CSS_SELECTOR, '#nav > li:nth-child(2) > a')
    MAIN_ITEM_3 = (By.CSS_SELECTOR, '#nav > li:nth-child(3) > a')
    SUB_ITEM_1 = (By.CSS_SELECTOR, '#nav > li:nth-child(2) > ul > li:nth-child(1) > a')
    SUB_ITEM_2 = (By.CSS_SELECTOR, '#nav > li:nth-child(2) > ul > li:nth-child(2) > a')
    SUB_SUB_LIST = (By.CSS_SELECTOR, '#nav > li:nth-child(2) > ul > li:nth-child(3) > a')
    SUB_SUB_ITEM_1 = (By.CSS_SELECTOR, '#nav > li:nth-child(2) > ul > li:nth-child(3) > ul > li:nth-child(1) > a')
    SUB_SUB_ITEM_2 = (By.CSS_SELECTOR, '#nav > li:nth-child(2) > ul > li:nth-child(3) > ul > li:nth-child(2) > a')
    PAGE_HEADER = (By.CLASS_NAME, 'main-header')
    PAGE_FOOTER = (By.TAG_NAME, 'footer')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/menu"

    def open(self):
        self.driver.get(self.url)
        self.logger.info(f"Opened page: {self.url}")

    def hover_element(self, locator):
        try:
            element = self.wait_for_element_visible(locator)
            self._scroll_to_element(element)
            ActionChains(self.driver).move_to_element(element).perform()
            import time
            time.sleep(0.3)  # CSS transition uchun
            self.logger.info(f"Successfully hovered over element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to hover over element {locator}: {str(e)}")
            self._take_screenshot("hover_error")
            raise

    def is_element_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            is_visible = element.is_displayed()
            self.logger.info(f"Element {locator} visibility: {is_visible}")
            return is_visible
        except:
            self.logger.info(f"Element {locator} not found")
            return False