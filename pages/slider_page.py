from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class SliderPage(BasePage):
    SLIDER_INPUT = (By.CLASS_NAME, "range-slider")
    SLIDER_CONTAINER = (By.ID,'sliderContainer')

    def get_slider_value(self):      # 🔍 Sliderning joriy qiymatini olish
        element = self.wait_for_element_visible(self.SLIDER_INPUT)
        return element.get_attribute('value')# HTML attribute sifatida qiymat qaytariladi (string)

    def set_slider_value(self, target_value: int):    # ⚙️ Sliderga kerakli qiymatni o‘rnatish
        slider = self.wait_for_element_visible(self.SLIDER_INPUT)     # Slider elementini kutib olish
        current_value = int(self.get_slider_value())        # Joriy qiymatni olish (int ko‘rinishga keltiramiz)

        # Agar qiymat allaqachon kerakli bo‘lsa, hech narsa qilinmaydi
        if current_value == target_value:
            return
        # 📏 Slider'ning vizual kengligini olish (px da)
        slider_width = slider.size['width']
        # 🔢 Slider diapazoni (demoqa uchun default 0–100)
        max_value = 100
        # 🎯 Offset hisoblash: nechta px ga o‘ngga yoki chapga surish kerak
        offset = int(((target_value - current_value) / max_value) * slider_width)

        try:
            # 🖱 ActionChains orqali slider'ni ko‘chirish
            actions = ActionChains(self.driver)
            actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()

        except Exception as e:
            # ❌ Agar harakat muvaffaqiyatsiz bo‘lsa, log yoziladi
            self.logger.error(f"Failed to set slider value: {e}")
