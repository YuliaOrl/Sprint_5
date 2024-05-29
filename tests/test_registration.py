from data import *
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


def user_email():
    email = f'yulia_orlova_9{random.randint(1000, 9999)}@yandex.ru'
    return email


def user_password():
    password = random.randint(100000, 9999999999)
    return password


def user_incorrect_password():
    password = random.randint(1, 99999)
    return password


class TestRegistration:

    def test_registration_user_correct_data(self, driver):
        email = user_email()
        password = user_password()
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.REGISTER_TITLE))
        driver.find_element(*TestLocators.NAME_INPUT).send_keys(USER_NAME)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_TITLE))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        login_profile = driver.find_element(*TestLocators.LOGIN_INPUT).get_attribute('value')
        name_profile = driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value')
        assert login_profile == email and name_profile == USER_NAME

    def test_registration_user_incorrect_password(self, driver):
        email = user_email()
        incorrect_password = user_incorrect_password()
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.REGISTER_TITLE))
        driver.find_element(*TestLocators.NAME_INPUT).send_keys(USER_NAME)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(incorrect_password)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        notification = driver.find_element(*TestLocators.ERROR_NOTIFICATION).text
        assert notification == 'Некорректный пароль'
