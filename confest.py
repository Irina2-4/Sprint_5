import pytest
from selenium import webdriver
@pytest.fixture
def driver():
# инициализируем драйвер браузера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
# закроем браузер
    driver.quit()