from datetime import time

from selenium.webdriver.common.by import By
from Locators import Main_Locators,Authtor_Locators,Reg_Locators,Pass_Recover_Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from confest import driver
from selenium import webdriver
from url import URL

class TestProfile:
    def test_auth_from_main_page(self,driver):
        # Вход через кнопку "Личный кабинет"
        driver.maximize_window()
        driver.get(URL.MAIN)
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(Authtor_Locators.PER_ACC))


        # Поиск кнопки Личный кабинет
        element = driver.find_element(*Authtor_Locators.PER_ACC)
        element.click()

        # Ожидание окна ввода данных
        WebDriverWait(driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, './/input[@name="name"]')))
        # Ввод почты
        element = driver.find_element(By.XPATH, './/input[@name="name"]')
        element.send_keys("irinka2035@yandex.ru")

        # Ввод пароля
        element = driver.find_element(By.XPATH, './/input[@name="Пароль"]')
        element.send_keys("1234567")

        # Клик на кнопку вход
        element = driver.find_element(*Authtor_Locators.LOGIN)
        element.click()

        driver.quit()

       # WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(*Locators.LOGIN))
        #element = driver.find_element(*Locators.LOGIN)
       # element.click()
        #WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable(*Locators.ORDER_B))
        #assert driver.find_element(*Locators.ORDER_B)