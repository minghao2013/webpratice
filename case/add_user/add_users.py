from time import sleep

import yaml
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddUsers:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        pass

    def teardown_class(self):
        pass

    def test_add_users(self):
        f = Faker(locale="zh_CN")
        name = f.name()
        phone_num = f.phone_number()
        accid = f.ssn()

        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("..\\data\\cookie.yml") as f:
            cookie_data = yaml.safe_load(f)
        for itm in cookie_data:
            self.driver.add_cookie(itm)
        self.driver.refresh()
        sleep(10)

        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(accid)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone_num)
        self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_operationBar .js_btn_save")[0].click()
        save_text = self.driver.find_element(By.ID, "js_tips").text
        assert "保存成功" in save_text
