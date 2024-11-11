from Locators import Locators,Main_Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from confest import driver
from url import URL
from random import randint
class TestRegistration:

    # Успешная регистрация
    def test_button_registration(self,driver):

        driver.maximize_window()
        driver.get(URL.REG)
        #Генерация рандомного адреса
        email = f'imorgunova{randint(5,500)}@yandex.ru'
        #Ожидание доступности ввода информации
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.REG))
        # Ввод имени пользователя
        element = driver.find_element(*Locators.NAME)
        element.send_keys('Ира')
        # Ввод почты пользователя
        element = driver.find_element(*Locators.EMAIL)
        element.send_keys(email)
        # Ввод пароля пользователя
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("1234567")
        # Поиск кнопки "Зарегистрироваться"
        element = driver.find_element(*Locators.REG)
        element.click()
        #Ожидание возможности войти в аккант(поле для ввода логина и пароля)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.LOGIN))
        assert driver.find_element(*Main_Locators.LOGIN)

    # Проверка ошибки при вводе некорректного пароля

    def test_password_incorrect(self, driver):

        driver.maximize_window()
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.BUTTON_ACCOUNT))
        # Поиск кнопки Личный кабинет
        element = driver.find_element(*Main_Locators.BUTTON_ACCOUNT)
        element.click()
        # Ожидание доступности окна ввода данных
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.LOGIN))
        # Ввод почты пользователя
        element = driver.find_element(*Main_Locators.email)
        element.send_keys("imorgunova15@yandex.ru")
        # Ввод пароля пользователя
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("123")
        # Клик на кнопку вход
        element = driver.find_element(*Main_Locators.LOGIN)
        element.click()
        assert driver.find_element(*Locators.BAD_PASSWORD)