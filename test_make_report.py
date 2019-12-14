import time


def test_go_to_login_page_register_and_find_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    time.sleep(5)
    login_link=browser.find_element_by_css_selector('#login_link')
    login_link.click()
    registration_email=browser.find_element_by_name("registration-email")
    input_email=str(time.time()) + "@fakemail.org"
    registration_email.send_keys(input_email)
    registration_password1=browser.find_element_by_id('id_registration-password1')
    time.sleep(1)
    input_password = str(time) + "258"
    registration_password1.send_keys(input_password)
    registration_password2 = browser.find_element_by_id('id_registration-password2')
    registration_password2.send_keys(input_password)
    regictration_button = browser.find_element_by_css_selector('#register_form > button')
    regictration_button.click()
    success_message = browser.find_element_by_css_selector('.alertinner')
    assert success_message, "User cant register"

