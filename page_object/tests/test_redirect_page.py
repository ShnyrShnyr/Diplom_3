import allure


class TestRedirectPage:
    @allure.title("Проверка перенаправления на страницу изменения пароля")
    def test_redirect_to_recovery_password(self, redirect_page):
        element = redirect_page.redirect_to_password_recovery()
        assert element.is_displayed()

    @allure.title("Проверка перенаправления на страницу авторизации")
    def test_redirect_to_sign_in(self, redirect_page):
        element = redirect_page.redirect_to_sign_in()
        assert element.is_displayed()

    @allure.title("Проверка перенаправления на страницу истории заказов")
    def test_redirect_to_history_orders(self, redirect_page):
        element = redirect_page.redirect_to_history_orders()
        assert element.is_displayed()

    @allure.title("Проверка перенаправления на конструктора заказов")
    def test_redirect_from_constractor(self,redirect_page):
        element = redirect_page.redirect_from_constractor()
        assert element.is_displayed()

    @allure.title("Проверка перенаправления на страницу лента заказов")
    def test_redirect_to_lenta_orders(self, redirect_page):
        element = redirect_page.redirect_to_lenta_orders()
        assert element.is_displayed()