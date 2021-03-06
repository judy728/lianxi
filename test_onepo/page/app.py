import yaml
from appium import webdriver

from test_onepo.page.base_page import BasePage
from test_onepo.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = "com.xueqiu.android.common.MainActivity"
    def start(self):
        if self._driver is None:
            caps=dict()
            caps['platformName'] = "android"
            caps['deviceName'] = "test"
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps['noReset'] = True
            caps['udid'] = yaml.safe_load(open("../page/udid.yml"))['caps']['udid']
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        else:
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(3)
        return self

    def main(self) ->Main:
        return Main(self._driver)

