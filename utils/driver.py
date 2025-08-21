from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
def get_driver():
    options = Options()
    if os.getenv("CI") or os.getenv("HEADLESS", "").lower() in ("1","true","yes"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
        options.add_argument("--force-device-scale-factor=0.70")

    driver = webdriver.Chrome(options=options)  # ❗️Selenium Manager o‘zi mos driverni tanlaydi
    driver.implicitly_wait(0)
    return driver