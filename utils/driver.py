from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


def get_driver():
    options = Options()

    # CI environment yoki headless rejim
    if os.getenv("CI") or os.getenv("HEADLESS", "").lower() in ("1", "true", "yes"):
        # GitHub Actions uchun optimallashtirilgan sozlamalar
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-features=VizDisplayCompositor")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-images")  # Rasmlarni yuklamaslik (tezroq)
        options.add_argument("--disable-javascript")  # Agar JS kerak bo'lmasa

        # Performance optimizatsiyalari
        options.add_argument("--memory-pressure-off")
        options.add_argument("--max_old_space_size=4096")

        # Network optimizatsiyalari
        options.add_argument("--aggressive-cache-discard")
        options.add_argument("--disable-background-timer-throttling")

    else:
        # Local development uchun
        options.add_argument("--start-maximized")
        options.add_argument("--force-device-scale-factor=0.70")

    # Umumiy optimizatsiyalar
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Logging ni kamaytirish
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options)

    # Timeout'larni qisqartirish CI uchun
    if os.getenv("CI"):
        driver.implicitly_wait(5)  # CI da qisqaroq kutish
        driver.set_page_load_timeout(30)  # Sahifa yuklash timeout
    else:
        driver.implicitly_wait(10)  # Local da ko'proq kutish
        driver.set_page_load_timeout(60)

    return driver