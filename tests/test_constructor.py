import pytest
from locators import TestLocators


class TestConstructor:

    @pytest.mark.parametrize('locator', [TestLocators.TAB_SAUCES, TestLocators.TAB_STUFFING])
    def test_switching_tab_sauces_and_stuffing(self, driver, locator):
        driver.find_element(*locator).click()
        class_name = driver.find_element(*locator).get_attribute('class')
        assert 'tab_tab_type_current' in class_name

    def test_switching_tab_bun(self, driver):
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        driver.find_element(*TestLocators.TAB_BUN).click()
        class_name = driver.find_element(*TestLocators.TAB_BUN).get_attribute('class')
        assert 'tab_tab_type_current' in class_name
