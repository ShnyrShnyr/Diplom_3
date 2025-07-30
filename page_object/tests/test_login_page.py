


class TestLoginPage:
    def test_enter_email_and_click_to_button(self,login_page):
        field = login_page.redirect_enter_email_click_to_button()
        assert field.is_displayed()

    def test_logout(self,login_page):
        element = login_page.logout()
        assert element.is_displayed()