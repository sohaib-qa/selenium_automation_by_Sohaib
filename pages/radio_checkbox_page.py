from selenium.webdriver.remote.webdriver import WebDriver
from locators.radio_checkbox_locators import RadioCheckboxLocators


class RadioCheckboxPage:
    def __init__(self, driver):
        self.driver = driver

    def radiobutton(self):
        self.driver.find_element(*RadioCheckboxLocators.Male).click()

    def weakdaysmark(self,days):

        for i in days:
            self.driver.find_element(*RadioCheckboxLocators.Day(i)).click()
