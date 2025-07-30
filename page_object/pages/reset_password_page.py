from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators
from page_object.pages.base_page import BasePage
from page_object.data import Data

class ResetPasswordPage(BasePage):

    def click_to_eye_for_active_field(self):
        self.find_element_with_wait(ResetPasswordPageLocators.RECOVERY_BUTTON)
        self.add_text_to_element(ResetPasswordPageLocators.EMAIL_FIELD, Data.EMAIL)
        self.click_to_element(ResetPasswordPageLocators.RECOVERY_BUTTON)
        self.find_element_with_wait(ResetPasswordPageLocators.APPROVE_FIELD)
        self.click_to_element(ResetPasswordPageLocators.EYE)
        field = self.find_element_with_wait(ResetPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
        return field
