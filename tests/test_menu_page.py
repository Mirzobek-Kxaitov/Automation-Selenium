import pytest
from pages.menu_page import MenuPage

@pytest.fixture
def menu_page(driver):
    page = MenuPage(driver)
    page.open()
    return page


# tests/test_menu_page.py dagi testni o'zgartiring

def test_submenu_disappears_on_hover_away(menu_page):
    """
    Sichqoncha menyudan chetga olinganda ichki menyu yopilishini (yo'qolishini) tekshiradi.
    """
    menu_page.logger.info("TEST: Ichki menyuning hoverdan keyin yo'qolishini tekshirish.")

    menu_page.hover_element(menu_page.MAIN_ITEM_2)

    assert menu_page.is_element_visible(menu_page.SUB_ITEM_1), "Tekshiruv oldidan ichki menyu ochilmadi."
    menu_page.logger.info("Ichki menyu muvaffaqiyatli ochildi.")

    # JavaScript yordamida ishonchliroq hover qilamiz
    menu_page.hover_element_with_js(menu_page.PAGE_FOOTER) # <-- O'ZGARISH SHU YERDA
    menu_page.logger.info("Sichqoncha menyudan chetga, sahifa footeriga olindi.")

    assert menu_page.wait_for_element_invisible(
        menu_page.SUB_ITEM_1), "Sichqoncha chetga olingandan keyin ichki menyu yo'qolmadi."
    menu_page.logger.info("Test muvaffaqiyatli: Ichki menyu to'g'ri yopildi.")
def test_navigation_on_submenu_click(menu_page):
    menu_page.logger.info("TEST: Ichki menyu bandining bosilishini (navigatsiya) tekshirish.")
    menu_page.hover_element(menu_page.MAIN_ITEM_2)
    menu_page.hover_element(menu_page.SUB_SUB_LIST)

    try:
        menu_page.click(menu_page.SUB_SUB_ITEM_1)
        clicked_successfully = True
        menu_page.logger.info("Sub Sub Item 1 muvaffaqiyatli bosildi.")
    except Exception as e:
        menu_page.logger.error(f"Elementni bosishda kutilmagan xato yuz berdi: {e}")
        clicked_successfully = False
    assert clicked_successfully, "Ichki menyu bandini bosishda xatolik yuz berdi."

