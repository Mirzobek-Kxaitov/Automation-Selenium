from selenium.webdriver.common.by import By
from base.base_page import BasePage

class Selectable_Page(BasePage):
    FIRST_LIST = (By.XPATH, "(//li[contains(@class,'list-group-item')])[1]")
    SECOND_LIST = (By.XPATH, "(//li[contains(@class,'list-group-item')])[2]")
    THIRD_LIST = (By.XPATH, "(//li[contains(@class,'list-group-item')])[3]")
    FOURTH_LIST = (By.XPATH,"(//li[contains(@class,'list-group-item')])[4]")

    GRID_TAB = (By.XPATH, "//a[text()='Grid']")
    SELECT_ONE = (By.XPATH, "//div[@id='row1']//li[text()='One']")
    SELECT_TWO = (By.XPATH, "//div[@id='row1']//li[text()='Two']")
    SELECT_THREE = (By.XPATH, "//div[@id='row1']//li[text()='Three']")
    SELECT_FOUR = (By.XPATH, "//div[@id='row2']//li[text()='Four']")
    SELECT_FIVE = (By.XPATH, "//div[@id='row2']//li[text()='Five']")
    SELECT_SIX = (By.XPATH, "//div[@id='row2']//li[text()='Six']")
    SELECT_SEVEN = (By.XPATH, "//div[@id='row3']//li[text()='Seven']")
    SELECT_EIGHT = (By.XPATH, "//div[@id='row3']//li[text()='Eight']")
    SELECT_NINE = (By.XPATH, "//div[@id='row3']//li[text()='Nine']")


    def click_vertical_list(self, index):
        locator = (By.XPATH, f"(//li[contains(@class,'list-group-item')])[{index}]")
        self.click(locator)

    def is_vertical_item_selected(self, index):
        """
        Checks whether a given list item (by index) is selected (has 'active' class)
        """
        locator = (By.XPATH, f"(//li[contains(@class,'list-group-item')])[{index}]")
        element = self.wait_for_element_visible(locator)
        return "active" in element.get_attribute("class")

    def click_grid_button(self):
        self.click(self.GRID_TAB)
        self.wait_for_element_visible((By.XPATH, "//div[@id='row1']//li"))

    def is_grid_item_selected(self, row, col):
        locator = (By.XPATH, f"//div[@id='row{row}']//li[{col}]")
        element = self.wait_for_element_visible(locator)
        return "active" in element.get_attribute("class")
