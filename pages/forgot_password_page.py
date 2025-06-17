import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from pages.reset_password_page import ResetPasswordPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return super().get_current_url()

    @allure.step("Ввести емейл, нажать кнопку восстановления пароля")
    def restore_password(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY_LOCATOR))
        self.input_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
        return ResetPasswordPage(self.driver)


