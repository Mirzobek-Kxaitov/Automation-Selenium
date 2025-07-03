from base.base_page import BasePage
from selenium.webdriver.common.by import By

class Nested_frames_page(BasePage):
    PARENT_FRAME = "frame1"
    CHILD_FRAME = 0
    N_FRAME_CONTENT= (By.XPATH, "//text()")

    def switch_to_parent_frame(self):
        self.driver.switch_to.frame(self.PARENT_FRAME)

    def switch_to_child_frame(self):
        self.driver.switch_to.frame(self.CHILD_FRAME)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_frame_content_text(self):
        return self.get_text(self.N_FRAME_CONTENT)

    def get_frame_count(self):
        frames = self.driver.find.elements(By.TAG_NAME, "iframe")
        return len(frames)

    def get_target_frame_count(self):
        """Faqat bizning frame'larimizni tekshirish"""
        frame1_exists = len(self.driver.find_elements(By.ID, "frame1")) > 0
        frame2_exists = len(self.driver.find_elements(By.ID, "child-frame")) > 0
        return int(frame1_exists) + int(frame2_exists)