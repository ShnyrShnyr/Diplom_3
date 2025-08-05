from selenium.webdriver.common.by import By

class LentaOrdersPageLocators:
    ORDER = By.XPATH, '(//p[@class="text text_type_digits-default"])[1]'
    MODAL_ORDER = By.XPATH, '//p[@class="text text_type_main-medium mb-8"]'
    CLOSE_MODAL_ORDER = By.XPATH, '//button[contains(@class,"3V5XS")]'
    ORDERS_FROM_HISTORY_OR_LENTA = By.XPATH, '//p[@class ="text text_type_digits-default"]'
    TOTAL_ORDER_COUNT = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    TODAY_ORDER_COUNT = By.XPATH, '//p[normalize-space(.)="Выполнено за сегодня:"]/following-sibling::p'
    ORDER_9999 = By.XPATH, '//h2[text()="9999"]'
    ORDER_AT_WORK = By.XPATH, '//ul/li[@class="text text_type_digits-default mb-2"]'
    WAITING_AT_WORK = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'
    AREA_AT_WORK = By.XPATH, '//ul[contains(@class,"1YFem")]'
