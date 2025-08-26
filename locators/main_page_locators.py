from selenium.webdriver.common.by import By


class MainPageLocators:

    SIGNUP_BUTTON = By.CSS_SELECTOR, 'a[href="/signup"]'
    LOGIN_BUTTON = By.CSS_SELECTOR, "a[href='/signin']"
    EXIT_BUTTON = By.XPATH, "//a[starts-with(@class,'styles_menuLink__') and normalize-space(.)='Выход']"
