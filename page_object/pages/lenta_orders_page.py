from page_object.data import Data
from page_object.pages.base_page import BasePage
from page_object.locators.lenta_orders_page_locators import LentaOrdersPageLocators
from page_object.pages.main_page import MainPage


class LentaOrdersPage(BasePage, MainPage):
    def open_modal_order(self):
        self.click_to_element(LentaOrdersPageLocators.ORDER)
        element = self.find_element_with_wait(LentaOrdersPageLocators.MODAL_ORDER)
        return element

    def history_orders_in_lenta_orders(self):
        self.go_to_url(Data.URL_MAIN_PAGE + Data.URL_HISTORY_ORDERS)
        items = self.find_elements_with_wait(LentaOrdersPageLocators.ORDERS_FROM_HISTORY)
        last_item = items[-1]
        self.scroll_to_element(last_item)
        order_number = last_item.get_text_from_element(LentaOrdersPageLocators.FIELD_NUMBER_GET)
        self.go_to_url(Data.URL_MAIN_PAGE + Data.URL_LENTA_ORDERS)
        locator = LentaOrdersPageLocators.FIELD_NUMBER_FIND
        order_lenta = self.get_text_from_element(locator)
        return order_number == order_lenta

    def create_order_increases_counter(self, locator):
        total_orders_before = self.get_text_from_element(locator)
        _ = self.auth_user_create_order()
        self.go_to_url(Data.URL_MAIN_PAGE + Data. URL_LENTA_ORDERS)
        total_orders = self.get_text_from_element(locator)
        return total_orders > total_orders_before

    def create_order_and_find_in_work(self):
        element = self.auth_user_create_order()
        order_number = self.get_text_from_element(element)
        orders = self.find_elements_with_wait(LentaOrdersPageLocators.ORDER_AT_WORK).text
        return order_number, orders


