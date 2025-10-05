from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support import expected_conditions as e

class Base:
    def __init__(self,driver):
        self.driver=driver
        self.action=ActionChains(self.driver)

    def search_element(self,locator):
        web_element=self.driver.find_element(*locator)
        return web_element
    def search_elements(self,locator):
        web_elements=self.driver.find_elements(*locator)
        return web_elements
    def click_element(self,locator):
        element=self.search_element(locator)
        element.click()

    def send_data(self,locator):
        element=self.search_element(locator)
        element.send_keys()

    def drop_down(self,locator,choosed_value):
        element=Select(self.search_elements(locator))
        element.select_by_visible_text(choosed_value)

    def list_box(self,locator,user_value):
        elements=self.search_elements(locator)
        for element in elements:
            if element.text==user_value:
                element.click()
                break



