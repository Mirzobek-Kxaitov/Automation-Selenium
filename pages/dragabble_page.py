from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base.base_page import BasePage

class DragabblePage(BasePage):
    DRAG_BASIC = (By.ID, "dragBox")
    TAB_AXIS = (By.ID, "draggableExample-tab-axisRestriction")
    AXIS_X = (By.ID, "restrictedX")
    AXIS_Y = (By.ID, "restrictedY")
    TAB_CONTAINER = (By.ID, "draggableExample-tab-containerRestriction")
    BOX_PARENT = (By.XPATH, "//div[@id='containmentWrapper']")
    BOX_CONTAINER = (By.XPATH, "//div[@class='draggable ui-widget-content ui-draggable ui-draggable-handle']")
    TAB_CURSOR = (By.ID, "draggableExample-tab-cursorStyle")
    DRAG_CENTER = (By.ID, "cursorCenter")
    DRAG_TOP_LEFT = (By.ID, "cursorTopLeft")
    DRAG_BOTTOM = (By.ID, "cursorBottom")

# ----------------------------------------------------------------------------------------------------------------------------
    def switch_to_tab(self, tab_locator):
        self.click(tab_locator)

    def drag_by_offset(self, box_locator, x_offset, y_offset):
        box = self.wait_for_element_visible(box_locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(box).move_by_offset(x_offset, y_offset).release().perform()

    def get_location(self, locator):
        box = self.wait_for_element_visible(locator)
        return box.location