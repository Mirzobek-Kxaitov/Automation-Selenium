import unittest
from selenium import webdriver
from pages.resizable_page import Resizable_Page
from utils.driver import get_driver
import time

class TestResizablePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/resizable")
        time.sleep(2)  # May be replaced with better waits in a real project
        self.resizable = Resizable_Page(self.driver)
        time.sleep(3)

    def test_resize_box(self):
        initial_size = self.resizable.get_box_size()
        self.resizable.resize_box(100, 80)  # Resize by 100x80 px
        time.sleep(1)
        new_size = self.resizable.get_box_size()
        self.assertNotEqual(initial_size, new_size, "Box size did not change!")
        time.sleep(3)

    def test_min_max_constraints(self):
        # Enlarge beyond max
        self.resizable.resize_box(400, 400)
        big_size = self.resizable.get_box_size()
        # Shrink below min
        self.resizable.resize_box(-400, -400)
        small_size = self.resizable.get_box_size()
        self.assertLessEqual(big_size['width'], 500)
        self.assertLessEqual(big_size['height'], 300)
        self.assertGreaterEqual(small_size['width'], 150)
        self.assertGreaterEqual(small_size['height'], 150)
        time.sleep(3)

    def test_box_does_not_resize_without_drag(self):
        initial_size = self.resizable.get_box_size()
        time.sleep(1)
        new_size = self.resizable.get_box_size()
        self.assertEqual(initial_size, new_size, "Box size changed without action!")
        time.sleep(3)

    def test_handle_presence(self):
        self.assertTrue(self.resizable.is_resize_handle_displayed(), "Resize handle should be visible!")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
