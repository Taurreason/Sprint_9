from selenium.webdriver.common.by import By

class SignupPageLocators:

    SIGNUP_FIRST_NAME_INPUT = By.CSS_SELECTOR, 'input[name="first_name"]'
    SIGNUP_SECOND_NAME_INPUT = By.CSS_SELECTOR, 'input[name="last_name"]'
    SIGNUP_USER_NAME_INPUT = By.XPATH, "//input[@name='username']"
    SIGNUP_MAIL_INPUT = By.XPATH, "//input[@name='email']"
    SIGNUP_PASSWORD_INPUT = By.XPATH, "//input[@name='password']"

    SIGNUP_BUTTON_DOWN = By.XPATH, "//button[normalize-space()='Создать аккаунт']"
