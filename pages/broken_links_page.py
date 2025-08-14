from base.base_page import BasePage
from selenium.webdriver.common.by import By


class Broken_list_page(BasePage):

    valid_image = (By.XPATH,"(//img[contains(@src, 'Toolsqa.jpg')])[2]")
    broken_image = (By.XPATH, "//img[contains(@src, 'Toolsqa_1.jpg')]")
    valid_link = (By.XPATH, "//a[text()='Click Here for Valid Link']")
    broken_link = (By.XPATH, "//a[text()='Click Here for Broken Link']")
# ------------------------------------------------------------------------------------------------------------------------------
    def verify_valid_image(self):
        try:
            image = self.wait_for_element_visible(self.valid_image)
            width = image.get_attribute("naturalWidth")
            height = image.get_attribute("naturalHeight")
            self.logger.info(f"Image width: {width}, height: {height}")

            if int(width) > 0 and int(height) > 0:
                self.logger.info("Valid image is loaded successfully")
                return True #test passed
            else: #unday bo'masa
                self.logger.error("Valid image failed to load") #logda chiqadi
                return False #test failed


        except Exception as e:# ← Agar yuqorida XATOLIK bo'lsa
            self.logger.error(f"Error checking valid image: {str(e)}")
            return False
# ------------------------------------------------------------------------------------------------------------------------------
    def verify_broken_image(self):
        try:
            image = self.wait_for_element_visible(self.broken_image)
            width = image.get_attribute("naturalWidth")
            height = image.get_attribute("naturalHeight")
            self.logger.info(f"Image width{width}, height{height}")

            if int(width)== 0 and int(height)==0:
                self.logger.info("Broken image is correctly broken")
                return True
            else:
                self.logger.info("Broken image loaded  unexpectedly")

        except Exception as e:
            self.logger.info(f"Error checking broken image: {str(e)}")
            return False
#------------------------------------------------------------------------------------------------------------------------------

    def click_valid_link(self):
        try:
            self.click(self.valid_link)
            if "demoqa.com" in self.driver.current_url:
                self.logger.info("Valid link redirected correctly")
                return True
            else:
                self.logger.error("Unexpected URL")
                return False

        except Exception as e:
            self.logger.error(f"Error checking valid link: {str(e)}")
            return False

#------------------------------------------------------------------------------------------------------------------------------
    def click_broken_link(self):
        try:
            self.click(self.broken_link) # ← Broken linkni bosish
            current_url = self.driver.current_url # ← Yangi URL ni olish
            if ("404" in current_url or         # ←"404" bor-yo'qligi
                "not-found" in current_url or   # ← "not-found" bor-yo'qligi
                "error" in current_url or       # ← "error" bor-yo'qligi
                "status_codes" in current_url): # ← "status_codes" bor-yo'qligi
                self.logger.info("Broken link worked correctly")
                return True # ← Test PASSED (broken link to'g'ri buzilgan!)
            else:
                self.logger.error(f"Unexpected url: {current_url}")
                return False

        except Exception as e:
            self.logger.error(f"Error checking broken link : {str(e)}")
            return False

