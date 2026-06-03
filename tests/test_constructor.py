from locators import ConstructorPageLocators
from actions import open_main_page, wait_clickable, wait_for_tab_active


class TestConstructor:
    def test_constructor_buns_tab(self, driver):
        open_main_page(driver)
        wait_clickable(driver, ConstructorPageLocators.SAUCES_TAB).click()
        wait_for_tab_active(driver, ConstructorPageLocators.SAUCES_TAB)
        wait_clickable(driver, ConstructorPageLocators.BUNS_TAB).click()

        assert wait_for_tab_active(driver, ConstructorPageLocators.BUNS_TAB).is_displayed()

    def test_constructor_sauces_tab(self, driver):
        open_main_page(driver)
        wait_clickable(driver, ConstructorPageLocators.SAUCES_TAB).click()

        assert wait_for_tab_active(driver, ConstructorPageLocators.SAUCES_TAB).is_displayed()

    def test_constructor_fillings_tab(self, driver):
        open_main_page(driver)
        wait_clickable(driver, ConstructorPageLocators.FILLINGS_TAB).click()

        assert wait_for_tab_active(driver, ConstructorPageLocators.FILLINGS_TAB).is_displayed()
