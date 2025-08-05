import allure
import pytest
from page_object.locators.lenta_orders_page_locators import LentaOrdersPageLocators

@allure.description("Проверка Ленты заказов")
class TestLentaOrdersPage:

    @allure.title("Проверка открытия модального окна заказа")
    def test_open_modal_order(self, lenta_orders_page):
        element = lenta_orders_page.open_modal_order()
        assert element.is_displayed()

    @pytest.mark.parametrize(
        "locator",
        (
        LentaOrdersPageLocators.TOTAL_ORDER_COUNT,
        LentaOrdersPageLocators.TODAY_ORDER_COUNT
        )
    )
    @allure.title("Проверка, что созданный заказ увеличивает общий счетчик заказов и заказы сегодня")
    def test_create_order_increases_counter(self, lenta_orders_page, locator):
        total_orders_before, total_orders_after = lenta_orders_page.create_order_increases_counter(locator)
        assert total_orders_after > total_orders_before

    @allure.title("Проверка, что созданный заказ появляется 'В работе'")
    def test_create_order_and_find_in_work(self, lenta_orders_page):
        element_is_in_work = lenta_orders_page.create_order_and_find_in_work()
        assert element_is_in_work == True


