from pages.base_page import BasePage
from locators.signup_page_locators import SignupPageLocators
from service import site
from helpers import *



class SignupPage(BasePage):

    def __init__(self, *args):
        super().__init__(*args)
        self.open_url(site.signup)

    def input_first_name(self):
        self.find(SignupPageLocators.SIGNUP_FIRST_NAME_INPUT).send_keys(generate_random_string(6))

    def input_second_name(self):
        self.find(SignupPageLocators.SIGNUP_SECOND_NAME_INPUT).send_keys(generate_random_string(7))

    def input_user_name(self):
        self.find(SignupPageLocators.SIGNUP_USER_NAME_INPUT).send_keys(generate_random_string(8))

    def input_email(self):
        self.find(SignupPageLocators.SIGNUP_MAIL_INPUT).send_keys(generate_random_email(10))

    def input_password(self):
        self.find(SignupPageLocators.SIGNUP_PASSWORD_INPUT).send_keys(generate_random_string(9))

    def click_on_signup_down(self):
        self.alt_click(SignupPageLocators.SIGNUP_BUTTON_DOWN)
        