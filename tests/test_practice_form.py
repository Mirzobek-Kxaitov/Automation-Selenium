import time
from selenium.webdriver.common.keys import Keys

from pages.practice_form import Practice_form
from utils.driver import get_driver

def test_fill_registration_form():
    driver = get_driver("https://demoqa.com/automation-practice-form")
    practice_page = Practice_form(driver)
    practice_page.fill_first_name("Mirzobek")
    practice_page.fill_last_name("Xaitov")
    practice_page.fill_email("mirzobekxayitov@mail.ru")
    practice_page.select_male_gender()
    practice_page.fill_mobile("9885535355")
    time.sleep(2)
    practice_page.fill_date_of_birth("30 Apr 1995")
    practice_page.fill_subject("math")
    practice_page.fill_subject("Physics")
    practice_page.select_sports_hobby()
    practice_page.select_reading_hobby()
    practice_page.select_music_hobby()
    practice_page.upload_picture(r"C:\Users\user\Desktop\POST LINKEDIN.jpg")
    practice_page.fill_current_address("Uzbekistan, Tashkent, Jobster Company - QA manager")
    practice_page.select_state_uttar_pradesh()
    practice_page.select_city_merrut()
    time.sleep(5)
    practice_page.submit_form()
    time.sleep(5)

    practice_page.verify_submitted_data(
        "Mirzobek",
        "Xaitov",
        "mirzobekxayitov@mail.ru",
        "Male",
        "9885535355",
        "30 April,1995",
        "Maths, Physics",
        "Sports, Reading, Music",
        "Uzbekistan, Tashkent, Jobster Company - QA manager",
        "Uttar Pradesh",
        "Merrut"
    )
    driver.quit()