

class TestRedirectPage:

    def test_redirect_to_recovery_password(self, login_page):
        element = login_page.redirect_to_password_recovery()
        assert element.is_displayed()

    def test_redirect_to_sign_in(self, main_page):
        element = main_page.redirect_to_password_recovery()
        assert element.is_displayed()

    def test_redirect_to_history_orders(self,login_page):
        element = login_page.redirect_to_history_orders()
        assert element.is_displayed()

    def test_redirect_from_constractor(self,login_page):
        element = login_page.redirect_from_constractor()
        assert element.is_displayed()

    def test_redirect_to_lenta_orders(self, login_page):
        element = login_page.redirect_to_lenta_orders()
        assert element.is_displayed()