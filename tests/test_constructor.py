from locators import ConstructorPageLocators
from actions import open_main_page, wait_clickable, wait_for_active_tab


def test_constructor_buns_tab(driver):
    open_main_page(driver)
    wait_clickable(driver, ConstructorPageLocators.SAUCES_TAB).click()
    wait_for_active_tab(driver, "Соусы")
    wait_clickable(driver, ConstructorPageLocators.BUNS_TAB).click()

    assert wait_for_active_tab(driver, "Булки").is_displayed()


def test_constructor_sauces_tab(driver):
    open_main_page(driver)
    wait_clickable(driver, ConstructorPageLocators.SAUCES_TAB).click()

    assert wait_for_active_tab(driver, "Соусы").is_displayed()


def test_constructor_fillings_tab(driver):
    open_main_page(driver)
    wait_clickable(driver, ConstructorPageLocators.FILLINGS_TAB).click()

    assert wait_for_active_tab(driver, "Начинки").is_displayed()
