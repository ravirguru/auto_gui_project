from time import  sleep

import pytest

#from test_auto_gui_project.pages.login_page import LoginPage
from pages.login_page import LoginPage
from utilities.logger import get_logger

logger = get_logger(__name__)

def test_login_page(setup_teardown):
    logger.info(f"Starting test: test valid login user")
    driver = setup_teardown
    login_page = LoginPage(driver)
   # login_page = LoginPage()
    login_page.open_url(login_page.URL)
    logger.info("Navigated to Login page")
    username ="standard_user"

    try:
        login_page.enter_username(username)
        logger.info("Entering username in text field")
        sleep(2)
    except Exception as e:
        print(e.__repr__())
    login_page.enter_password("secret_sauce")
    logger.info("Entered password in text field")
    login_page.click_login_btn()
    logger.info("Clicked login button successfully")
    logger.info("Login test completed successfully")
    expected_title = "Swag Labs"
    actual_title = login_page.get_page_title()
    assert actual_title == expected_title, f"Expected title to be {expected_title} but got {actual_title
    }"

@pytest.mark.regression
def test_invalid_user(setup_teardown):
        logger.info(f"starting test for invalid user login")
        login_page = LoginPage(setup_teardown)
        login_page.open_url(login_page.URL)
        login_page.enter_username("abc123")
        login_page.enter_password("abc123")
        try:
            login_page.click_login_btn()
        except Exception as e:
            print(e)
        error_msg = login_page.get_error_msg()
        assert "Username and password do not match any user in this service".lower() in error_msg.lower(), "Expected error message not displayed"

@pytest.mark.smoke
def test_empty_user(setup_teardown):
    logger.info("Starting test for empty user name and password")
    driver = setup_teardown

    loginpage = LoginPage(driver)
    loginpage.open_url(loginpage.URL)
    loginpage.enter_username("   ")
    loginpage.enter_password("   ")
    try:
        loginpage.click_login_btn()
    except Exception as e:
        print(e.__repr__())
        errormessage = loginpage.get_text_by_xpath(loginpage.EMPTY_USERNAME_PWD)
        assert "Epic sadface: Username is required".lower() in errormessage.lower(), "Expected error message not displayed"

