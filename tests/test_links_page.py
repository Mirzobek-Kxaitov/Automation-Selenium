import pytest
from pages.links_page import Links_page

class Test_Links_page:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.links_page = Links_page(self.driver)  # ← (driver) qo'shildi
        self.driver.get("https://demoqa.com/links")

    def test_new_tab_functionality(self):
        """Yangi tab ochish funksionalligini tekshirish"""
        assert self.links_page.test_new_tab_functionality()

    def test_api_created_response(self):
        """Created (201) API response tekshirish"""
        assert self.links_page.verify_api_call_response(
            self.links_page.click_created_button,
            "201",
            "Created"
        )

    def test_api_no_content_response(self):
        """No Content (204) API response tekshirish"""
        assert self.links_page.verify_api_call_response(
            self.links_page.click_no_content_button,
            "204",
            "No Content"
        )

    def test_api_moved_response(self):
        """Moved Permanently (301) API response tekshirish"""
        assert self.links_page.verify_api_call_response(
            self.links_page.click_moved_button,
            "301",
            "Moved Permanently"
        )

    def test_api_bad_request_response(self):
        """Bad Request (400) API response tekshirish"""
        assert self.links_page.verify_api_call_response(
            self.links_page.click_bad_request_button,
            "400",
            "Bad Request"
        )

    def test_api_unauthorized_response(self):
        """Unauthorized (401) API response tekshirish"""
        assert self.links_page.verify_api_call_response(
            self.links_page.click_unauthorized_button,
            "401",
            "Unauthorized"
        )

    def test_api_forbidden_response(self):
        """Forbidden (403) API response tekshirish"""
        assert self.links_page.verify_api_call_response(
            self.links_page.click_forbidden_button,
            "403",
            "Forbidden"
        )

    def test_api_not_found_response(self):
        """Not Found (404) API response tekshirish"""
        assert self.links_page.verify_api_call_response(
            self.links_page.click_not_found_button,
            "404",
            "Not Found"
        )