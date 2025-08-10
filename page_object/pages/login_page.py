import allure
from page_object.data import Data
from selenium.webdriver.common.by import By
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.locators.lenta_orders_page_locators import LentaOrdersPageLocators
from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators


@allure.description("Страница авторизации")
class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Выйти из профиля")
    def logout(self):
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, Data.EMAIL)
        self.add_text_to_element_with_enter(LoginPageLocators.PASSWORD_FIELD, Data.PASSWORD)
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)
        self.find_element_with_wait(LoginPageLocators.LOGOUT)
        self.click_on_element(LoginPageLocators.LOGOUT)
        element = self.find_element_with_wait(LoginPageLocators.HEADER_AFTER_LOGOUT)
        return element

    @allure.step("Заказы из истории заказов ищем в ленте заказов")
    def history_orders_in_lenta_orders(self):
        self.auth_user_without_create_order()
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)
        self.find_element_with_wait(LoginPageLocators.HISTORY_ORDERS_BUTTON)
        self.click_on_element(LoginPageLocators.HISTORY_ORDERS_BUTTON)
        items = self.find_elements_with_wait(LentaOrdersPageLocators.ORDERS_FROM_HISTORY_OR_LENTA)
        history_last_item = items[-1]
        history_second_last_item = items[-2]
        order_history_last = history_last_item.text
        locator_order_lenta_last = By.XPATH, f"//p[text()='{order_history_last}']"
        order_history_second_last = history_second_last_item.text
        locator_order_lenta_second_last =By.XPATH, f"//p[text()='{order_history_second_last}']"
        self.click_on_element(MainPageLocators.LENTA_ORDERS_BUTTON)
        element1 = self.find_element_with_wait(locator_order_lenta_last)
        element2 = self.find_element_with_wait(locator_order_lenta_second_last)
        return element1, element2

    @allure.step("Восстановление пароля по email")
    def enter_email_click_to_button(self):
        self.click_on_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.find_element_with_wait(ResetPasswordPageLocators.RECOVERY_BUTTON)
        self.add_text_to_element(ResetPasswordPageLocators.EMAIL_FIELD, Data.EMAIL)
        self.click_on_element(ResetPasswordPageLocators.RECOVERY_BUTTON)
        field = self.find_element_with_wait(ResetPasswordPageLocators.APPROVE_FIELD)
        return field



