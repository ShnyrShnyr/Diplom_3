import allure
from page_object.data import Data
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators

@allure.description("Главная страница")
class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликнуть на ингредиент")
    def click_to_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_ICON)
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL)
        return element

    @allure.step("Кликнуть на крестик модального окна")
    def click_to_close_modal(self):
        self.click_on_element(MainPageLocators.INGREDIENT_ICON)
        self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL)
        self.click_on_element(MainPageLocators.CLOSE_INGREDIENT_MODAL)
        try:
            self.waiting_to_close_modal(MainPageLocators.INGREDIENT_MODAL)
            result = True
        except Exception:
            result = False
        return result

    @allure.step("При добавлении ингредиента счетчик ингредиента меняется")
    def change_the_counter_of_ingredient(self):
        counter_before = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER).text
        if Data.BROWSER_NAME == 'Chrome':
            self.my_drag_and_drop(MainPageLocators.INGREDIENT_ICON_2, MainPageLocators.LOCATOR_TO)
        else:
            self.switch_to_window()
            self.drag_and_drop_element(MainPageLocators.INGREDIENT_ICON_2, MainPageLocators.LOCATOR_TO)
        counter_after = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER).text
        return counter_before, counter_after
