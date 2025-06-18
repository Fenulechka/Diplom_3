import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        normalized_orders = [
            line.strip().lstrip('#').strip()
            for line in orders_section.splitlines()
            if line.startswith('#')
        ]
        return normalized_orders

    @allure.step("Кликнуть на Конструктор")
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_DROP_AREA)

    @allure.step("Ждем пока исчезнет текст Все текущие заказы готовы!")
    def wait_for_status_text_to_disappear(self, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            EC.text_to_be_present_in_element(
                OrderFeedPageLocators.STATUS_READY_TEXT,
                "Все текущие заказы готовы!")
            )
