from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from service import *

class MainPage(BasePage):

    def __init__(self, *args):
        super().__init__(*args)
        self.open_url(site.main)

    def click_on_signup(self):
        self.click(MainPageLocators.SIGNUP_BUTTON)

    def click_on_login(self):
        self.click(MainPageLocators.LOGIN_BUTTON)
    
    def wait_recipes_page_is_open(self):
        self.wait_open_url(site.recipes)
        return site.recipes in self.driver.current_url

    def check_exit_button(self):
        return bool(self.find(MainPageLocators.EXIT_BUTTON))
