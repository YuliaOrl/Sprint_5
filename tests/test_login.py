import pytest
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestLogin:

    @pytest.mark.parametrize('locator', [TestLocators.LOGIN_BUTTON, TestLocators.PERSONAL_PAGE_BUTTON])
    def test_enter_from_button_login_and_personal_page(self, driver, locator):
        driver.find_element(*locator).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        login_profile = driver.find_element(*TestLocators.LOGIN_INPUT).get_attribute('value')
        name_profile = driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value')
        assert login_profile == USER_EMAIL and name_profile == USER_NAME

    @pytest.mark.parametrize('locator', [TestLocators.REGISTER_LINK, TestLocators.PASSWORD_RECOVERY_LINK])
    def test_enter_from_form_registration_and_password_recovery(self, driver, locator):
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*locator).click()
        driver.find_element(*TestLocators.ENTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        login_profile = driver.find_element(*TestLocators.LOGIN_INPUT).get_attribute('value')
        name_profile = driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value')
        assert login_profile == USER_EMAIL and name_profile == USER_NAME
