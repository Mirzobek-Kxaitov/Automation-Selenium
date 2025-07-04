from base.base_page import BasePage
from pages.auto_complete_page import AutoComplete_page
from utils.driver import  get_driver
import time

def test_single_color_autocomplete():
    driver = get_driver("https://demoqa.com/auto-complete")
    autocomplete_page = AutoComplete_page(driver)

    autocomplete_page.input_single_color("bl")
    autocomplete_page.select_color_from_suggestions("Blue")
    selected_color = autocomplete_page.get_text(autocomplete_page.SINGLE_COLOR_INPUT)
    assert "Blue" in selected_color
    driver.quit()

# def test_multiple_color_autocomplete():
#     driver = get_driver("https://demoqa.com/auto-complete")
#     autocomplete_page = AutoComplete_page(driver)
#
#     autocomplete_page.input_multiple_color("re")
#     autocomplete_page.select_color_from_suggestions("Red")
#     autocomplete_page.input_multiple_color("bl")
#     autocomplete_page.select_color_from_suggestions("Blue")
#
#     selected_colors = autocomplete_page.get_selected_colors()
#     assert "Red" in selected_colors
#     assert "Blue" in selected_colors
#     assert len(selected_colors) == 2
#
#     driver.quit()
#
# def test_remove_color():
#     driver = get_driver("https://demoqa.com/auto-complete")
#     autocomplete_page = AutoComplete_page(driver)
#     autocomplete_page.input_multiple_color("re")
#     autocomplete_page.select_color_from_suggestions("Red")
#     autocomplete_page.input_multiple_color("gr")
#     autocomplete_page.select_color_from_suggestions("Green")
#     autocomplete_page.input_multiple_color("bl")
#     autocomplete_page.select_color_from_suggestions("Blue")
#     selected_colors = autocomplete_page.get_selected_colors()
#     assert len(selected_colors) == 3
#     autocomplete_page.remove_color(0)
#     selected_colors_after = autocomplete_page.get_selected_colors()
#     assert len(selected_colors_after) == 2
#     assert "Red" not in selected_colors_after
#     driver.quit()
#
#
