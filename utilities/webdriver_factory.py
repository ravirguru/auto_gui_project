from selenium import webdriver
import  os
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebDriverFactory:
    @staticmethod
    def create_driver(browser):
        # Detect CI or Jenkins
        run_env = os.getenv("RUN_ENV", "").lower()
        is_ci = os.getenv("CI", "").lower() == "true"
        use_remote = run_env == "jenkins" or is_ci
        if use_remote:
            return WebDriverFactory._create_remote_driver(browser)
        else:
            return WebDriverFactory._create_local_driver(browser)


    @staticmethod
    def _create_local_driver(browser):
        if browser == "chrome":
            options = ChromeOptions()
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        else:
            raise  ValueError(f"Unsupported browser type")
        driver.maximize_window()
        return driver

    @staticmethod
    def _create_remote_driver(browser):
        # Read from environment first, fallback to Chrome port
        remote_url = os.getenv("GRID_URL", "http://localhost:4444/wd/hub")
        if browser == "chrome":
            options = ChromeOptions()
            return webdriver.Remote(command_executor=remote_url,options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            return webdriver.Remote(command_executor=remote_url,options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")







