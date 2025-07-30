from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//a[@href="/forgot-password"]'
    EMAIL_FIELD = By.XPATH, '//label[text()="Email"]/following-sibling::*'
    PASSWORD_FIELD = By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]'
    HISTORY_ORDERS_BUTTON = By.XPATH, '//a[@href="/account/order-history"]'
    ORDER = By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]' #все заказы с таким xpath
    LOGOUT = By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]'
    HEADER_AFTER_LOGOUT = By.XPATH, "//h2[text()='Вход']"
    CONSTRACTOR_BUTTON = By.XPATH, '//a[@class="AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo"]'

