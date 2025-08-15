from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DatePickerPage(BasePage):
    SELECT_DATE = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
    DATE_AND_TIME = (By.XPATH, "//input[@id='dateAndTimePickerInput']")
    MONTH_DROPDOWN = (By.CLASS_NAME, "react-datepicker__month-select")
    YEAR_DROPDOWN = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    DAY_CELL = (By.XPATH, "//div[contains(@class,'react-datepicker__day') and normalize-space()='{}']")

    def set_date_by_typing(self, date_text):
        element = self.wait_for_element_visible(self.SELECT_DATE)

        # Triple clear
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(date_text)
        element.send_keys(Keys.ESCAPE)  # ✅ Calendar ni yopadi
        # self.driver.find_element(By.TAG_NAME, "body").click() Buyam calendar ni yopadi faqat demoqadagi xpathda


    def set_date_by_calendar(self, day, month, year):
        self.click(self.SELECT_DATE)
        self.select_dropdown_by_text(self.MONTH_DROPDOWN, month)
        self.select_dropdown_by_text(self.YEAR_DROPDOWN,year)
        day_locator = (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and not(contains(@class, 'outside')) and normalize-space()='{day}']")
        self.click(day_locator)


    def set_date(self, date_value, method="typing", day=None, month=None, year=None):
        if method == "typing":
            return self.set_date_by_typing(date_value)
        else:
            return self.set_date_by_calendar(day,month,year)


#OTHER WAYS TO FILL PAGE:
# from base.base_page import BasePage
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# class DatePickerPage(BasePage):
#     SELECT_DATE = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
#     DATE_AND_TIME = (By.XPATH, "//input[@id='dateAndTimePickerInput']")
#     MONTH_DROPDOWN = (By.CLASS_NAME, "react-datepicker__month-select")
#     YEAR_DROPDOWN = (By.XPATH, "//select[@class='react-datepicker__year-select']")
#     DAY_CELL = (By.XPATH, "//div[contains(@class,'react-datepicker__day') and normalize-space()='{}']")
#
#     def set_date_by_typing(self, date_text):
#         element = self.wait_for_element_visible(self.SELECT_DATE)
#
#         # Triple clear
#         element.click()
#         element.send_keys(Keys.CONTROL + "a")  # Select all
#         element.send_keys(Keys.DELETE)  # Delete
#         element.send_keys(date_text)
#         element.send_keys(Keys.ESCAPE)  # ✅ Calendar ni yopadi
#         # self.driver.find_element(By.TAG_NAME, "body").click() Buyam calendar ni yopadi faqat demoqadagi xpathda
#
#
#     def set_date_by_calendar(self, day, month, year):
#         self.click(self.SELECT_DATE)
#         self.select_dropdown_by_text(self.MONTH_DROPDOWN, month)
#         self.select_dropdown_by_text(self.YEAR_DROPDOWN,year)
#         day_num = str(int(day))
#         day_locator = (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and normalize-space()='{day}']")
#         self.click(day_locator)
#
#
#     def set_date(self, date_value, method="typing", day=None, month=None, year=None):
#         if method == "typing":
#             return self.set_date_by_typing(date_value)
#         else:
#             return self.set_date_by_calendar(day,month,year)
