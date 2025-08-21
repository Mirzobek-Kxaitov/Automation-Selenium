from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def get_driver():
    options = Options()

    if os.getenv("CI") or os.getenv("HEADLESS", "").lower() in ("1", "true", "yes"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        # CI muhiti uchun qo'shimcha sozlamalar
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-features=TranslateUI")
        options.add_argument("--disable-ipc-flooding-protection")
        options.add_argument("--remote-debugging-port=9222")
        # Network timeout sozlamalari
        options.add_argument("--timeout=30000")
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
    else:
        options.add_argument("--start-maximized")
        options.add_argument("--force-device-scale-factor=0.70")

    # Barcha muhitlar uchun umumiy sozlamalar
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)  # ❗️Selenium Manager o'zi mos driverni tanlaydi

    # Timeout sozlamalari
    driver.set_page_load_timeout(30)  # Sahifa yuklash uchun 30 soniya
    driver.implicitly_wait(0)  # Implicit wait 0 da qoldiramiz

    # CI muhitida user-agent o'rnatish
    if os.getenv("CI"):
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver