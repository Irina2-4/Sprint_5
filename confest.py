import pytest
from selenium import webdriver
@pytest.fixture
def driver():
# инициализируем драйвер браузера
    driver = webdriver.Chrome()

    yield driver
# закроем браузер
    #driver.quit()