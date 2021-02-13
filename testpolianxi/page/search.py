from selenium.webdriver.common.by import By

from testpolianxi.page.base_page import BasePage


class Search(BasePage):
    def search(self):
        self.steps("../page/search.yml")
        # self.send((By.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]'),"alibaba")
        self.find_and_click((By.XPATH,"//*[@text='阿里巴巴']"))

        return True