from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Buttons_page(BasePage):

    double_click_button = (By.XPATH, "//button[@id='doubleClickBtn']")
    def double_click_button_action(self):
        element = self.driver.find_element(*self.double_click_button)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    right_click_button = (By.XPATH,"//button[@id='rightClickBtn']")
    def right_click_button_action(self):
        element = self.driver.find_element(*self.right_click_button)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    simple_click_button = (By.XPATH, "//button[text()='Click Me']")
    def simple_click_button_action(self):
        element = self.driver.find_element(*self.simple_click_button)
        actions = ActionChains(self.driver)
        actions.click(element).perform()