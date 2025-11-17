from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import  expected_conditions as EC
from datetime import datetime
import allure
import os

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def open_url(self,url):
        self.driver.get(url)

    def get_page_title(self):
        return  self.driver.title

    def get_text_by_xpath(self, xpath):
        locator = (By.XPATH, xpath )
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text


    def take_screenshot(self, name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_dir = os.path.join(os.getcwd(),"reports", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        path = os.path.join(screenshot_dir, screenshot_name)
        self.driver.save_screenshot(path)

        #Attach screenshot to allure.
        allure.attach.file(path,name=name,attachment_type=allure.attachment_type.PNG)












