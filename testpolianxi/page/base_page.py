import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver:WebDriver = None
    def __init__(self,driver:WebDriver = None):
        self._driver = driver

    def find(self,locator):
        return self._driver.find_element(*locator)

    def find_and_click(self,locator):
        self.find(locator).click()

    def send(self,locator,value):
        self.find(locator).send_keys(value)

    def steps(self,path):
        with open(path,"r") as f :
            steps = yaml.load(f)

        for step in steps:
            action = step['action']
            if action == "find_and_click":
                self.find_and_click(step['locator'])
            elif action == 'send':
                self.send(step['locator'], step['content'])


