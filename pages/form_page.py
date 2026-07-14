from locators.form_locators import FormLocators

class FormPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(*FormLocators.NAME).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*FormLocators.EMAIL).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*FormLocators.PHONE).send_keys(phone)

    def enter_message(self, message):
        self.driver.find_element(*FormLocators.TEXTAREA).send_keys(message)

