import time

from pages.radio_checkbox_page import RadioCheckboxPage


def test_radio(driver):
    driver.get("https://testautomationpractice.blogspot.com")
    radio = RadioCheckboxPage(driver)
    radio.radiobutton()
    radio.weakdaysmark(["monDay", "Tuesday"])