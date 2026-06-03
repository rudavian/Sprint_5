from locators import ForgotPasswordPageLocators, LoginPageLocators, MainPageLocators, RegisterPageLocators
from actions import (
    login_user,
    open_forgot_password_page,
    open_main_page,
    open_registration_page,
    register_user,
    wait_clickable,
    wait_for_login_success,
    wait_visible,
)


def test_login_from_main_page_login_button(driver):
    user_data = register_user(driver)
    open_main_page(driver)
    wait_clickable(driver, MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
    wait_visible(driver, LoginPageLocators.PAGE_TITLE)
    login_user(driver, user_data["email"], user_data["password"])

    assert wait_for_login_success(driver).is_displayed()


def test_login_from_personal_account_button(driver):
    user_data = register_user(driver)
    open_main_page(driver)
    wait_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    wait_visible(driver, LoginPageLocators.PAGE_TITLE)
    login_user(driver, user_data["email"], user_data["password"])

    assert wait_for_login_success(driver).is_displayed()


def test_login_from_registration_page(driver):
    user_data = register_user(driver)
    open_registration_page(driver)
    wait_clickable(driver, RegisterPageLocators.LOGIN_LINK).click()
    wait_visible(driver, LoginPageLocators.PAGE_TITLE)
    login_user(driver, user_data["email"], user_data["password"])

    assert wait_for_login_success(driver).is_displayed()


def test_login_from_forgot_password_page(driver):
    user_data = register_user(driver)
    open_forgot_password_page(driver)
    wait_clickable(driver, ForgotPasswordPageLocators.LOGIN_LINK).click()
    wait_visible(driver, LoginPageLocators.PAGE_TITLE)
    login_user(driver, user_data["email"], user_data["password"])

    assert wait_for_login_success(driver).is_displayed()
