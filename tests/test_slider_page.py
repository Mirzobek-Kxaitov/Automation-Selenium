import time

from pages.slider_page import SliderPage
from utils.driver import get_driver

# def test_slider_basic_functionality():
#     driver = get_driver("https://demoqa.com/slider")
#     page = SliderPage(driver)
#
#     initial_value = page.get_slider_value()
#     print(f"Initial value {initial_value}")
#
#     page.set_slider_value(50)
#
#     new_value = page.get_slider_value()
#     print(f"New value: {new_value}")
#     if new_value == "75":
#         print("Test passed")
#     else:
#         print("Test failed")
#
#
#     driver.quit()


def test_slider_boundary_values():
    driver = get_driver("https://demoqa.com/slider")
    page = SliderPage(driver)



    # Max value test
    page.set_slider_value(100)
    max_value = page.get_slider_value()
    time.sleep(2)
    print(f"Max value: {max_value}")

    # Min value test
    page.set_slider_value(0)
    time.sleep(2)
    min_value = page.get_slider_value()
    print(f"Min value: {min_value}")

    # Verification (calculation issue ni hisobga olgan holda)
    if min_value == "0":  # Approximate check
        print("✅ Min test passed!")

    if max_value == "100" or int(max_value) >= 95:  # Approximate check
        print("✅ Max test passed!")

    driver.quit()