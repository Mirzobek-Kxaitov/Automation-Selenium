# ================================================================================
# ALERTS TEST FILE
# ================================================================================
# Bu file alerts sahifasining barcha funksiyalarini test qilish uchun yaratilgan
# Har bir test method alohida alert type'ni tekshiradi


import time

from pages.alerts_page import Alerts_page
from utils.driver import get_driver

def test_smimple_alert_button():
    """
     TEST 1: Simple Alert Functionality

     Bu test oddiy alert'ning to'g'ri ishlashini tekshiradi:
     1. Button bosiladi
     2. Alert chiqishini kutadi
     3. Alert'ni yopadi

     Expected: Alert muvaffaqiyatli ochiladi va yopiladi
     """
    # Test setup - browser ochish va sahifaga borish
    driver = get_driver("https://demoqa.com/alerts")
    alerts_page = Alerts_page(driver)
    # Test logging - test boshlanganligi haqida ma'lumot
    alerts_page.logger.info("STARTING TEST: test_simple_alert_functionality")
    # ACTION 1: Simple alert button'ini bosish
    alerts_page.click_simple_alert_button()
    alerts_page.logger.info("Clicking simple alert button...")
    # ACTION 2: Alert'ni handle qilish (yopish)
    alerts_page.handle_simple_alert()
    alerts_page.logger.info("Handling simple alert...")
    # Test yakunlanishi
    alerts_page.logger.info("Test completed successfully!")
    # Cleanup - browser resurslarini tozalash
    time.sleep(3)
    driver.quit()

def test_timer_alert_functionality():
    """
    TEST 2: Timer Alert Functionality

    Bu test 5 soniyalik timer alert'ni tekshiradi:
    1. Button bosiladi
    2. 5 soniya kutiladi
    3. Alert chiqgandan keyin yopiladi

    Expected: 5 soniyadan keyin alert chiqadi va muvaffaqiyatli yopiladi
    """
    driver = get_driver("https://demoqa.com/alerts")
    alerts_page = Alerts_page(driver)
    alerts_page.logger.info("STARTING TEST: test_timer_alert_functionality")
    alerts_page.logger.info("Clicking timer alert button...")
    alerts_page.click_timer_alert_button()
    alerts_page.logger.info("Waiting for 5-second timer alert...")
    alerts_page.handle_timer_alert()
    alerts_page.logger.info("Handling timer alert")
    alerts_page.logger.info("Timer alert handled successfully!")
    time.sleep(3)
    driver.quit()

def test_confirm_alert_accept():
    driver = get_driver("https://demoqa.com/alerts")
    alerts_page = Alerts_page(driver)
    alerts_page.logger.info("STARTING TEST: test_confirm_alert_accept")
    alerts_page.logger.info("Clicking confirm button...")
    alerts_page.click_confirm_button()
    alerts_page.logger.info("Accepting confirm alert...")
    alerts_page.handle_confirm_alert_accept()
    result_text = alerts_page.get_confirm_result_text()
    assert "You selected Ok" in result_text
    alerts_page.logger.info(f"Result verified: {result_text}")
    time.sleep(5)
    driver.quit()

def test_confirm_alert_dismiss():
    driver = get_driver("https://demoqa.com/alerts")
    alerts_page = Alerts_page(driver)
    alerts_page.logger.info("STARTING TEST: test_confirm_alert_dismiss")
    alerts_page.logger.info("Clicking confirm button...")
    alerts_page.click_confirm_button()
    alerts_page.logger.info("Dismiss confirm alert...")
    alerts_page.handle_confirm_alert_dismiss()
    result_text = alerts_page.get_confirm_result_text()
    assert "You selected Cancel" in result_text
    alerts_page.logger.info(f"Result verified: {result_text}")
    time.sleep(5)
    driver.quit()

def test_prompt_alert_functionality():
    driver = get_driver("https://demoqa.com/alerts")
    alerts_page = Alerts_page(driver)
    alerts_page.logger.info("STARTING TEST: test_prompt_alert_functionality")
    alerts_page.logger.info("Clicking prompt button...")
    alerts_page.click_prompt_button()
    alerts_page.handle_prompt_alert("Test User")  # ← Bu qoldirilgan!
    alerts_page.logger.info("Accepting prompt alert...")
    result_text = alerts_page.get_prompt_result_text()
    assert "You entered Test User" in result_text  # ✅ specific
    alerts_page.logger.info(f" Result verified: {result_text}")
    time.sleep(5)
    driver.quit()