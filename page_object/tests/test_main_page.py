from selenium.webdriver.support.expected_conditions import element_to_be_selected


class TestMainPage:
    def test_click_to_ingredient(self, main_page):
        element = main_page.click_to_ingredient()
        assert element.is_displayed

    def test_close_modal(self, main_page):
        element = main_page.click_to_close_modal()
        assert element.is_not_displayed

    def test_change_the_counter_of_ingredient(self, main_page):
        element = main_page.change_the_counter_of_ingredient()
        assert element.is_displayed
        
    def test_auth_user_create_order(self, main_page):
        element = main_page.auth_user_create_order()
        assert element.is_displayed
