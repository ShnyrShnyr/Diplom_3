from selenium.webdriver.common.by import By

class LentaOrdersLocators:
    ORDER = By.XPATH, '//a[@href="/feed/6887ea429ed280001b665ace"]'
    MODAL_ORDER = By.XPATH, '//p[@class="text text_type_main-medium mb-8"]'
    ORDERS_FROM_HISTORY = By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]'
    FIELD_NUMBER_GET = By.XPATH, '//p[@class ="text text_type_digits-default"]'
    FIELD_NUMBER_FIND = By.XPATH, f'//p[text()={order_number}]'
    TOTAL_ORDER_COUNT = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    TODAY_ORDER_COUNT = By.XPATH, '//p[normalize-space(.)="Выполнено за сегодня:"]/following-sibling::p'
    ORDER_9999 = By.XPATH, '//h2[text()="9999"]'
    ORDER_AT_WORK = By.XPATH, '//li[@class="text text_type_digits-default mb-2"]'

    < li

    class ="text text_type_digits-default mb-2" > 0272320 < / li >
    < h2

    class ="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8" > 9999 < / h2 >

