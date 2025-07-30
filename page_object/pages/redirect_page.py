from page_object.data import Data
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators
from page_object.pages.base_page import BasePage

class RedirectPage(BasePage):
    def redirect_to_password_recovery(self):
        self.click_to_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        button = self.find_element_with_wait(ResetPasswordPageLocators.RECOVERY_BUTTON)
        return button

    def redirect_to_sign_in(self):
        self.click_to_element(MainPageLocators.SIGN_IN_BUTTON)
        button = self.find_element_with_wait(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        return button

    def redirect_to_history_orders(self):
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, Data.EMAIL)
        self.add_text_to_element_with_enter(LoginPageLocators.PASSWORD_FIELD, Data.PASSWORD)
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.SIGN_IN_BUTTON)
        self.find_element_with_wait(LoginPageLocators.HISTORY_ORDERS_BUTTON).click()
        element = self.find_element_with_wait(LoginPageLocators.ORDER)
        return element

    def redirect_from_constractor(self):
        self.click_to_element(LoginPageLocators.CONSTRACTOR_BUTTON)
        element = self.find_element_with_wait(MainPageLocators.COLLECT_BURGER_HEADER)
        return element

    def redirect_to_lenta_orders(self):
        self.click_to_element(MainPageLocators.LENTA_ORDERS_BUTTON)
        element = self.find_element_with_wait(MainPageLocators.LENTA_ORDERS_HEADER)
        return element
