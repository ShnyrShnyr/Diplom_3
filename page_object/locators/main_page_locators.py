from selenium.webdriver.common.by import By

class MainPageLocators:

    SIGN_IN_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]'
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    COLLECT_BURGER_HEADER = By.XPATH,'//h1[@class="text text_type_main-large mb-5 mt-10"]'
    LENTA_ORDERS_BUTTON = By.XPATH, '//a[@href="/feed"]'
    LENTA_ORDERS_HEADER = By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"]'
    CLOSE_INGREDIENT_MODAL = By.XPATH,'//button[contains(@class, "Modal_modal__close")]'
    LOCATOR_TO = By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]'
    INGREDIENT_ICON = By.XPATH, '//img[@alt="Краторная булка N-200i"]'
    INGREDIENT_ICON_2 = By.XPATH, '//img[@alt="Соус фирменный Space Sauce"]'
    INGREDIENT_ICON_3 = By.XPATH, '//img[@alt="Говяжий метеорит (отбивная)"]'
    INGREDIENT_MODAL = By.XPATH,'//p[text()="Калории,ккал"]'
    INGREDIENT_COUNTER = By.XPATH, '//ul[2]/a[2]/div[1]/p'
    CONFIRM_ORDER = By.XPATH, '//h2[contains(@class,"3ikwq")]'
    HEADERS = By.XPATH, '//nav[contains(@class,"g5hnF")]'
    INGREDIENTS_AREA = By.XPATH,'//div[contains(@class,"Xu3Mo")]'
