import yaml

from pageobject.base.base import Base
from pageobject.page.home_page import HomePage


class LoginPage(Base):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx"

    def setup(self):
        pass

    def login(self):
        with open("..\\..\\case\\data\\cookie.yml") as f:
            cookie_data = yaml.safe_load(f)
        for itm in cookie_data:
            self.driver.add_cookie(itm)
        self.driver.refresh()
        return HomePage(self.driver)
