import allure
from page_object.data import Data
from selenium.webdriver.common.by import By
from page_object.pages.base_page import BasePage
from page_object.locators.lenta_orders_page_locators import LentaOrdersPageLocators

@allure.description("Лента заказов")
class LentaOrdersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть модальное окно заказа')
    def open_modal_order(self):
        self.click_on_element(LentaOrdersPageLocators.ORDER)
        element = self.find_element_with_wait(LentaOrdersPageLocators.MODAL_ORDER)
        return element

    @allure.step('Создание заказа увеличивает счетчик')
    def create_order_increases_counter(self, locator):
        total_orders_before = self.get_text_from_element(locator)
        _, __ = self.auth_user_create_order()
        self.go_to_url(Data.URL_MAIN_PAGE + Data.URL_LENTA_ORDERS)
        self.find_element_with_wait(locator)
        total_orders_after = self.get_text_from_element(locator)
        return total_orders_before, total_orders_after

    @allure.step('Создание заказа и поиск его В работе')
    def create_order_and_find_in_work(self):
        _, order_number = self.auth_user_create_order()
        self.go_to_url(Data.URL_MAIN_PAGE + Data.URL_LENTA_ORDERS)
        try:
            self.waiting_to_close_modal(LentaOrdersPageLocators.WAITING_AT_WORK)
            locator_at_work = By.XPATH, f'//ul/li[text()="{order_number}" and text()="0"]'
            element = self.find_element_with_wait(locator_at_work)
            result = f'0{order_number}', element.text
        except Exception:
            result = 'Тест', f'не нашел заказ {order_number} в работе'
        return result
