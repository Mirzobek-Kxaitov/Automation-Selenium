from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DraggablePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    DRAG_ME_BOX = (By.ID, "dragBox")

    # Axis Restriction tab
    TAB_AXIS = (By.ID, "draggableExample-tab-axisRestriction")
    ONLY_X_BOX = (By.ID, "restrictedX")
    ONLY_Y_BOX = (By.ID, "restrictedY")

    # Container Restriction tab
    TAB_CONTAINER = (By.ID, "draggableExample-tab-containerRestriction")
    BOX_PARENT = (By.XPATH, "//div[@id='containmentWrapper']")
    BOX_CONTAINER = (By.XPATH, "//div[@class='draggable ui-widget-content ui-draggable ui-draggable-handle']")

    # Cursor Style tab
    TAB_CURSOR = (By.ID, "draggableExample-tab-cursorStyle")
    DRAG_CENTER = (By.ID, "cursorCenter")
    DRAG_TOP_LEFT = (By.ID, "cursorTopLeft")
    DRAG_BOTTOM = (By.ID, "cursorBottom")

    def wait_for_element_visible(self, locator):
        """Element ko'rinishini kutish"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Element'ni bosish"""
        element = self.wait_for_element_visible(locator)
        element.click()

    def switch_to_tab(self, tab_locator):
        element = self.wait_for_element_visible(tab_locator)
        self.driver.execute_script("arguments[0].click();", element)
#
    def drag_by_offset(self, box_locator, x_offset, y_offset):
        """Element'ni belgilangan masofaga sudrab o'tkazish"""
        # Boshlang'ich pozitsiyani olish
        initial_position = self.get_location(box_locator)

        # Element'ni topish va sudrab o'tkazish
        box = self.wait_for_element_visible(box_locator)

        # Element'ni ko'rinadigan joyga scroll qilish
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", box)
        time.sleep(0.5)

        # Drag action
        actions = ActionChains(self.driver)
        actions.click_and_hold(box).move_by_offset(x_offset, y_offset).release().perform()

        # Action tugashini kutish
        time.sleep(1)

        # Oxirgi pozitsiyani olish
        final_position = self.get_location(box_locator)

        return {
            'initial_position': initial_position,
            'final_position': final_position,
            'moved': initial_position != final_position
        }

    def get_location(self, locator):
        """Element pozitsiyasini olish"""
        box = self.wait_for_element_visible(locator)
        return box.location

    def is_element_draggable(self, locator):
        """Element sudraladigan yoki yo'qligini tekshirish"""
        element = self.wait_for_element_visible(locator)

        # Draggable attribute'ni tekshirish
        draggable_attr = element.get_attribute("draggable")

        # Draggable class'larni tekshirish
        class_names = element.get_attribute("class") or ""
        has_draggable_class = 'draggable' in class_names.lower() or 'ui-draggable' in class_names.lower()

        return draggable_attr == "true" or has_draggable_class