from selenium.webdriver.common.by import By

class MainPageLocators:

    SIGN_IN_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]'
    CREATE_ORDER_BUTTON = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    COLLECT_BURGER_HEADER = By.XPATH,'//h1[@class="text text_type_main-large mb-5 mt-10"]'
    LENTA_ORDERS_BUTTON = By.XPATH, '//a[@href="/feed"]'
    LENTA_ORDERS_HEADER = By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"]'
    INGREDIENT_ICON = By.XPATH,'//img[@alt="Краторная булка N-200i"]'
    INGREDIENT_MODAL = By.XPATH,'//p[@class="text text_type_main-medium mb-8"]'
    CLOSE_INGREDIENT_MODAL = By.XPATH,'//button[contains(@class, "Modal_modal__close")]'
    INGREDIENT_ICON_2 = By.XPATH, '//img[@alt="Соус фирменный Space Sauce"]'
    INGREDIENT_COUNTER = By.XPATH, '//p[@class="counter_counter__num__3nue1" and text()=1]'
    LOCATOR_TO = By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]'
    INGREDIENT_ICON_3 = By.XPATH, '//img[@alt="Говяжий метеорит (отбивная)"]'
    CONFIRM_ORDER = By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]'



     '''QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//div[@aria-labelledby="accordion__heading-{}"]'
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH,'//div[@id="accordion__heading-7"]'
    ORDER_BUTTON_UP = By.XPATH, '//button[@class="Button_Button__ra12g"]'
    ORDER_BUTTON_DOWN = By.CLASS_NAME, 'Button_Middle__1CSJM'
    CHECK_MAIN_PAGE = By.CLASS_NAME, 'Home_FirstPart__3g6vG'
    
INPUT_USER_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::*"
TOTAL_ORDER_COUNT = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
для глазика
//section[contains(@class,"Modal_modal_opened")]//button[@type="button"]'''