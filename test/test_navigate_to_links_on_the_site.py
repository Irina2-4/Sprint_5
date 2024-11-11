from Locators import Main_Locators,Constructor_Locators, Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from confest import driver
from url import URL

class TestNavigateToLinksOnTheSite:

    # Переход по клику в личный кабинет
    def test_log_in_to_account(self,driver):
        driver.maximize_window()
        # Переход на главную страницу
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.BUTTON_ACCOUNT))
        # Поиск кнопки Личный кабинет
        element = driver.find_element(*Main_Locators.BUTTON_ACCOUNT)
        element.click()
        # Ввод почты пользователя
        element = driver.find_element(*Main_Locators.email)
        element.send_keys("imorgunova15@yandex.ru")
        #Ввод пароля пользователя
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("1234567")
        # Клик на кнопку вход
        element = driver.find_element(*Main_Locators.LOGIN)
        element.click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.LOGIN))
        assert driver.find_element(*Main_Locators.LOGIN)


    # Переход по клику на "Конструктор"
    def test_go_constr(self,driver):
        driver.maximize_window()
        # Переход на главную страницу
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.BUTTON_ACCOUNT))

        # Поиск кнопки Личный кабинет
        element = driver.find_element(*Main_Locators.BUTTON_ACCOUNT)
        element.click()
        # Ввод почты пользователя
        element = driver.find_element(*Main_Locators.email)
        element.send_keys("imorgunova15@yandex.ru")
        # Ввод пароля пользователя
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("1234567")
        # Клик на кнопку вход
        element = driver.find_element(*Main_Locators.LOGIN)
        element.click()
        #Ожидание, когда кнопка "Конструктор" станет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Constructor_Locators.BUTTON_CONSTR))
        element = driver.find_element(*Constructor_Locators.BUTTON_CONSTR)
        element.click()
        assert driver.current_url == URL.MAIN

# Переход на логотип Stellar Burger
    def test_go_stellar_burger(self,driver):
        driver.maximize_window()
        # Переход на главную страницу
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.BUTTON_ACCOUNT))
        # Поиск кнопки Личный кабинет
        element = driver.find_element(*Main_Locators.BUTTON_ACCOUNT)
        element.click()
        element = driver.find_element(*Main_Locators.email)
        element.send_keys("imorgunova15@yandex.ru")
        # Ввод пароля
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("1234567")
        # Клик на кнопку вход
        element = driver.find_element(*Main_Locators.LOGIN)
        element.click()
        #Ожидание, когда "Логотип" станет кликабелен
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.CLICK_LOGO))
        element = driver.find_element(*Locators.CLICK_LOGO)
        element.click()

        assert driver.current_url == URL.MAIN

