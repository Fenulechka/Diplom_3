import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from pages.reset_password_page import ResetPasswordPage
from locators.main_page_locators import MainPageLocators


class ForgotPasswordPage(BasePage):

    @allure.step("Ввести емейл, нажать кнопку восстановления пароля")
    def restore_password(self, email):
        self.element_is_not_visible(MainPageLocators.MODAL_OVERLAY_LOCATOR)
        self.input_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
        return ResetPasswordPage(self.driver)


