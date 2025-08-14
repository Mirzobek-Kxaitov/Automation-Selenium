from pages.broken_links_page import Broken_list_page

def test_verify_valid_image(driver):
    broken_links_page = Broken_list_page(driver)
    assert broken_links_page.verify_valid_image()
#------------------------------------------------------------------------------------------------------------------------------
def test_verify_broken_image(driver):
    broken_links_page = Broken_list_page(driver)
    assert broken_links_page.verify_broken_image()
#------------------------------------------------------------------------------------------------------------------------------
def test_click_valid_link(driver):
    broken_links_page = Broken_list_page(driver)
    assert broken_links_page.click_valid_link()
#------------------------------------------------------------------------------------------------------------------------------
def test_click_broken_link(driver):
    broken_links_page = Broken_list_page(driver)
    assert broken_links_page.click_broken_link()

