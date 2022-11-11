from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.base.base import Base


class ConnectPage(Base):
    _TEXT_USER_NAME = (By.ID, "username")
    _TEXT_ACCID = (By.ID, "memberAdd_acctid")
    _TEXT_PHONE_NUMBER = (By.ID, "memberAdd_phone")
    _BTN_SAVE = (By.CSS_SELECTOR, ".member_colRight_operationBar .js_btn_save")
    _TEXT_TIPS = (By.ID, "js_tips")
    _BTN_ADD_USERS = (By.XPATH, "//div[@class='ww_operationBar']//a[@class='qui_btn ww_btn js_add_member']")

    def fill_content(self):
        self.get_element()
        return self

    def get_element(self):
        self.do_send_key(self.name, self._TEXT_USER_NAME)
        self.do_send_key(self.accid, self._TEXT_ACCID)
        self.do_send_key(self.phone_num, self._TEXT_PHONE_NUMBER)
        self.do_click(self._BTN_SAVE)

    def fill_user_details(self):
        """
        显示等待是等待所有元素相应的属性加载完的
        隐式是只能等待到dom的标签的架构加载,没有办法判断到dom的属性有没有加载出来
        :return:
        """
        WebDriverWait(self.driver, timeout=10).until(self.wait_for)
        self.get_element()
        return self

    def text_tips(self):
        text_tips = self.do_find_element(self._TEXT_TIPS).text
        return text_tips

    def wait_for(self, driver: WebDriver):
        try:
            driver.find_element(*self._BTN_ADD_USERS).click()
            return driver.find_element(*self._TEXT_USER_NAME)
        except:
            return False
