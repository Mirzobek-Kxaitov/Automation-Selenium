from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Practice_form(BasePage):
    Name = (By.XPATH,"//input[@id='firstName']")
    Last_name = (By.XPATH, "//input[@id='lastName']")
    Email =(By.XPATH, "//input[@id='userEmail']")
    Radiobutton_other = (By.XPATH, "//label[@for='gender-radio-3']")
    Radiobutton_female = (By.XPATH, "//label[@for='gender-radio-2']")
    Radiobutton_male = (By.XPATH, "//label[@for='gender-radio-1']")
    Mobile  = (By.XPATH, "//input[@id='userNumber']")
    Date_of_birth = (By.XPATH, "//input[@id='dateOfBirthInput']")
    Subjects =(By.XPATH, "//input[@id='subjectsInput']")
    Sport_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    Reading_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    Music_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-3']")
    Upload_picture = (By.XPATH, "//input[@type='file']")
    Current_address = (By.XPATH, "//textarea[@placeholder='Current Address']")

    State_and_city = (By.XPATH, "//div[contains(text(), 'Select State')]")
    State_ncr = (By.XPATH, "//div[@id='react-select-20-option-0']")
    State_uttar_pradesh = (By.XPATH, "//div[text()='Uttar Pradesh']")
    State_haryana = (By.XPATH, "//div[text()='Haryana']")
    State_rajasthan = (By.XPATH, "//div[text()='Rajasthan']")

    Select_sity = (By.XPATH, "//div[contains(text(), 'Select City')]")
    Agra_city = (By.XPATH, "//div[@id='react-select-4-option-0']")
    Lucknow = (By.XPATH, "//div[@id='react-select-4-option-1']")
    Merrut = (By.XPATH, "//div[@id='react-select-4-option-2']")

    submit_button = (By.XPATH, "//button[@id='submit']")

    def fill_first_name(self,name):
        self.input_text(self.Name,name)

    def fill_last_name(self,last_name):
        self.input_text(self.Last_name,last_name)

    def fill_email(self,email):
        self.input_text(self.Email,email)

    def select_female_gender(self):
        self.click(self.Radiobutton_female)

    def select_male_gender(self):
        self.click(self.Radiobutton_male)

    def select_other_gender(self):
        self.click(self.Radiobutton_other)

    def fill_mobile(self,mobile):
        self.input_text(self.Mobile,mobile)

    def fill_date_of_birth(self,date):
        element = self.wait_for_element_visible(self.Date_of_birth)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(date)
        element.send_keys(Keys.ESCAPE)


    def fill_subject(self,subject):
        element = self.wait_for_element_visible(self.Subjects)
        element.click()
        element.send_keys(subject)
        element.send_keys(Keys.ENTER)

    def select_sports_hobby(self):
        self.click(self.Sport_checkbox)

    def select_reading_hobby(self):
        self.click(self.Reading_checkbox)

    def select_music_hobby(self):
        self.click(self.Music_checkbox)

    def upload_picture(self,file_path):
        try:
            upload_element = self.wait_for_element_visible(self.Upload_picture)
            upload_element.send_keys(file_path)
            self.logger.info(f"File uploaded {file_path}")
            return True

        except Exception as e:
            self.logger.error(f"Upload error {file_path}")
            return False

    def fill_current_address(self,current_address):
        self.input_text(self.Current_address,current_address)

    def select_state(self, state_locator):
        self.click(self.State_and_city)
        self.wait_for_element_visible(state_locator)
        self.click(state_locator)

    def select_state_uttar_pradesh(self):
        self.select_state(self.State_uttar_pradesh)

    def select_state_haryana(self):
        self.select_state(self.State_haryana)

    def select_state_rajasthan(self):
        self.select_state(self.State_rajasthan)

    def select_city(self, city_locator):
        self.click(self.Select_sity)
        self.wait_for_element_visible(city_locator)
        self.click(city_locator)

    def select_city_agra(self):
        self.select_city(self.Agra_city)

    def select_city_lucknow(self):
        self.select_city(self.Lucknow)

    def select_city_merrut(self):
        self.select_city(self.Merrut)

    def submit_form(self):
        self.click(self.submit_button)

    def verify_submitted_data(self, first_name, last_name, email, gender, mobile,
                              date_of_birth, subjects, hobbies, address, state, city):
        """Barcha submit qilingan ma'lumotlarni tekshirish"""

        # Student Name
        name_element = self.get_text((By.XPATH, "//td[text()='Student Name']//following-sibling::td"))
        expected_name = f"{first_name} {last_name}"
        assert expected_name in name_element, f"Name mismatch: expected {expected_name}, got {name_element}"

        # Student Email
        email_element = self.get_text((By.XPATH, "//td[text()='Student Email']//following-sibling::td"))
        assert email in email_element, f"Email mismatch: expected {email}, got {email_element}"

        # Gender
        gender_element = self.get_text((By.XPATH, "//td[text()='Gender']//following-sibling::td"))
        assert gender in gender_element, f"Gender mismatch: expected {gender}, got {gender_element}"

        # Mobile
        mobile_element = self.get_text((By.XPATH, "//td[text()='Mobile']//following-sibling::td"))
        assert mobile in mobile_element, f"Mobile mismatch: expected {mobile}, got {mobile_element}"

        # Date of Birth
        dob_element = self.get_text((By.XPATH, "//td[text()='Date of Birth']//following-sibling::td"))
        assert date_of_birth in dob_element, f"DOB mismatch: expected {date_of_birth}, got {dob_element}"

        # Subjects
        subjects_element = self.get_text((By.XPATH, "//td[text()='Subjects']//following-sibling::td"))
        assert subjects in subjects_element, f"Subjects mismatch: expected {subjects}, got {subjects_element}"

        # Hobbies
        hobbies_element = self.get_text((By.XPATH, "//td[text()='Hobbies']//following-sibling::td"))
        assert hobbies in hobbies_element, f"Hobbies mismatch: expected {hobbies}, got {hobbies_element}"

        # Address
        address_element = self.get_text((By.XPATH, "//td[text()='Address']//following-sibling::td"))
        assert address in address_element, f"Address mismatch: expected {address}, got {address_element}"

        # State and City
        state_city_element = self.get_text((By.XPATH, "//td[text()='State and City']//following-sibling::td"))
        expected_state_city = f"{state} {city}"
        assert expected_state_city in state_city_element, f"State/City mismatch: expected {expected_state_city}, got {state_city_element}"

        self.logger.info("All submitted data verified successfully!")
        return True
