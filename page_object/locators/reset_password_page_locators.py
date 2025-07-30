from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    RECOVERY_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    EMAIL_FIELD = By.XPATH, "//input[@class='text input__textfield text_type_main-default']"
    APPROVE_FIELD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']"
    EYE = By.CSS_SELECTOR, "div.input__icon.input__icon-action > svg"
    PASSWORD_FIELD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']"
    PASSWORD_FIELD_ACTIVE = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']"

