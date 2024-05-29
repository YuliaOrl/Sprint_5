from selenium.webdriver.common.by import By


class TestLocators:
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"  # Кнопка «Войти в аккаунт»
    REGISTER_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"  # Кнопка «Зарегистрироваться»
    ENTER_BUTTON = By.XPATH, ".//button[text()='Войти']"  # Кнопка «Войти»
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"  # Кнопка «Выход»
    PERSONAL_PAGE_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"  # Кнопка для перехода в личный кабинет
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"  # Кнопка для перехода в конструктор
    REGISTER_LINK = By.LINK_TEXT, "Зарегистрироваться"  # Ссылка для перехода на страницу регистрации
    PROFILE_LINK = By.LINK_TEXT, "Профиль"  # Ссылка в разделе профиля
    ENTER_LINK = By.LINK_TEXT, "Войти"  # Ссылка для входа
    PASSWORD_RECOVERY_LINK = By.LINK_TEXT, 'Восстановить пароль'  # Ссылка для восстановления пароля
    NAME_INPUT = By.XPATH, ".//label[text()='Имя']/following-sibling::input"  # Форма ввода имени пользователя
    EMAIL_INPUT = By.XPATH, ".//label[text()='Email']/following-sibling::input"  # Форма ввода email пользователя
    PASSWORD_INPUT = By.XPATH, ".//label[text()='Пароль']/following-sibling::input"  # Форма ввода пароля пользователя
    LOGIN_INPUT = By.XPATH, ".//label[text()='Логин']/following-sibling::input"  # Форма ввода логина в профиле
    REGISTER_TITLE = By.XPATH, ".//h2[text()='Регистрация']"  # Заголовок страницы регистрации
    ENTER_TITLE = By.XPATH, ".//h2[text()='Вход']"  # Заголовок страницы входа
    CONSTRUCTOR_TITLE = By.XPATH, ".//h1[text()='Соберите бургер']"  # Заголовок страницы конструктора
    ERROR_NOTIFICATION = By.CSS_SELECTOR, ".input__error"  # Сообщение-ошибка о некорректном пароле
    LOGO = By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"  # Логотип
    TAB_SAUCES = By.XPATH, ".//span[text()='Соусы']/parent::div"  # Элемент для перехода в раздел "Соусы"
    TAB_STUFFING = By.XPATH, ".//span[text()='Начинки']/parent::div"  # Элемент для перехода в раздел "Начинки"
    TAB_BUN = By.XPATH, ".//span[text()='Булки']/parent::div"  # Элемент для перехода в раздел "Булки"


