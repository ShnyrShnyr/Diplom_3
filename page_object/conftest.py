import pytest
from selenium import webdriver
from page_object.data import Data
from page_object.pages.main_page import MainPage
from page_object.pages.login_page import LoginPage


@pytest.fixture(params=['Chrome','Firefox'])
def driver(request):
    if request.param == 'Chrome':
        Data.BROWSER_NAME = 'Chrome'
        driver = webdriver.Chrome
    else:
        Data.BROWSER_NAME = 'Firefox'
        driver = webdriver.Firefox
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(Data.URL_MAIN_PAGE)
    return page

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.go_to_url(Data.URL_MAIN_PAGE+Data.URL_LOGIN_PAGE)
    return page

@pytest.fixture
def reset_password(driver):
    page = LoginPage(driver)
    page.go_to_url(Data.URL_MAIN_PAGE + Data.URL_LOGIN_PAGE)
    return page

@pytest.fixture
def lenta_orders(driver):
    page = LentaOrders(driver)
    page.go_to_url(Data.URL_MAIN_PAGE + Data.URL_LENTA_ORDERS)
    return page

