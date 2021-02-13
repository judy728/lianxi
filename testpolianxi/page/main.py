from selenium.webdriver.common.by import By

from testpolianxi.page.base_page import BasePage
from testpolianxi.page.search import Search


class Main(BasePage):
    def goto_search(self):
        # self.find_and_click((By.ID,'com.xueqiu.android:id/tv_search'))
        self.steps('../page/main.yml')
        return Search(self._driver)