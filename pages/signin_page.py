from data import EMAIL, PASSWORD
from locators.signin_page_locators import SigninPageLocators
from pages.base_page import BasePage
from service import site



class SigninPage(BasePage):

    def __init__(self, *args):
        super().__init__(*args)
        self.open_url(site.signin)

    def input_email(self):
        self.find(SigninPageLocators.EMAIL_FIELD).send_keys(EMAIL)

    def input_password(self):
        self.find(SigninPageLocators.PASSWORD_FIELD).send_keys(PASSWORD)

    def check_visibility_signin_form(self):
        return bool(self.find(SigninPageLocators.SIGNIN_FORM))

    def check_user_is_authorized(self):
        return bool(self.find(SigninPageLocators.LOGIN_TITLE))
    
    def click_on_login_button_in_form(self):
        self.click(SigninPageLocators.LOGIN_BUTTON_IN_LOGIN_FORM)
