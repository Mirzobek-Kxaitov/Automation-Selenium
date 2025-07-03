from base.base_page import BasePage
from selenium.webdriver.common.by import By
class Frames_page(BasePage):
    BIG_FRAME = "frame1"
    LITTLE_FRAME = "frame2"
    FRAME_CONTENT = (By.ID, "sampleHeading")

    def switch_to_frame1(self): #katta asosiy framega o'tish metodi
        self.driver.switch_to.frame(self.BIG_FRAME)

    def switch_to_frame2(self): #kichik framega o'tish
        self.driver.switch_to.frame(self.LITTLE_FRAME)

    def switch_to_default_content(self): #asosiy main page ga qaytish - framelardan chiqish
        self.driver.switch_to.default_content()

    def get_frame_content_text(self):  # ← Page Object ichida
        return self.get_text(self.FRAME_CONTENT)

    def get_frame_count(self):
        frames = self.driver.find_elements(By.TAG_NAME, "iframe")
        return len(frames)

    def get_target_frame_count(self):
        """Faqat bizning frame'larimizni tekshirish"""
        frame1_exists = len(self.driver.find_elements(By.ID, "frame1")) > 0
        frame2_exists = len(self.driver.find_elements(By.ID, "frame2")) > 0
        return int(frame1_exists) + int(frame2_exists)