from pages.alerts_page import Alerts_page
from utils.driver import get_driver
import logging
import pytest

# Loggerni sozlash
def setup_logger():
    import sys, logging
    logger = logging.getLogger("AlertsTest")
    logger.setLevel(logging.INFO)

    logger.handlers.clear()

    ch = logging.StreamHandler(sys.stdout)  # stdout
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(ch)
    logger.propagate = False
    return logger


@pytest.mark.parametrize("alert_type, expected_result", [
    ("simple", "Alert accepted"),  # simple alert
    ("timer", "Alert after 5 seconds"),  # timer alert
    ("confirm", "You selected Ok"),  # confirm alert
    ("prompt", "You entered Test User")  # prompt alert
])
def test_alerts(alert_type, expected_result):
    logger = setup_logger()
    driver = get_driver("https://demoqa.com/alerts")
    alerts_page = Alerts_page(driver)
    logger.info(f"STARTING TEST: {alert_type} alert functionality")
    if alert_type == "simple":
        alerts_page.click_simple_alert_button()
        alerts_page.handle_simple_alert()
        logger.info(f"Handled {alert_type} alert successfully.")
    elif alert_type == "timer":
        alerts_page.click_timer_alert_button()
        alerts_page.handle_timer_alert()
        logger.info(f"Handled {alert_type} alert successfully.")
    elif alert_type == "confirm":
        alerts_page.click_confirm_button()
        alerts_page.handle_confirm_alert_accept()
        logger.info(f"Handled {alert_type} alert successfully.")
    elif alert_type == "prompt":
        alerts_page.click_prompt_button()
        alerts_page.handle_prompt_alert("Test User")
        logger.info(f"Handled {alert_type} alert successfully.")
    result_text = alerts_page.get_alert_result_text()
    assert expected_result in result_text
    logger.info(f"Test completed successfully for {alert_type} alert.")
    driver.quit()
