from Locators import Main_Locators,Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from confest import driver
from url import URL

class TestEnterToAccount:
    # Вход по кнопке "Войти в аккаунт"
    def test_login_with_the_correct_password(self,driver):
        driver.maximize_window()
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        # Поиск кнопки Войти в аккаунт
        element = driver.find_element(*Locators.BUTTON_LOGIN)
        element.click()
        # Ожидание окна ввода данных
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.LOGIN))
        # Ввод почты пользователя
        element = driver.find_element(*Main_Locators.email)
        element.send_keys("imorgunova15@yandex.ru")
        # Ввод пароля пользователя
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("1234567")
        # Клик на кнопку "Войти"
        element = driver.find_element(*Main_Locators.LOGIN)
        element.click()

        WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_B))
        assert driver.find_element(*Locators.ORDER_B)

        # Вход по кнопке "Личный кабинет"
    def test_login_through_personal_account(self, driver):
        driver.maximize_window()
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.BUTTON_ACCOUNT))
        # Поиск кнопки Войти в аккаунт
        element = driver.find_element(*Main_Locators.BUTTON_ACCOUNT)
        element.click()
        # Ожидание окна ввода данных
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.LOGIN))
        # Ввод почты пользователя
        element = driver.find_element(*Main_Locators.email)
        element.send_keys("imorgunova15@yandex.ru")
        # Ввод пароля пользователя
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("1234567")
        # Клик на кнопку "Войти"
        element = driver.find_element(*Main_Locators.LOGIN)
        element.click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_B))
        assert driver.find_element(*Locators.ORDER_B)

        # Вход через кнопку "Войти" в форме регистрации"
    def test_login_through_login_button_in_registration_form(self, driver):
        driver.maximize_window()
        driver.get(URL.REG)
        #Ожидание ссылки "Войти"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.ACC_BUTTON))
        # Переход по ссылке
        element = driver.find_element(*Locators.ACC_BUTTON)
        element.click()
        # Ожидание окна ввода данных
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.LOGIN))
        # Ввод почты пользователя
        element = driver.find_element(*Main_Locators.email)
        element.send_keys("imorgunova15@yandex.ru")
        # Ввод пароля пользователя
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("1234567")
        # Клик на кнопку "Войти"
        element = driver.find_element(*Main_Locators.LOGIN)
        element.click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_B))
        assert driver.find_element(*Locators.ORDER_B)

    #Вход через кнопку в форме восстановления пароля
    def test_login_through_password_recovery_form(self,driver):
        driver.maximize_window()
        driver.get(URL.PASSWORD_RECOVERY)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.ACC_BUTTON))
        # Поиск кнопки "Войти в аккаунт"
        element = driver.find_element(*Locators.ACC_BUTTON)
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
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_B))
        assert driver.find_element(*Locators.ORDER_B)

    def test_log_out_of_account(self,driver):
        driver.maximize_window()
        # Переход на главную страницу
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        # Поиск кнопки Личный кабинет
        element = driver.find_element(*Locators.BUTTON_LOGIN)
        element.click()
        # Ввод логина пользователя
        element = driver.find_element(*Main_Locators.email)
        element.send_keys("imorgunova15@yandex.ru")
        # Ввод пароля пользователя
        element = driver.find_element(*Main_Locators.password)
        element.send_keys("1234567")
        # Клик на кнопку "Войти"
        element = driver.find_element(*Main_Locators.LOGIN)
        element.click()
        #Ожидание, пока кнопка "Личный кабинет" не станет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.BUTTON_ACCOUNT))
        element = driver.find_element(*Main_Locators.BUTTON_ACCOUNT)
        element.click()
        #Ожидание, пока кнопка "Выход" не станет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_EXIT))
        element = driver.find_element(*Locators.BUTTON_EXIT)
        element.click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.LOGIN))

        assert driver.current_url == URL.LOGIN