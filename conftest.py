import allure
import pytest
import os
import time

from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector

from pages.main_page import MainPage
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from pages.recipe_page import RecipePage
from helpers import *
from service import *


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # полезные флаги для контейнеров
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # версия браузера и selenoid-опции
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": False,
            "name": "pytest-session",
            "shmSize": 536870912,  # 512MB
            "screenResolution": "1366x900x24"

        },
    )

    command_executor = os.getenv("SELENOID_URL", "http://localhost:4444/wd/hub")
    drv = webdriver.Remote(command_executor=command_executor, options=options)
    drv.file_detector = LocalFileDetector()
    drv.set_window_size(1366, 900)
    yield drv
    drv.quit()
    
@pytest.fixture
def main_page(driver):
    with allure.step('Открываем главную страницу'):
        return MainPage(driver)
    

@pytest.fixture
def signin_page(driver):
    with allure.step('Открываем страницу входа пользователя'):
        return SigninPage(driver)
    
@pytest.fixture
def signup_page(driver):
    with allure.step('Открываем страницу регистрации пользователя'):
        return SignupPage(driver)
    
@pytest.fixture
def recipe_page(driver, login_user):
    with allure.step('Открываем страницу рецептов'):
        return RecipePage(driver)
    
@pytest.fixture
def login_user(driver):
    with allure.step('Открываем страницу входа пользователя'):
        signin_page = SigninPage(driver)
    with allure.step('Вводим почту'):
        signin_page.input_email()
    with allure.step('Вводим пароль'):
        signin_page.input_password()
        time.sleep(1)
    with allure.step('Нажимаем на кнопку Войти в форме авторизации'):
        signin_page.click_on_login_button_in_form()
