from selenium.webdriver.common.by import By

from pageobject.base.base import Base
from pageobject.page.contact_page import ConnectPage


class HomePage(Base):
    _ADD_USER = (By.XPATH, "//*[text()='添加成员']")
    _BTN_AAD_USERS = (By.XPATH, "//*[text()='通讯录']")

    def setup(self):
        pass

    def tear_down(self):
        pass

    def tear_down_class(self):
        pass

    def click_add_user(self):
        self.do_click(self._ADD_USER)
        return ConnectPage(self.driver)

    def goto_connect_page(self):
        self.do_click(self._BTN_AAD_USERS)
        return ConnectPage(self.driver)
