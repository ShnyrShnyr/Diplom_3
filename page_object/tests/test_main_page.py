import allure


class TestMainPage:
    @allure.title("Клик на ингредиент раскрывает модальное окно с ингредиентом")
    def test_click_to_ingredient(self, main_page):
        element = main_page.click_to_ingredient()
        assert element.is_displayed

    @allure.title("Проверка закрытия модального окна")
    def test_close_modal(self, main_page):
        status_modal_closed = main_page.click_to_close_modal()
        assert status_modal_closed

    @allure.title("Проверка изменения счетчика ингредиента в заказе")
    def test_change_the_counter_of_ingredient(self, main_page):
        counter_before, counter_after = main_page.change_the_counter_of_ingredient()
        assert counter_after > counter_before

    @allure.title("Проверка авторизации и создание заказа")
    def test_auth_user_create_order(self, main_page):
        element, _ = main_page.auth_user_create_order()
        assert element.is_displayed
