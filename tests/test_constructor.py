from locators import TestLocators


class TestConstructor:

    def test_switching_tab_sauces(self, driver):
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        class_name = driver.find_element(*TestLocators.TAB_SAUCES).get_attribute('class')
        assert 'tab_tab_type_current' in class_name

    def test_switching_tab_stuffing(self, driver):
        driver.find_element(*TestLocators.TAB_STUFFING).click()
        class_name = driver.find_element(*TestLocators.TAB_STUFFING).get_attribute('class')
        assert 'tab_tab_type_current' in class_name

    def test_switching_tab_bun(self, driver):
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        driver.find_element(*TestLocators.TAB_BUN).click()
        class_name = driver.find_element(*TestLocators.TAB_BUN).get_attribute('class')
        assert 'tab_tab_type_current' in class_name
