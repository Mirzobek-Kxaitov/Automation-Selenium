import pytest
from pages.frames_page import Frames_page


class Test_Frame_page:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.frames_page = Frames_page(self.driver)
        self.driver.get("https://demoqa.com/frames")

    def test_frame1_content(self):
        """Frame1 ning content ini tekshirish"""
        assert self.frames_page.verify_frame_content("frame1")

    def test_frame2_content(self):
        """Frame2 ning content ini tekshirish"""
        assert self.frames_page.verify_frame_content("frame2")

    def test_frame_count(self):
        """Sahifadagi frame larni sanash"""
        frames_count = self.frames_page.get_target_frame_count()
        assert frames_count == 2, f"Expected 2 frames, but found {frames_count}"

    def test_frame_switching(self):
        """Frame switching funksionalligini tekshirish"""
        # Frame1 ga o'tish
        assert self.frames_page.switch_to_frame1(), "Failed to switch to frame1"

        # Content tekshirish
        content = self.frames_page.get_frame_content_text()
        assert "This is a sample page" in content, f"Wrong content in frame1: {content}"

        # Default content ga qaytish
        assert self.frames_page.switch_to_default_content(), "Failed to switch to default content"

        # Frame2 ga o'tish
        assert self.frames_page.switch_to_frame2(), "Failed to switch to frame2"

        # Content tekshirish
        content = self.frames_page.get_frame_content_text()
        assert "This is a sample page" in content, f"Wrong content in frame2: {content}"

        # Default content ga qaytish
        assert self.frames_page.switch_to_default_content(), "Failed to switch back to default content"