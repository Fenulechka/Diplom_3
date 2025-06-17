from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON_AUTH = (By.XPATH, "//button[contains(text(), 'Войти')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    PERSONAL_CABINET_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
