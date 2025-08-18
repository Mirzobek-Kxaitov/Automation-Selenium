import pytest
from pages.dragabble_page import DraggablePage

class TestDraggablePage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Har bir test uchun setup"""
        self.driver = driver
        self.draggable_page = DraggablePage(self.driver)
        # DemoQA draggable sahifasiga o'tish
        self.driver.get("https://demoqa.com/dragabble")
#
    def test_simple_drag(self):
        """Oddiy drag testi"""
        print("\n=== Simple Drag Test ===")

        # Boshlang'ich pozitsiyani olish
        initial_pos = self.draggable_page.get_location(self.draggable_page.DRAG_ME_BOX)
        print(f"Initial position: {initial_pos}")

        # Drag qilish
        result = self.draggable_page.drag_by_offset(self.draggable_page.DRAG_ME_BOX, 100, 50)

        # Natijani tekshirish
        assert result is not None, "Drag operation failed"
        assert result['moved'], "Element did not move"

        final_pos = result['final_position']
        print(f"Final position: {final_pos}")

        # Pozitsiya o'zgarganligini tekshirish
        assert final_pos['x'] > initial_pos['x'], "X position should increase"
        assert final_pos['y'] > initial_pos['y'], "Y position should increase"

        print("✅ Simple drag test PASSED")

    def test_axis_restriction_x_only(self):
        """X o'qida cheklash testi"""
        print("\n=== X-Axis Restriction Test ===")

        # Axis restriction tab'ga o'tish
        self.draggable_page.switch_to_tab(self.draggable_page.TAB_AXIS)

        # X-only element'ni topish
        x_only_element = self.draggable_page.wait_for_element_visible(self.draggable_page.ONLY_X_BOX)
        assert x_only_element.is_displayed(), "X-only element should be visible"

        # Boshlang'ich pozitsiya
        initial_pos = self.draggable_page.get_location(self.draggable_page.ONLY_X_BOX)
        print(f"Initial position: {initial_pos}")

        # X bo'yicha harakat (ishlashi kerak)
        result_x = self.draggable_page.drag_by_offset(self.draggable_page.ONLY_X_BOX, 100, 0)
        assert result_x['moved'], "X movement should work"
        print(f"After X movement: {result_x['final_position']}")

        # Y bo'yicha harakat (cheklanishi kerak)
        result_y = self.draggable_page.drag_by_offset(self.draggable_page.ONLY_X_BOX, 0, 50)

        # Y pozitsiyasi o'zgarmaganligini tekshirish (5 pixel xatolikka ruxsat)
        y_changed = abs(result_y['final_position']['y'] - result_x['final_position']['y']) > 5
        assert not y_changed, "Y movement should be restricted"

        print("✅ X-Axis restriction test PASSED")

    def test_axis_restriction_y_only(self):
        """Y o'qida cheklash testi"""
        print("\n=== Y-Axis Restriction Test ===")

        # Axis restriction tab'da qolish
        self.draggable_page.switch_to_tab(self.draggable_page.TAB_AXIS)

        # Y-only element'ni topish
        y_only_element = self.draggable_page.wait_for_element_visible(self.draggable_page.ONLY_Y_BOX)
        assert y_only_element.is_displayed(), "Y-only element should be visible"

        # Boshlang'ich pozitsiya
        initial_pos = self.draggable_page.get_location(self.draggable_page.ONLY_Y_BOX)
        print(f"Initial position: {initial_pos}")

        # Y bo'yicha harakat (ishlashi kerak)
        result_y = self.draggable_page.drag_by_offset(self.draggable_page.ONLY_Y_BOX, 0, 100)
        assert result_y['moved'], "Y movement should work"
        print(f"After Y movement: {result_y['final_position']}")

        # X bo'yicha harakat (cheklanishi kerak)
        result_x = self.draggable_page.drag_by_offset(self.draggable_page.ONLY_Y_BOX, 50, 0)

        # X pozitsiyasi o'zgarmaganligini tekshirish (5 pixel xatolikka ruxsat)
        x_changed = abs(result_x['final_position']['x'] - result_y['final_position']['x']) > 5
        assert not x_changed, "X movement should be restricted"

        print("✅ Y-Axis restriction test PASSED")

    def test_container_restriction(self):
        """Container cheklash testi"""
        print("\n=== Container Restriction Test ===")

        # Container restriction tab'ga o'tish
        self.draggable_page.switch_to_tab(self.draggable_page.TAB_CONTAINER)

        # Container element'ni topish
        container_element = self.draggable_page.wait_for_element_visible(self.draggable_page.BOX_CONTAINER)
        assert container_element.is_displayed(), "Container element should be visible"

        # Boshlang'ich pozitsiya
        initial_pos = self.draggable_page.get_location(self.draggable_page.BOX_CONTAINER)
        print(f"Initial position: {initial_pos}")

        # Kichik harakat (ishlashi kerak)
        result = self.draggable_page.drag_by_offset(self.draggable_page.BOX_CONTAINER, 50, 50)
        assert result['moved'], "Small movement should work"

        print(f"After movement: {result['final_position']}")
        print("✅ Container restriction test PASSED")

    def test_cursor_styles(self):
        """Cursor uslublari testi"""
        print("\n=== Cursor Styles Test ===")

        # Cursor style tab'ga o'tish
        self.draggable_page.switch_to_tab(self.draggable_page.TAB_CURSOR)

        # Har bir cursor element'ni tekshirish
        cursor_elements = [
            (self.draggable_page.DRAG_CENTER, "Center cursor"),
            (self.draggable_page.DRAG_TOP_LEFT, "Top-left cursor"),
            (self.draggable_page.DRAG_BOTTOM, "Bottom cursor")
        ]

        for element_locator, description in cursor_elements:
            print(f"Testing {description}...")

            # Element mavjudligini tekshirish
            element = self.draggable_page.wait_for_element_visible(element_locator)
            assert element.is_displayed(), f"{description} should be visible"

            # Draggable ekanligini tekshirish
            is_draggable = self.draggable_page.is_element_draggable(element_locator)
            assert is_draggable, f"{description} should be draggable"

            # Drag qilish
            result = self.draggable_page.drag_by_offset(element_locator, 30, 30)
            assert result is not None, f"Failed to drag {description}"
            assert result['moved'], f"{description} should move"

            print(f"✅ {description} test passed")

        print("✅ All cursor styles test PASSED")

    def test_element_visibility(self):
        """Element ko'rinish testi"""
        print("\n=== Element Visibility Test ===")

        # Drag element ko'rinadigan ekanligini tekshirish
        drag_element = self.draggable_page.wait_for_element_visible(self.draggable_page.DRAG_ME_BOX)
        assert drag_element.is_displayed(), "Drag element should be visible"

        # Element draggable ekanligini tekshirish
        is_draggable = self.draggable_page.is_element_draggable(self.draggable_page.DRAG_ME_BOX)
        assert is_draggable, "Element should be draggable"

        print("✅ Element visibility test PASSED")