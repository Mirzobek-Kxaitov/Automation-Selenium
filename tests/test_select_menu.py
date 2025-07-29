from pages.select_menu import Select_Menu_Page
from utils.driver import get_driver
import pytest
import time

@pytest.fixture()
def setup():
    driver = get_driver("https://demoqa.com/select-menu")
    page = Select_Menu_Page(driver)
    yield page
    driver.quit()
# -----------------------------------------------------------------------------------------------------------------------

def test_group1_option1(setup):
    page = setup
    page.select_group1_option1()
    assert True

def test_select_group1_option2(setup):
    page = setup
    page.select_group1_option2()
    assert True

def test_select_group2_option1(setup):
    page = setup
    page.select_group2_option1()
    assert True

def test_select_group2_option2(setup):
    page = setup
    page.select_group2_option2()
    assert True

def test_select_a_root_option(setup):
    page = setup
    page.select_a_root_option()
    assert True

def test_select_another_root_option(setup):
    page = setup
    page.select_another_root_option()
    assert True

def test_select_all_value_options(setup):
    page = setup
    page.select_group1_option1()
    time.sleep(1)
    page.select_group1_option2()
    time.sleep(1)
    page.select_group2_option1()
    time.sleep(1)
    page.select_group2_option2()
    time.sleep(1)
    page.select_a_root_option()
    time.sleep(1)
    page.select_another_root_option()
    time.sleep(1)
    assert True

def test_select_one_functionality(setup):
    page = setup
    page.select_one_option_dr()
    time.sleep(2)
    page.select_one_option_mr()
    time.sleep(2)
    page.select_one_option_mrs()
    time.sleep(2)
    page.select_one_option_ms()
    time.sleep(2)
    page.select_one_option_prof()
    time.sleep(2)
    page.select_one_option_other()
    time.sleep(2)
    assert True
# -----------------------------------------------------------------------------------------------------------------------

def test_old_style_select_color_green(setup):
    page = setup
    page.select_old_style_color("Blue")
    time.sleep(1)
    page.select_old_style_color("Red")
    time.sleep(1)
    page.select_old_style_color("Green")
    time.sleep(1)
    page.select_old_style_color("Black")
    time.sleep(1)
    page.select_old_style_color("Yellow")
    time.sleep(1)
    page.select_old_style_color("Purple")
    time.sleep(1)
    page.select_old_style_color("White")
    time.sleep(1)
    page.select_old_style_color("Voilet")
    time.sleep(1)
    page.select_old_style_color("Indigo")
    time.sleep(1)
    page.select_old_style_color("Magenta")
    time.sleep(1)
    page.select_old_style_color("Aqua")
    time.sleep(2)
    assert True



def test_multiselect_functionality(setup):
    page = setup

    # Multiselect tanlash
    selection_result = page.select_multiselect_option()
    time.sleep(3)
    assert selection_result, "Failed to select multiselect options"

    # Screenshot olish va manual tekshirish
    page._take_screenshot("multiselect_final_state")

    print("Multiselect test completed successfully")





def test_standard_multi_select(setup):
    page = setup
    page.select_standard_multi_cars()
    time.sleep(2)
    assert page.select_standard_multi_cars()

