import allure
from selenium.webdriver.common.by import By

from page_object.data import Data
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators
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
        self.go_to_url(Data.URL_MAIN_PAGE + Data. URL_LENTA_ORDERS)
        total_orders_after = self.get_text_from_element(locator)
        return total_orders_before, total_orders_after

    @allure.step('Создание заказа и поиск его "В работе"')
    def create_order_and_find_in_work(self):
        _,order_number = self.auth_user_create_order()
        self.click_on_element(LentaOrdersPageLocators.CLOSE_MODAL_ORDER)
        order_locator_at_work = By.XPATH, f'//li[text()="{order_number}" and text()="0"]'
        self.go_to_url(Data.URL_MAIN_PAGE + Data. URL_LENTA_ORDERS)
        self.waiting_to_close_modal(LentaOrdersPageLocators.WAITING_AT_WORK)
        element = self.find_elements_with_wait(order_locator_at_work)
        return True
