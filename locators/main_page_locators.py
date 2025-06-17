from selenium.webdriver.common.by import By


class MainPageLocators:
    # Основные элементы
    MODAL_OVERLAY_LOCATOR = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    # Ингредиенты
    INGREDIENT_BUN = (By.XPATH, "//h2[contains(text(),'Булки')]/following-sibling::ul//a[1]")
    INGREDIENT_SAUCE = (By.XPATH, "//h2[contains(text(),'Соусы')]/following-sibling::ul//a[1]")
    INGREDIENT_MAIN = (By.XPATH, "//h2[contains(text(),'Начинки')]/following-sibling::ul//a[1]")

    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "/html/body/div/div/section[1]/div[1]/button")
    MODAL_INGREDIENT_NAME = (By.XPATH, "//h2[contains(@class,'text_type_main-medium')]")

    # Локатор откуда тянуть
    BURGER_INGREDIENT_LINK = (
    By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6[href='/ingredient/61c0c5a71d1f82001bdaaa6d']")

    # Локатор куда тянуть общий
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket')]")

    # Локатор куда тянуть для верхнего элемента
    CONSTRUCTOR_ELEMENT_TOP = (By.XPATH, "//li[@class='BurgerConstructor_basket__listItem__aWMu1 mr-4']/div[contains(., 'Перетяните булочку сюда (верх)') and @class='constructor-element constructor-element_pos_top']")

    # Локатор куда тянуть для нижнего элемента
    CONSTRUCTOR_ELEMENT_BOTTOM = (By.XPATH,"//li[@class='BurgerConstructor_basket__listItem__aWMu1 mr-4']/div[contains(., 'Перетяните булочку сюда (низ)') and @class='constructor-element constructor-element_pos_bottom']")

    # Счетчик ингредиента
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6[href='/ingredient/61c0c5a71d1f82001bdaaa6d'] .counter_counter__num__3nue1")

    # Кнопка оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Конструктор заказа
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket')]")

    # Лента заказов
    ORDER_FEED_SECTION = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")

    # Локатор для заказа в ленте
    ORDER_IN_FEED = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")

    # Модальное окно идентификатор заказа (при нажатии на кнопку "Оформить заказ")
    INGREDIENT_MODAL_DETAILS_TITLE = (By.CSS_SELECTOR, ".Modal_modal__contentBox__sCy8X")

    # Закрыть модальное окно идентификатор заказа
    CLOSE_BUTTON = (By.XPATH, "/html/body/div/div/section[1]/div[1]/button")
    MODAL_CLOSE_ORDER = (By.XPATH, "//button//*[local-name()='svg' and @width='24' and @height='24' and @fill='#F2F2F3']")











