from selenium.webdriver.common.by import By


class SigninPageLocators:

    EMAIL_FIELD = By.CSS_SELECTOR, "input[name='email']"
    PASSWORD_FIELD = By.CSS_SELECTOR, "input[name='password']"

    LOGIN_TITLE = By.XPATH, "//h1[normalize-space(.)='Войти на сайт']"

    SIGNIN_FORM = By.XPATH, "//form[.//input[@name='email'] and .//input[@name='password']]"
    LOGIN_BUTTON_IN_LOGIN_FORM = By.XPATH, "//form[.//input[@name='email'] and .//input[@name='password']]//button[normalize-space(.)='Войти']"
