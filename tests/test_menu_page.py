import pytest
from pages.menu_page import MenuPage
import time


@pytest.fixture
def menu_page(driver):
    page = MenuPage(driver)
    page.open()
    return page


def test_menu_page_debug(menu_page):
    """Debug: Sahifadagi menu strukturasini tekshirish"""
    menu_page.logger.info("DEBUG: Menu strukturasini tekshirish...")

    # Sahifa to'liq yuklanganligini kutish
    time.sleep(3)

    # Barcha menu elementlarining mavjudligini tekshirish
    main_item2_exists = menu_page.driver.find_elements(*menu_page.MAIN_ITEM_2)
    sub_item1_exists = menu_page.driver.find_elements(*menu_page.SUB_ITEM_1)

    menu_page.logger.info(f"Main Item 2 count: {len(main_item2_exists)}")
    menu_page.logger.info(f"Sub Item 1 count: {len(sub_item1_exists)}")

    # Sahifa manbasi haqida ma'lumot
    page_title = menu_page.driver.title
    current_url = menu_page.driver.current_url

    menu_page.logger.info(f"Page title: {page_title}")
    menu_page.logger.info(f"Current URL: {current_url}")

    # CSS qoidalarini tekshirish
    if len(main_item2_exists) > 0:
        main_element = main_item2_exists[0]

        # JavaScript orqali CSS ma'lumotlarini olish
        css_info = menu_page.driver.execute_script("""
            const element = arguments[0];
            const style = window.getComputedStyle(element);

            return {
                display: style.display,
                visibility: style.visibility,
                position: style.position,
                zIndex: style.zIndex
            };
        """, main_element)

        menu_page.logger.info(f"Main element CSS: {css_info}")

    # Submenu element haqida ma'lumot
    if len(sub_item1_exists) > 0:
        sub_element = sub_item1_exists[0]

        sub_css_info = menu_page.driver.execute_script("""
            const element = arguments[0];
            const style = window.getComputedStyle(element);

            return {
                display: style.display,
                visibility: style.visibility,
                opacity: style.opacity,
                height: element.offsetHeight,
                width: element.offsetWidth
            };
        """, sub_element)

        menu_page.logger.info(f"Sub element CSS before hover: {sub_css_info}")

        # Hover qilish va qaytadan tekshirish
        menu_page.hover_element(menu_page.MAIN_ITEM_2)
        time.sleep(2)

        sub_css_info_after = menu_page.driver.execute_script("""
            const element = arguments[0];
            const style = window.getComputedStyle(element);

            return {
                display: style.display,
                visibility: style.visibility,
                opacity: style.opacity,
                height: element.offsetHeight,
                width: element.offsetWidth
            };
        """, sub_element)

        menu_page.logger.info(f"Sub element CSS after hover: {sub_css_info_after}")

    # Test har doim pass bo'lsin (debug uchun)
    assert True


def test_force_show_submenu(menu_page):
    """JavaScript orqali submenu'ni majburiy ko'rsatish"""
    menu_page.logger.info("TEST: JavaScript orqali submenu ko'rsatish")

    # Submenu'ni JavaScript orqali majburiy ko'rsatish
    result = menu_page.driver.execute_script("""
        // Submenu elementini topish
        const submenu = document.querySelector('#nav > li:nth-child(2) > ul');
        const subItem = document.querySelector('#nav > li:nth-child(2) > ul > li:nth-child(1) > a');

        if (submenu && subItem) {
            // CSS orqali ko'rsatish
            submenu.style.display = 'block';
            submenu.style.visibility = 'visible';
            submenu.style.opacity = '1';

            return {
                success: true,
                submenu_found: true,
                subitem_found: true
            };
        } else {
            return {
                success: false,
                submenu_found: !!submenu,
                subitem_found: !!subItem
            };
        }
    """)

    menu_page.logger.info(f"Force show result: {result}")

    if result['success']:
        time.sleep(1)

        # Endi ko'rinadimi?
        submenu_visible = menu_page.is_element_visible(menu_page.SUB_ITEM_1)
        menu_page.logger.info(f"Submenu visible after JS force: {submenu_visible}")

        assert submenu_visible, "JavaScript orqali ko'rsatish ham ishlamadi"
    else:
        menu_page.logger.error("Menu elementlari topilmadi!")
        # Element mavjud emasligini tekshirish
        assert False, f"Menu strukturasi noto'g'ri: {result}"