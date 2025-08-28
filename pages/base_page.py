from functools import wraps
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    @staticmethod
    def wait_for_element_visibility(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(EC.visibility_of_element_located(locator))
            return func(self, locator)

        return wrapper

    @staticmethod
    def wait_for_element_presence(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(EC.presence_of_element_located(locator))
            return func(self, locator)

        return wrapper
    
    @staticmethod
    def wait_for_elements_presence(func):
        @wraps(func)
        def wrapper(self, locator, *args, **kwargs):
            self.wait.until(EC.presence_of_all_elements_located(locator))
            return func(self, locator, *args, **kwargs)
        return wrapper

    @staticmethod
    def wait_for_element_clickability(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(EC.element_to_be_clickable(locator))
            return func(self, locator)

        return wrapper

    @staticmethod
    def wait_for_element_invisibility(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(EC.invisibility_of_element_located(locator))
            return func(self, locator)

        return wrapper

    @wait_for_elements_presence
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_open_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    def open_url(self, url) -> bool:
        self.driver.get(url)
        return self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    @wait_for_element_visibility
    def find(self, locator):
        return self.driver.find_element(*locator)

    @wait_for_element_clickability
    def click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @wait_for_element_clickability
    def alt_click(self, locator):
        self.find(locator).click()

    def find_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
        
    def upload_file(self, locator, filename):
        path = (Assets.DIR / filename).resolve()
        assert path.exists(), f"Файл не найден: {path}"

        el = self.find_present(locator).send_keys(str(path))

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    def choose_from_suggest(self, list_locator, option_locator):
        self.find(list_locator)      # дождались появления списка
        self.click(option_locator)   # клик

    def get_current_url(self):
        return self.driver.current_url

    def url_contains(self, part):
        return part in self.get_current_url()