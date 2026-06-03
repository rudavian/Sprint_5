from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import DEFAULT_WAIT_TIMEOUT, INVALID_PASSWORD_ERROR_TEXT, VALID_NAME
from helpers import generate_user_data
from locators import (
    ConstructorPageLocators,
    ForgotPasswordPageLocators,
    LoginPageLocators,
    MainPageLocators,
    ProfilePageLocators,
    RegisterPageLocators,
)
from urls import BASE_URL, FORGOT_PASSWORD_URL, LOGIN_URL, REGISTER_URL


def wait_visible(driver, locator, timeout=DEFAULT_WAIT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_clickable(driver, locator, timeout=DEFAULT_WAIT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def wait_url_contains(driver, url_part, timeout=DEFAULT_WAIT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.url_contains(url_part))


def open_main_page(driver):
    driver.get(BASE_URL)
    wait_visible(driver, MainPageLocators.CONSTRUCTOR_SECTION)


def open_login_page(driver):
    driver.get(LOGIN_URL)
    wait_visible(driver, LoginPageLocators.PAGE_TITLE)


def open_registration_page(driver):
    driver.get(REGISTER_URL)
    wait_visible(driver, RegisterPageLocators.PAGE_TITLE)


def open_forgot_password_page(driver):
    driver.get(FORGOT_PASSWORD_URL)
    wait_visible(driver, ForgotPasswordPageLocators.PAGE_TITLE)


def login_user(driver, email, password):
    wait_visible(driver, LoginPageLocators.EMAIL_INPUT).send_keys(email)
    wait_visible(driver, LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    wait_clickable(driver, LoginPageLocators.LOGIN_BUTTON).click()


def wait_for_login_success(driver):
    return wait_visible(driver, MainPageLocators.PLACE_ORDER_BUTTON)


def wait_for_active_tab(driver, tab_name, timeout=DEFAULT_WAIT_TIMEOUT):
    def active_tab_matches(browser):
        active_tab = browser.find_element(*ConstructorPageLocators.ACTIVE_TAB)
        return active_tab if active_tab.text == tab_name else False

    return WebDriverWait(driver, timeout).until(active_tab_matches)


def register_user(driver, name=VALID_NAME, attempts=5):
    for _ in range(attempts):
        user_data = generate_user_data(name=name)
        open_registration_page(driver)
        wait_visible(driver, RegisterPageLocators.NAME_INPUT).send_keys(user_data["name"])
        wait_visible(driver, RegisterPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
        wait_visible(driver, RegisterPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
        wait_clickable(driver, RegisterPageLocators.REGISTER_BUTTON).click()

        try:
            wait_visible(driver, LoginPageLocators.PAGE_TITLE, timeout=10)
            return user_data
        except TimeoutException:
            errors = driver.find_elements(*RegisterPageLocators.INVALID_PASSWORD_ERROR)
            if errors:
                raise AssertionError(INVALID_PASSWORD_ERROR_TEXT)

    raise AssertionError("Не удалось зарегистрировать пользователя с уникальным email за несколько попыток.")


def register_and_login_user(driver):
    user_data = register_user(driver)
    login_user(driver, user_data["email"], user_data["password"])
    wait_for_login_success(driver)
    return user_data


def open_personal_account(driver):
    wait_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    wait_url_contains(driver, "/account/profile")
    wait_visible(driver, ProfilePageLocators.PROFILE_ACTIVE_LINK)
