# tests/test_menu_page.py - BUTUNLAY ALMASHTIRING

import pytest
from pages.menu_page import MenuPage
import time


@pytest.fixture
def menu_page(driver):
    page = MenuPage(driver)
    page.open()
    return page


def test_submenu_disappears_on_hover_away(menu_page):
    """
    Sichqoncha menyudan chetga olinganda ichki menyu yopilishini tekshiradi.
    """
    menu_page.logger.info("TEST: Ichki menyuning hoverdan keyin yo'qolishini tekshirish.")

    # Submenu ochish
    menu_page.hover_element(menu_page.MAIN_ITEM_2)

    # Submenu ochilganini tekshirish
    assert menu_page.is_element_visible(menu_page.SUB_ITEM_1), "Submenu ochilmadi."
    menu_page.logger.info("Ichki menyu muvaffaqiyatli ochildi.")

    # Mouse'ni menu'dan olib ketish
    menu_page.trigger_mouse_leave(menu_page.MAIN_ITEM_2)
    menu_page.move_mouse_to_safe_location()
    menu_page.logger.info("Sichqoncha menyudan chetga olindi.")

    # Submenu yopilishini kutish
    is_invisible = menu_page.wait_for_element_invisible_with_retry(
        menu_page.SUB_ITEM_1,
        timeout=5,
        max_retries=3
    )

    assert is_invisible, "Sichqoncha chetga olingandan keyin ichki menyu yo'qolmadi."
    menu_page.logger.info("Test muvaffaqiyatli: Ichki menyu to'g'ri yopildi.")


def test_navigation_on_submenu_click(menu_page):
    menu_page.logger.info("TEST: Ichki menyu bandining bosilishini tekshirish.")

    menu_page.hover_element(menu_page.MAIN_ITEM_2)
    menu_page.hover_element(menu_page.SUB_SUB_LIST)
    time.sleep(0.5)

    try:
        menu_page.click(menu_page.SUB_SUB_ITEM_1)
        menu_page.logger.info("Sub Sub Item 1 muvaffaqiyatli bosildi.")
        clicked_successfully = True
    except Exception as e:
        menu_page.logger.error(f"Elementni bosishda xato: {e}")
        clicked_successfully = False

    assert clicked_successfully, "Ichki menyu bandini bosishda xatolik yuz berdi."