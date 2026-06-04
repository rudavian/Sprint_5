from data import INVALID_PASSWORD_ERROR_TEXT, INVALID_SHORT_PASSWORD, VALID_NAME
from helpers import generate_email, generate_password
from locators import LoginPageLocators, RegisterPageLocators
from actions import open_registration_page, wait_clickable, wait_visible


class TestRegistration:
    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password()

        open_registration_page(driver)
        wait_visible(driver, RegisterPageLocators.NAME_INPUT).send_keys(VALID_NAME)
        wait_visible(driver, RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        wait_visible(driver, RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        wait_clickable(driver, RegisterPageLocators.REGISTER_BUTTON).click()

        login_title = wait_visible(driver, LoginPageLocators.PAGE_TITLE)

        assert "/login" in driver.current_url
        assert login_title.is_displayed()

    def test_registration_with_short_password_shows_error(self, driver):
        open_registration_page(driver)
        wait_visible(driver, RegisterPageLocators.NAME_INPUT).send_keys(VALID_NAME)
        wait_visible(driver, RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        wait_visible(driver, RegisterPageLocators.PASSWORD_INPUT).send_keys(INVALID_SHORT_PASSWORD)
        wait_clickable(driver, RegisterPageLocators.REGISTER_BUTTON).click()

        error_message = wait_visible(driver, RegisterPageLocators.INVALID_PASSWORD_ERROR)

        assert error_message.text == INVALID_PASSWORD_ERROR_TEXT
