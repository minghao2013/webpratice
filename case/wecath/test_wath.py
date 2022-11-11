import time

import yaml
from selenium import webdriver


class TestWacth:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tear_down(self):
        pass

    def teardown_class(self):
        pass

    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        time.sleep(10)
        cookies = self.driver.get_cookies()
        with open("..\\data\\cookie.yml", mode="w") as f:
            yaml.safe_dump(cookies, f)

    def test_add_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("..\\data\\cookie.yml") as f:
            cookie_data = yaml.safe_load(f)
        for itm in cookie_data:
            self.driver.add_cookie(itm)
        self.driver.refresh()
