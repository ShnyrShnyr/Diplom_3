import allure


class TestResetPasswordPage:
    @allure.title("Проверка клик на 'глаз' активирует поле")
    def test_click_to_eye_for_active_field(self, reset_password_page):
        field = reset_password_page.click_to_eye_for_active_field()
        assert field.is_displayed()
