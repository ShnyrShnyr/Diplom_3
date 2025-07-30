

class TestResetPasswordPage:
    def test_click_to_eye_for_active_field(self, reset_password):
        field = reset_password.click_to_eye_for_active_field()
        assert field.is_displayed()
