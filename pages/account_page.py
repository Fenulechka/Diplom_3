import allure

from locators.account_page_locators import AccountPageLocators, HistoryPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("Кликнуть по кнопке История заказов")
    def click_on_order_history_button(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY)

    @allure.step("Кликнуть по кнопке Выйти")
    def click_on_logout_button(self):
        self.click_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Подождать прогрузки текста описания раздела")
    def wait_visibility_of_account_text(self):
        self.wait_for_element(AccountPageLocators.ACCOUNT_TEXT)