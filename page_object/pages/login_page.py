from page_object.locators.login_page_locators import LoginPageLocators, ResetPasswordPageLocators
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage
from page_object.data import Data

class LoginPage(BasePage):
    def redirect_enter_email_click_to_button(self):
        self.click_to_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.find_element_with_wait(ResetPasswordPageLocators.RECOVERY_BUTTON)
        self.add_text_to_element(ResetPasswordPageLocators.EMAIL_FIELD,Data.EMAIL)
        self.click_to_element(ResetPasswordPageLocators.RECOVERY_BUTTON)
        field = self.find_element_with_wait(ResetPasswordPageLocators.APPROVE_FIELD)
        return field

    def logout(self):
        self.click_to_element(MainPageLocators.SIGN_IN_BUTTON)
        if self.find_element_with_wait(LoginPageLocators.LOGOUT).is_displayed():
            self.click_to_element(LoginPageLocators.LOGOUT)
            element = self.find_element_with_wait(LoginPageLocators.HEADER_AFTER_LOGOUT)
        else:
            self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, Data.EMAIL)
            self.add_text_to_element_with_enter(LoginPageLocators.PASSWORD_FIELD, Data.PASSWORD)
            self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)
            self.click_to_element(MainPageLocators.SIGN_IN_BUTTON)
            self.find_element_with_wait(LoginPageLocators.LOGOUT).click()
            element = self.find_element_with_wait(LoginPageLocators.HEADER_AFTER_LOGOUT)
        return element



