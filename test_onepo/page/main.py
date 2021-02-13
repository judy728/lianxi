from selenium.webdriver.common.by import By

from test_onepo.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find_and_click((By.ID,'com.xueqiu.android:id/tv_search'))
        self.steps('../page/main.yml')
        return True