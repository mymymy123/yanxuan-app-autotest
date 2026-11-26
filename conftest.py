from config import *
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest
import time
from pages.enter_home_page import EnterHomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.cart_page import CartPage

@pytest.fixture()
def first_app_driver():
    des_caps = {**DEVICE_CONFIG, **FIRST_APP_CONFIG}
    # 初始化设备配置信息
    option = UiAutomator2Options().load_capabilities(des_caps)
    # 创建驱动对象
    driver = webdriver.Remote(APPIUM_SERVER, options=option)
    yield driver
    time.sleep(3)
    driver.terminate_app(APP_CONFIG['appPackage'])
    driver.quit()

@pytest.fixture()
def app_driver():
    des_caps = {**DEVICE_CONFIG, **APP_CONFIG}
    # 初始化设备配置信息
    option = UiAutomator2Options().load_capabilities(des_caps)
    # 创建驱动对象
    driver = webdriver.Remote(APPIUM_SERVER, options=option)
    yield driver
    time.sleep(3)
    driver.terminate_app(APP_CONFIG['appPackage'])
    driver.quit()

@pytest.fixture()
def enter_home_fix(first_app_driver):
    enter=EnterHomePage(first_app_driver)
    return enter

@pytest.fixture()
def login_fix(first_app_driver,enter_home_fix):
    login=LoginPage(first_app_driver)
    enter_home_fix.enter_home()
    login.enter_login()
    return login

@pytest.fixture()
def search_fix(first_app_driver,login_fix):
    search=SearchPage(first_app_driver)
    login_fix.login(EMAIL,PASSWORD)
    return search

@pytest.fixture()
def cart_fix(first_app_driver,search_fix):
    cart=CartPage(first_app_driver)
    search_fix.search('毛巾')
    cart.enter_goods_detail()
    yield cart
    cart.back_home()

