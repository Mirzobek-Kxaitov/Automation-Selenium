from pages.tabs_page import TabsPage
from utils.driver import get_driver
from selenium.webdriver.common.by import By

def test_tabs_content_switching():
    driver = get_driver("https://demoqa.com/tabs")
    page = TabsPage(driver)

    page.click_what_tab()
    assert "Lorem Ipsum is simply dummy" in page.get_what_text()

    page.click_origin_tab()
    assert "Contrary to popular belief, Lorem Ipsum is not simply random text" in page.get_origin_text()

    page.click_use_tab()
    assert "It is a long established fact that a reader" in page.get_use_text()

    driver.quit()

def test_more_tab_is_disabled():
    driver = get_driver("https://demoqa.com/tabs")
    page = TabsPage(driver)
    more_element = driver.find_element(By.ID, "demo-tab-more")

    is_disabled = "disabled" in more_element.get_attribute("class")
    assert is_disabled, "'More' tab is expected to be disabled"

    driver.quit()