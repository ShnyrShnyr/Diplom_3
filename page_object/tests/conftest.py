import pytest
from selenium import webdriver
from page_object.data import Data
from page_object.pages.main_page import MainPage
from page_object.pages.login_page import LoginPage
from page_object.pages.lenta_orders_page import LentaOrdersPage
from page_object.pages.redirect_page import RedirectPage
from page_object.pages.reset_password_page import ResetPasswordPage


@pytest.fixture(params=['Chrome','Firefox'])
def driver(request):
    if request.param == 'Chrome':
        Data.BROWSER_NAME = 'Chrome'
        drv = webdriver.Chrome()
        drv.implicitly_wait(5)
    else:
        Data.BROWSER_NAME = 'Firefox'
        drv = webdriver.Firefox()
        drv.implicitly_wait(5)
    yield drv
    drv.quit()

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
def reset_password_page(driver):
    page = ResetPasswordPage(driver)
    page.go_to_url(Data.URL_MAIN_PAGE+Data.URL_LOGIN_PAGE)
    return page

@pytest.fixture
def lenta_orders_page(driver):
    page = LentaOrdersPage(driver)
    page.go_to_url(Data.URL_MAIN_PAGE+Data.URL_LENTA_ORDERS)
    return page

@pytest.fixture
def redirect_page(driver):
    page = RedirectPage(driver)
    page.go_to_url(Data.URL_MAIN_PAGE)
    return page
