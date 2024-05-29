from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestPersonalPage:

    def test_enter_in_personal_page(self, driver):
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

    def test_enter_in_constructor_from_constructor_button(self, driver):
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        title = driver.find_element(*TestLocators.CONSTRUCTOR_TITLE)
        assert title.text == 'Соберите бургер'

    def test_enter_in_constructor_from_logo(self, driver):
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.LOGO).click()
        title = driver.find_element(*TestLocators.CONSTRUCTOR_TITLE)
        assert title.text == 'Соберите бургер'

    def test_logout_button(self, driver):
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        assert '/login' in driver.current_url
