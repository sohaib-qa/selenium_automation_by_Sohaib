from selenium.webdriver.common.by import By


class RadioCheckboxLocators:
    Male = (By.ID, "male")
    Female = (By.ID, "female")
    # Monday = (By.XPATH, "input[@id='monday']")
    # Tuesday = (By.ID, "tuesday")
    # Wednesday = (By.ID, "wednesday")
    # Thursday = (By.ID, "thursday")
    # Friday = (By.ID, "friday")
    # Saturday = (By.ID, "saturday")
    # Sunday = (By.ID, "sunday")
    @staticmethod
    def Day(day):
        return By.ID, day.lower()

