from selenium.webdriver.common.by import By

class Constructor_Locators:
    BUNS_BUR = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")  # Ссылка на булки
    SAUCES_BUR = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")  # Ссылка на соусы
    FILLINGS_BUR = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")  # Ссылка на начинки
    BUTTON_CONSTR = (By.XPATH, ".//p[text() = 'Конструктор']")  # Ссылка "Конструктор"

class Main_Locators:
    email = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    LOGIN = (By.XPATH, "//button[text() = 'Войти']") # Кнопка войти
    password = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    BUTTON_ACCOUNT = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный кабинет"

class Locators:

    NAME = (By.XPATH, "(.//input[@name = 'name'])[1]")  # Поле ввода имени
    EMAIL = (By.XPATH, "(.//input[@name = 'name'])[2]")  # Поле ввода email
    BUTTON_LOGIN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка войти в аккаунт
    REC_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Ссылка "Восстановить пароль"
    BAD_PASSWORD = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка при вводе некорректного пароля
    REG = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ORDER_B = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка оформить заказ
    ACC_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")  # Ссылка "Войти"
    BUTTON_EXIT = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка "Выход"

    CLICK_LOGO = (By.XPATH, ".//header//div/a[@href='/']")  # Логотип

    # Cсылки переключения внутри конструктора

    LINK_BUNS = (By.XPATH, ".//span[text() = 'Булки']")  # Ссылка переключения на булки
    LINK_SAUCES = (By.XPATH, ".//span[text() = 'Соусы']")  # Ссылка переключения на соусы
    LINK_FILLINGS = (By.XPATH, ".//span[text() = 'Начинки']")  # Ссылка переключения на начинки