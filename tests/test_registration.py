from data import INVALID_PASSWORD_ERROR_TEXT, INVALID_SHORT_PASSWORD, VALID_NAME
from helpers import generate_email
from locators import LoginPageLocators, RegisterPageLocators
from actions import open_registration_page, register_user, wait_clickable, wait_visible


def test_successful_registration(driver):
    register_user(driver)

    assert "/login" in driver.current_url
    assert wait_visible(driver, LoginPageLocators.PAGE_TITLE).is_displayed()


def test_registration_with_short_password_shows_error(driver):
    open_registration_page(driver)
    wait_visible(driver, RegisterPageLocators.NAME_INPUT).send_keys(VALID_NAME)
    wait_visible(driver, RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    wait_visible(driver, RegisterPageLocators.PASSWORD_INPUT).send_keys(INVALID_SHORT_PASSWORD)
    wait_clickable(driver, RegisterPageLocators.REGISTER_BUTTON).click()

    error_message = wait_visible(driver, RegisterPageLocators.INVALID_PASSWORD_ERROR)

    assert error_message.text == INVALID_PASSWORD_ERROR_TEXT
