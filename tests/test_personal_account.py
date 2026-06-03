from locators import LoginPageLocators, MainPageLocators, ProfilePageLocators
from actions import (
    open_personal_account,
    register_and_login_user,
    wait_clickable,
    wait_visible,
)
from urls import BASE_URL


def test_go_to_personal_account(driver):
    register_and_login_user(driver)
    wait_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    assert wait_visible(driver, ProfilePageLocators.PROFILE_ACTIVE_LINK).is_displayed()


def test_go_to_constructor_from_personal_account_by_constructor_link(driver):
    register_and_login_user(driver)
    open_personal_account(driver)
    wait_clickable(driver, ProfilePageLocators.CONSTRUCTOR_LINK).click()
    wait_visible(driver, MainPageLocators.CONSTRUCTOR_SECTION)

    assert driver.current_url == BASE_URL


def test_go_to_constructor_from_personal_account_by_logo(driver):
    register_and_login_user(driver)
    open_personal_account(driver)
    wait_clickable(driver, ProfilePageLocators.STELLAR_BURGERS_LOGO).click()
    wait_visible(driver, MainPageLocators.CONSTRUCTOR_SECTION)

    assert driver.current_url == BASE_URL


def test_logout_from_personal_account(driver):
    register_and_login_user(driver)
    open_personal_account(driver)
    wait_clickable(driver, ProfilePageLocators.LOGOUT_BUTTON).click()

    assert wait_visible(driver, LoginPageLocators.PAGE_TITLE).is_displayed()
