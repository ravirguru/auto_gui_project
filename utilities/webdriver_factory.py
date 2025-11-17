from selenium import webdriver
import  os
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebDriverFactory:
    @staticmethod
    def create_driver(browser):
        is_ci = os.getenv("CI") == "true"
        if browser == "chrome":
            options = ChromeOptions()
            if is_ci:   # In GitHub Actions → must run headless
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            if is_ci:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        else:
            raise  ValueError(f"Unsupported browser type")
        driver.maximize_window()
        return driver




