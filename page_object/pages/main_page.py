from data import BROWSER_NAME
import allure

from page_object.data import Data
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_ICON)
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL)
        return element

    def click_to_close_modal(self):
        self.click_to_element(MainPageLocators.INGREDIENT_ICON)
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL)
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_MODAL)
        return element

    def change_the_counter_of_ingredient(self):
        self.my_drag_and_drop(MainPageLocators.INGREDIENT_ICON_2, MainPageLocators.LOCATOR_TO)
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
        return element

    def auth_user_create_order(self):
        self.click_to_element(MainPageLocators.SIGN_IN_BUTTON)
        self.find_element_with_wait(LoginPageLocators.EMAIL_FIELD)
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, Data.EMAIL)
        self.add_text_to_element_with_enter(LoginPageLocators.PASSWORD_FIELD, Data.PASSWORD)
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)
        self.my_drag_and_drop(MainPageLocators.INGREDIENT_ICON,MainPageLocators.LOCATOR_TO)
        self.my_drag_and_drop(MainPageLocators.INGREDIENT_ICON_2,MainPageLocators.LOCATOR_TO)
        self.my_drag_and_drop(MainPageLocators.INGREDIENT_ICON_3, MainPageLocators.LOCATOR_TO)
        self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)
        element = self.find_element_with_wait(MainPageLocators.CONFIRM_ORDER)
        return element

    '''@allure.step('Клик на вопрос')
    def
if BROWSER_NAME == 'Chrome':
    self.wait.until_not(expected_conditions.visibility_of_element_located())'''