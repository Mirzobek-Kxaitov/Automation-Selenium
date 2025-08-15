import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = Options()

    # 👉 GitHub Actions’da CI=true bo‘ladi. Shuningdek HEADLESS=1/true bo‘lsa ham headless’ga o‘tamiz.
    if os.getenv("CI") or os.getenv("HEADLESS", "").lower() in ("1", "true", "yes"):
        options.add_argument("--headless=new")     # zamonaviy headless
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("--start-maximized")
        options.add_argument("--force-device-scale-factor=0.70")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=options)
    return driver
