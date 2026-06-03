from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Войти в аккаунт» на главной странице.
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
    # Ссылка «Личный Кабинет» в шапке сайта.
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "header a[href='/account']")
    # Ссылка «Конструктор» в шапке сайта.
    CONSTRUCTOR_LINK = (By.XPATH, "//header//a[@href='/' and .//p[normalize-space()='Конструктор']]")
    # Логотип Stellar Burgers в шапке сайта.
    STELLAR_BURGERS_LOGO = (By.XPATH, "//header//a[@href='/' and not(.//p)]")
    # Вкладка «Булки» в конструкторе.
    BUNS_TAB = (By.XPATH, "//div[./span[normalize-space()='Булки']]")
    # Вкладка «Соусы» в конструкторе.
    SAUCES_TAB = (By.XPATH, "//div[./span[normalize-space()='Соусы']]")
    # Вкладка «Начинки» в конструкторе.
    FILLINGS_TAB = (By.XPATH, "//div[./span[normalize-space()='Начинки']]")
    # Активная вкладка конструктора ингредиентов.
    ACTIVE_CONSTRUCTOR_TAB = (By.CSS_SELECTOR, "div[class*='tab_tab_type_current']")
    # Основной контейнер конструктора на главной странице.
    CONSTRUCTOR_SECTION = (
        By.CSS_SELECTOR,
        "main section[class*='BurgerIngredients_ingredients']",
    )
    # Кнопка «Оформить заказ» для проверки успешной авторизации.
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    # Основной контент главной страницы для smoke-проверки.
    MAIN_CONTENT = CONSTRUCTOR_SECTION


class LoginPageLocators:
    # Заголовок страницы входа.
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Вход']")
    # Поле ввода Email на странице входа.
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    # Поле ввода пароля на странице входа.
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")
    # Кнопка «Войти» в форме входа.
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    # Ссылка «Зарегистрироваться» под формой входа.
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")
    # Ссылка «Восстановить пароль» под формой входа.
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")


class RegisterPageLocators:
    # Заголовок страницы регистрации.
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Регистрация']")
    # Поле ввода имени на странице регистрации.
    NAME_INPUT = (By.XPATH, "//label[normalize-space()='Имя']/following-sibling::input")
    # Поле ввода Email на странице регистрации.
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    # Поле ввода пароля на странице регистрации.
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")
    # Кнопка «Зарегистрироваться» в форме регистрации.
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
    # Ссылка «Войти» под формой регистрации.
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    # Сообщение об ошибке для некорректного короткого пароля.
    INVALID_PASSWORD_ERROR = (By.XPATH, "//p[normalize-space()='Некорректный пароль']")


class ForgotPasswordPageLocators:
    # Заголовок страницы восстановления пароля.
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Восстановление пароля']")
    # Поле ввода Email на странице восстановления пароля.
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    # Ссылка «Войти» под формой восстановления пароля.
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")


class ProfilePageLocators:
    # Активная ссылка «Профиль» в личном кабинете.
    PROFILE_LINK = (By.CSS_SELECTOR, "a[href='/account/profile']")
    # Активный маркер текущей страницы профиля.
    PROFILE_ACTIVE_LINK = (By.CSS_SELECTOR, "a[href='/account/profile'][class*='Account_link_active']")
    # Кнопка «Выход» в личном кабинете.
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")
    # Ссылка «Конструктор» в шапке из личного кабинета.
    CONSTRUCTOR_LINK = (By.XPATH, "//header//a[@href='/' and .//p[normalize-space()='Конструктор']]")
    # Логотип Stellar Burgers в шапке личного кабинета.
    STELLAR_BURGERS_LOGO = (By.XPATH, "//header//a[@href='/' and not(.//p)]")
    # Активная ссылка «Личный Кабинет» в шапке профиля.
    PERSONAL_ACCOUNT_ACTIVE_LINK = (
        By.CSS_SELECTOR,
        "header a[href='/account'][class*='AppHeader_header__link_active']",
    )


class ConstructorPageLocators:
    # Фрагмент CSS-класса активной вкладки конструктора.
    ACTIVE_TAB_CLASS = "tab_tab_type_current"
    # Вкладка «Булки» в конструкторе.
    BUNS_TAB = (By.XPATH, "//div[./span[normalize-space()='Булки']]")
    # Вкладка «Соусы» в конструкторе.
    SAUCES_TAB = (By.XPATH, "//div[./span[normalize-space()='Соусы']]")
    # Вкладка «Начинки» в конструкторе.
    FILLINGS_TAB = (By.XPATH, "//div[./span[normalize-space()='Начинки']]")
    # Активная вкладка конструктора по классу состояния.
    ACTIVE_TAB = (By.CSS_SELECTOR, "div[class*='tab_tab_type_current']")
    # Основной контейнер конструктора ингредиентов.
    CONSTRUCTOR_SECTION = (
        By.CSS_SELECTOR,
        "main section[class*='BurgerIngredients_ingredients']",
    )
