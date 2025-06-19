from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    RESET_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
