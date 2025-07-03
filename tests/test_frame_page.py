from pages.frames_page import Frames_page
from utils.driver import get_driver

def test_frame1():
    driver = get_driver("https://demoqa.com/frames")
    frames_page = Frames_page(driver)
    frames_page.logger.info("STARTING TEST: test_frame1")
    frames_page.switch_to_frame1()
    content = frames_page.get_frame_content_text()
    assert "This is a sample page" in content
    frames_page.logger.info("Test passed!")
    driver.quit()

def test_frame2():
    driver = get_driver("https://demoqa.com/frames")
    frames_page = Frames_page(driver)
    frames_page.logger.info("STARTING TEST: test_frame2")
    frames_page.switch_to_frame2()
    content = frames_page.get_frame_content_text()
    assert "This is a sample page" in content
    frames_page.logger.info("Test passed")
    driver.quit()

def test_frame_count():
    driver = get_driver("https://demoqa.com/frames")
    frames_page = Frames_page(driver)
    frames_page.logger.info("STARTING TEST: test_frame_count")
    frames_count = frames_page.get_target_frame_count()
    assert frames_count == 2
    frames_page.logger.info("Test passed")
    driver.quit()
