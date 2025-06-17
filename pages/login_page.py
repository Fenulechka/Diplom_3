import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Кликнуть на ссылку Восстановить пароль на странице входа")
    def go_to_forgot_password_page(self):
        link = self.wait_for_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
        link.click()

    @allure.step("Авторизация пользователя")
    def user_authorization(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON_AUTH)

