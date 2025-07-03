from base.base_page import BasePage
from utils.driver import get_driver
from pages.login_page import LoginPage


driver = get_driver("https://demoqa.com/login")
login_page = LoginPage(driver)

login_page.enter_username("invalid_user")
base_page.logger.info("usernamekiritildi")

login_page.enter_password("invalid_pass")
base_page.logger.info("password kiritildi")
base_page._take_screenshot()

login_page.click_login()
base_page.logger.info("login button bosildi")

error_text = login_page.get_error_message()
assert "Invalid" in error_text, "❌ Xato xabari noto‘g‘ri!"

driver.quit()