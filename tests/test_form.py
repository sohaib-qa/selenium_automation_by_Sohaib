from pages.form_page import FormPage

def test_fill_form(driver):

    driver.get("https://testautomationpractice.blogspot.com")

    form = FormPage(driver)

    form.enter_name("Sohaib Ahmad")
    form.enter_email("sohaib@gmail.com")
    form.enter_phone("03001234567")
    form.enter_message("Learning Selenium POM")