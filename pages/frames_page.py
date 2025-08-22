import time
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Frames_page(BasePage):
    BIG_FRAME = "frame1"
    LITTLE_FRAME = "frame2"
    FRAME_CONTENT = (By.ID, "sampleHeading")

    def switch_to_frame1(self):
        """Katta asosiy framega o'tish metodi"""
        try:
            # Frame mavjudligini kutamiz
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.frame_to_be_available_and_switch_to_it(self.BIG_FRAME))
            self.logger.info("Successfully switched to frame1")
            return True
        except Exception as e:
            self.logger.error(f"Error switching to frame1: {str(e)}")
            return False

    def switch_to_frame2(self):
        """Kichik framega o'tish"""
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.frame_to_be_available_and_switch_to_it(self.LITTLE_FRAME))
            self.logger.info("Successfully switched to frame2")
            return True
        except Exception as e:
            self.logger.error(f"Error switching to frame2: {str(e)}")
            return False

    def switch_to_default_content(self):
        """Asosiy main page ga qaytish - framelardan chiqish"""
        try:
            self.driver.switch_to.default_content()
            self.logger.info("Successfully switched to default content")
            return True
        except Exception as e:
            self.logger.error(f"Error switching to default content: {str(e)}")
            return False

    def get_frame_content_text(self):
        """Frame ichidagi text ni olish"""
        try:
            # Element ko'rinadigan bo'lguncha kutamiz
            element = self.wait_for_element_visible(self.FRAME_CONTENT)
            text = element.text
            self.logger.info(f"Frame content text: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Error getting frame content text: {str(e)}")
            return ""

    def get_frame_count(self):
        """Sahifadagi barcha iframe larni sanash"""
        try:
            frames = self.driver.find_elements(By.TAG_NAME, "iframe")
            count = len(frames)
            self.logger.info(f"Total iframe count: {count}")
            return count
        except Exception as e:
            self.logger.error(f"Error getting frame count: {str(e)}")
            return 0

    def get_target_frame_count(self):
        """Faqat bizning frame'larimizni tekshirish"""
        try:
            frame1_exists = len(self.driver.find_elements(By.ID, self.BIG_FRAME)) > 0
            frame2_exists = len(self.driver.find_elements(By.ID, self.LITTLE_FRAME)) > 0
            count = int(frame1_exists) + int(frame2_exists)
            self.logger.info(f"Target frame count: {count}")
            return count
        except Exception as e:
            self.logger.error(f"Error getting target frame count: {str(e)}")
            return 0

    def verify_frame_content(self, frame_type="frame1"):
        """Frame ga o'tish va content ni tekshirish"""
        try:
            # Default content ga qaytamiz
            self.switch_to_default_content()

            # Kerakli frame ga o'tamiz
            if frame_type == "frame1":
                success = self.switch_to_frame1()
            elif frame_type == "frame2":
                success = self.switch_to_frame2()
            else:
                self.logger.error(f"Unknown frame type: {frame_type}")
                return False

            if not success:
                return False

            # Content ni olamiz
            content = self.get_frame_content_text()

            # Default content ga qaytamiz
            self.switch_to_default_content()

            # Content ni tekshiramiz
            if "This is a sample page" in content:
                self.logger.info(f"Frame {frame_type} content verification successful")
                return True
            else:
                self.logger.error(f"Frame {frame_type} content verification failed. Found: {content}")
                return False

        except Exception as e:
            self.logger.error(f"Error verifying frame {frame_type} content: {str(e)}")
            # Xato bo'lsa ham default content ga qaytamiz
            try:
                self.switch_to_default_content()
            except:
                pass
            return False