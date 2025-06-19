from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    NEW_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    CODE_INPUT = (By.XPATH, "//input[@name='Введите код из письма']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
    PASSWORD_INPUT_ACTIV = (By.CSS_SELECTOR, ".input.text.input__textfield.text_type_main-default[type='password'][name='Введите новый пароль']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    VALUE_PASSWORD_IS_VISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]')