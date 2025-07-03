from base.base_page import BasePage
from selenium.webdriver.common.by import By

class Web_tables_page(BasePage):

    add_button = (By.XPATH, "//button[@id='addNewRecordButton']")
    def click_add_button(self):
        self.click(self.add_button)

    first_name = (By.XPATH, "//input[@id='firstName']")
    def fill_first_name(self, name):
        element = self.driver.find_element(*self.first_name)
        element.clear()
        element.send_keys(name)

    last_name=(By.XPATH,"//input[@id='lastName']")
    def fill_last_name(self,name):
        element = self.driver.find_element(*self.last_name)
        element.clear()
        element.send_keys(name)


    email = (By.XPATH,"//input[@id='userEmail']")
    def fill_email(self,mail):
        element = self.driver.find_element(*self.email)
        element.clear()
        element.send_keys(mail)

    age = (By.XPATH,"//input[@id='age']")
    def fill_age(self,age):
        element = self.driver.find_element(*self.age)
        element.clear()
        element.send_keys(age)


    salary= (By.XPATH, "//input[@id='salary']")
    def fill_salary(self,salary):
        element = self.driver.find_element(*self.salary)
        element.clear()
        element.send_keys(salary)


    department= (By.XPATH,"//input[@id='department']")
    def fill_department(self,department):
        element = self.driver.find_element(*self.department)
        element.clear()
        element.send_keys(department)

    submit_button = (By.XPATH, "//button[@id='submit']")
    def click_submit_button(self):
       element = self.driver.find_element(*self.submit_button)
       element.click()

    def verify_record_added(self, first_name, last_name):
        assert first_name in self.driver.page_source
        assert last_name in self.driver.page_source

    search_text = (By.XPATH, "//input[@id='searchBox']")
    def search_in_table(self,search_text):
        element = self.driver.find_element(*self.search_text)
        element.send_keys(search_text)

    def verify_search_result(self, search_text):
        # Table da faqat search qilingan ma'lumot ko'rinishini tekshirish
        assert search_text in self.driver.page_source

    edit_button = (By.XPATH,"//span[@id='edit-record-2']")
    def click_edit_button(self):
        self.click(self.edit_button)

    def verify_record_edited(self, first_name, last_name):
        assert first_name in self.driver.page_source
        assert last_name in self.driver.page_source

    delete_button =(By.XPATH, "//span[@id='delete-record-3']")
    def click_delete_button(self):
        self.click(self.delete_button)

    def verify_record_deleted(self, first_name):
        # Bu ma'lumotlar tableda YO'Q ekanligini tekshirish
        assert first_name not in self.driver.page_source  # "not in" - YO'Q
