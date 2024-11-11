from Locators import Main_Locators,Locators,Constructor_Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from confest import driver
from url import URL

class TestNavigateSectionInConstructor:

    # Переход к разделу "Начинки"

    def test_go_link_fillings(self,driver):
        driver.maximize_window()
        # Переход на главную страницу
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Main_Locators.BUTTON_ACCOUNT))

        #Ожидание, когда кнопка "Конструктор" станет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Constructor_Locators.BUTTON_CONSTR))
        element = driver.find_element(*Constructor_Locators.BUTTON_CONSTR)
        element.click()
        # Переход к разделу "Начинки"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LINK_FILLINGS))
        element = driver.find_element(*Locators.LINK_FILLINGS)
        element.click()
        fillings = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(Constructor_Locators.FILLINGS_BUR))
        assert fillings

    # Переход к разделу "Соусы"
    def test_go_link_sauces(self, driver):
        driver.maximize_window()
        # Переход на главную страницу
        driver.get(URL.MAIN)
        # Ожидание, когда ссылка "Соусы" станет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LINK_SAUCES))
        element = driver.find_element(*Locators.LINK_SAUCES)
        element.click()

        sauces = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(Constructor_Locators.SAUCES_BUR))
        assert sauces

    # Переход к разделу "Булки"
    def test_go_link_buns(self,driver):
        driver.maximize_window()

        # Переход на главную страницу
        driver.get(URL.MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Constructor_Locators.BUTTON_CONSTR))

        # Ожидание, когда ссылка "Начинки" станет кликабельна
        element = driver.find_element(*Locators.LINK_FILLINGS)
        element.click()

        # Переход к разделу "Булки"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LINK_BUNS))
        element = driver.find_element(*Locators.LINK_BUNS)
        element.click()

        buns = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Constructor_Locators.BUNS_BUR))
        assert buns