from page_object.conftest import lenta_orders


class TestLentaOrdersPage:

    def test_open_modal_order(self, lenta_orders):
        element = lenta_orders.open_modal_order()
        assert element.is_displayed

    def test_history_orders_in_lenta_orders(self,lenta_orders):
        assert lenta_orders.history_orders_in_lenta_orders()

    @pytest.mark.parametrize(
        locator,
        [LentaOrdersPageLocators.TOTAL_ORDER_COUNT,
         LentaOrdersPageLocators.TODAY_ORDER_COUNT]
    )

    def test_create_order_increases_counter(self, lenta_orders, locator):
        assert lenta_orders.create_order_increases_counter(locator)

    def test_create_order_and_find_in_work(self, lenta_orders):
        order_number, order = lenta_orders.create_order_and_find_in_work()
        assert order_number in order


