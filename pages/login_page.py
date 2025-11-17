from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utilities.logger import get_logger

logger = get_logger(__name__)


def wait_for_element(locator):
    """
    Decorator that waits for an element to be visible before running the method.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


# class LoginPage(setup_teardown):
class LoginPage(BasePage):
    # driver = WebDriver()
    # ------------Locators and xpath.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    URL = "https://www.saucedemo.com/"
    # USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    USERNAME_INPUT = (By.ID, 'user-name')

    USERS_PWD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//input[@class='submit-button btn_action']")
    #ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error' and contains(text(),'Epic sadface')])")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error' and contains(text(),'Epic sadface')]")
    EMPTY_USERNAME_PWD = (By.XPATH, "//h3[@data-test='error' and contains(text(),'Epic sadface: Username is required')]")

    @wait_for_element(USERNAME_INPUT)
    def enter_username(self, username):
        try:
            self.driver.find_element(*self.USERNAME_INPUT).clear()
            self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
            #self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
            print("username is entered now")
        except Exception as e:
            print(e.__repr__())

    @wait_for_element(USERS_PWD)
    def enter_password(self, password):
        self.driver.find_element(*self.USERS_PWD).send_keys(password)

    @wait_for_element(LOGIN_BTN)
    def click_login_btn(self):

        if self.driver.find_element(*self.LOGIN_BTN).click():
            logger.info("Clicked on login button successfully")
            return True
        else:
            return False


    # @wait_for_element
    def get_error_msg(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
