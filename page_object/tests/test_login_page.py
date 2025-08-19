import allure


class TestLoginPage:
    @allure.title("Проверка восстановления пароля")
    def test_enter_email_and_click_to_button(self,login_page):
        field = login_page.enter_email_click_to_button()
        assert field.is_displayed()

    @allure.title("Проверка выхода из профиля")
    def test_logout(self,login_page):
        element = login_page.logout()
        assert element.is_displayed()

    @allure.title("Проверка заказов из истории в ленте заказов")
    def test_history_orders_in_lenta_orders(self,login_page):
        element1, element2 = login_page.history_orders_in_lenta_orders()
        assert element1.is_displayed() and element2.is_displayed()