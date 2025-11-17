import pytest
from pytest import  fixture
from selenium import  webdriver
import  allure
from pages.base_page import BasePage
from utilities.webdriver_factory import WebDriverFactory

#@fixture(params=["chrome","firefox"])
@fixture()   #Removing pytest_addoption() and use: Then just pytest -vs runs twice — once per browser automatically.
def setup_teardown(request):
    #browser  = request.param.lower().strip()
    browser = request.config.getoption("--browser").lower().strip()
   # print(f"browser value is {browser}")
   # browser.lower().strip()
   #  if browser == "chrome":
   #     driver = webdriver.Chrome()
   #  elif browser == "firefox":
   #      driver = webdriver.Firefox()
   #  else:
   #      raise ValueError(f"Unsupported browser {browser}")
   #  driver.maximize_window()
    driver = WebDriverFactory.create_driver(browser)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
     outcome = yield
     report = outcome.get_result()

     if report.when == "call" and report.failed:
         print(f"🔥 Screenshot hook triggered for: {item.name}")
         driver = item.funcargs.get("setup_teardown")
         if driver:
             try:
                 page = BasePage(driver)
                 page.take_screenshot(name=item.name)
             except Exception as e:
                 print(f"Screenshot capture failed {e}")



@pytest.fixture()
def sample_data():
    print("\n Setting up fixture for sample data")
    data = {"name" : "Alice", "age" : 30}
    yield  data
    print("tearing down the fixture")

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
         action = "store",
         default = "chrome",
         help ="Type of browser: chrome or firefox"
    )