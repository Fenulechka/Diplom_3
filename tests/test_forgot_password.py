import allure

from data import Date, TextDate
from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestForgotPassword:
    @allure.title("Тест проверки перехода на страницу восстановления пароля по кнопке Восстановить пароль")
    def test_go_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_login_page()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password_page()
        forgot_password_page = ForgotPasswordPage(driver)
        current_url = forgot_password_page.get_current_url()
        assert TextDate.TEXT_FORGOT_PASSWORD in current_url

    @allure.title("Тест проверки ввода почты и клик по кнопке Восстановить")
    def test_restore_password(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_login_page()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password_page()
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = forgot_password_page.restore_password(Date.test_email)
        reset_password_page.toggle_password_visibility()
        current_url = reset_password_page.get_current_url()
        assert TextDate.TEXT_RESET_PASSWORD in current_url

    @allure.title("Тест проверки подсветки поля пароля при клике на иконку глаза")
    def test_toggle_password_visibility(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_login_page()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password_page()
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = forgot_password_page.restore_password(Date.test_email)
        reset_password_page.toggle_password_visibility()
        reset_password_page.set_new_password(Date.new_password)
        assert reset_password_page.check_displaying_password_value()