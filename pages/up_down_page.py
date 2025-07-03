from zoneinfo import reset_tzpath

from base.base_page import BasePage
from selenium.webdriver.common.by import By

class Up_Down_page(BasePage):

    download_button = (By.XPATH, "//a[@id='downloadButton']")
    upload_file_input = (By.XPATH,"//input[@id='uploadFile']")

    def click_download_button(self):
        try:
            self.click(self.download_button)
            self.logger.info("Download button clicked successfully")
            return True

        except Exception as e:
            self.logger.error(f"Error clicking download button: {str(e)}")
            return False

# ------------------------------------------------------------------------------------------------------------------------------
    def upload_file_to_page(self,file_path):
        try:
            result = self.upload_file(self.upload_file_input,file_path)
            if result:
                self.logger.info("File uploaded successfully")
                return True
            else:
                self.logger.info("Failed to upload file to page")
                return False

        except Exception as e:
            self.logger.info(f"Error uploading file to page: {str(e)} ")
            return False

# ------------------------------------------------------------------------------------------------------------------------------
    def verify_file_uploaded(self, filename):
        try:
            element = self.wait_for_element_visible(self.upload_file_input)
            current_value = element.get_attribute("value")

            # DEBUG: Nima ko'rinayotganini ko'rish
            print(f"DEBUG - Current text: '{current_value}'")
            print(f"DEBUG - Looking for: '{filename}'")

            if filename in current_value:
                self.logger.info(f"File {filename} verified successfully")
                return True
            else:
                self.logger.error(f"File {filename} not found. Found: '{current_value}'")
                return False
        except Exception as e:
            self.logger.error(f"Error verifying file upload: {str(e)}")
            return False
# ------------------------------------------------------------------------------------------------------------------------------
