from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestLogin:

    def test_login_button_in_maine_page(self, driver):
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        login_profile = driver.find_element(*TestLocators.LOGIN_INPUT).get_attribute('value')
        name_profile = driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value')
        assert login_profile == USER_EMAIL and name_profile == USER_NAME

    def test_login_button_personal_cabinet(self, driver):
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        login_profile = driver.find_element(*TestLocators.LOGIN_INPUT).get_attribute('value')
        name_profile = driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value')
        assert login_profile == USER_EMAIL and name_profile == USER_NAME

    def test_login_button_in_registration_form(self, driver):
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.REGISTER_TITLE))
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


    def test_login_button_in_password_recovery_form(self, driver):
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.PASSWORD_RECOVERY_LINK).click()
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

