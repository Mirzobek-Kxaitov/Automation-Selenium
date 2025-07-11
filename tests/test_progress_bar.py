from pages.progress_bar_page import ProgressBarPage
from utils.driver import get_driver


def test_progress_bar_basic_functionality():
    driver = get_driver("https://demoqa.com/progress-bar")
    page = ProgressBarPage(driver)

    initial_progress = int(page.get_progress_value())
    print(f"initial progress: {initial_progress}%")

    page.click_start_stop_button()
    page.wait_until_complete()

    final_progress = int(page.get_progress_value())
    print(f"Final progress: {final_progress}%")
    assert final_progress == 100, f"Expected 100% but got {final_progress}%"

    driver.quit()
