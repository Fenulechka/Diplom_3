import allure

from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Получить номер оформленного заказа")
    def get_new_order_number(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.wait_and_find_element(OrderFeedPageLocators.MODAL_ORDER_NUMBER).text != '9999')
        new_order_number_element = self.wait_and_find_element(OrderFeedPageLocators.MODAL_ORDER_NUMBER)
        new_order_number = new_order_number_element.text
        return int(new_order_number)

    @allure.step("Закрыть модальное окно")
    def close_modal_window(self):
        button = self.wait_and_find_element(OrderFeedPageLocators.MODAL_CLOSE_ORDER)
        self.click_element(button)

    @allure.step("Получить номер заказа в разделе В работе на экране Лента заказов")
    def get_order_id_in_progress_list(self):
        self.wait_and_find_element(OrderFeedPageLocators.ORDERS_AT_WORK)
        result = self.get_element_text(OrderFeedPageLocators.ORDERS_AT_WORK)
        return result

    @allure.step("Получить номера заказов из Ленты заказов")
    def find_orders_list(self):
        orders_section = self.get_element_text(OrderFeedPageLocators.ORDER_FEED_LIST)
        raw_order_numbers = [
            line.strip() for line in orders_section.splitlines() if line.startswith('#')
        ]
        normalized_orders = [number.lstrip('#').strip() for number in raw_order_numbers]
        return normalized_orders

    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_DROP_AREA)