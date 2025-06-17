import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Вставить новый пароль")
    def set_new_password(self, new_password):
        self.input_text(ResetPasswordPageLocators.NEW_PASSWORD_INPUT, new_password)

    @allure.step("Проверить, что значение поля password отображается")
    def check_displaying_password_value(self):
        return self.wait_for_element(ResetPasswordPageLocators.VALUE_PASSWORD_IS_VISIBLE)

    @allure.step("Переключение видимости введённого пароля")
    def toggle_password_visibility(self):
        self.click_element(ResetPasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON)


