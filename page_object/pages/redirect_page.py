import allure
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators


class RedirectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход в восстановление пароля")
    def redirect_to_password_recovery(self):
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)
        self.find_element_with_wait(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.click_on_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        button = self.find_element_with_wait(ResetPasswordPageLocators.RECOVERY_BUTTON)
        return button

    @allure.step("Переход в авторизацию")
    def redirect_to_sign_in(self):
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)
        button = self.find_element_with_wait(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        return button

    @allure.step("Переход в историю заказов")
    def redirect_to_history_orders(self):
        self.auth_user_without_create_order()
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)
        self.find_element_with_wait(LoginPageLocators.HISTORY_ORDERS_BUTTON)
        self.click_on_element(LoginPageLocators.HISTORY_ORDERS_BUTTON)
        element = self.find_element_with_wait(LoginPageLocators.ORDER)
        return element

    @allure.step("Переход в конструктор заказа")
    def redirect_from_constractor(self):
        self.click_on_element(LoginPageLocators.CONSTRACTOR_BUTTON)
        element = self.find_element_with_wait(MainPageLocators.COLLECT_BURGER_HEADER)
        return element

    @allure.step("Переход в ленту заказов")
    def redirect_to_lenta_orders(self):
        self.click_on_element(MainPageLocators.LENTA_ORDERS_BUTTON)
        element = self.find_element_with_wait(MainPageLocators.LENTA_ORDERS_HEADER)
        return element
