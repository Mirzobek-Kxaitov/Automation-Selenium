import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page

def test_login_invalid_credentials(login_page):
    invalid_username = "invalid_user"
    invalid_password = "InvalidPassword123!"
    expected_error_message = "Invalid username or password!"
    login_page.login(invalid_username, invalid_password)
    login_page.logger.info("Login formasi noto'g'ri ma'lumotlar bilan to'ldirildi va yuborildi.")
    actual_error_message = login_page.get_error_message()
    assert actual_error_message == expected_error_message, \
        f"Kutilgan xatolik xabari '{expected_error_message}', lekin '{actual_error_message}' chiqdi."

    login_page.logger.info("Test muvaffaqiyatli yakunlandi: Noto'g'ri ma'lumotlar uchun xatolik xabari to'g'ri chiqdi.")
    login_page._take_screenshot("test_login_invalid_credentials_success")

def test_login_valid_credential(login_page):
    valid_username = "mirzobek"
    valid_password = "cDN!!asaCxbxva4"
    login_page.login(valid_username,valid_password)
    login_page.logger.info("Login formasi to'g'ri ma'lumotlar bilan to'ldirildi va yuborildi.")
    login_page.logger.info("Test muvaffaqiyatli yakunlandi")
    login_page._take_screenshot("test_login_valid_credentials_success")