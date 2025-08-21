from base.base_page import BasePage
from pages.dynamic_page import Dynamic_page
import pytest
class Test_Dynamic_page:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.dynamic_page = Dynamic_page(self.driver)
        self.driver.get("https://demoqa.com/dynamic-properties")
#
    def test_random_text_verification(self):
        assert self.dynamic_page.verify_random_text_displayed()

    def test_enable_button_functionality(self):
        assert  self.dynamic_page.verify_enable_button_clickable()

    def test_color_change_functionality(self):
        assert  self.dynamic_page.verify_color_change()


    def test_visible_button_functionality(self):
        assert  self.dynamic_page.verification_visible_button()
