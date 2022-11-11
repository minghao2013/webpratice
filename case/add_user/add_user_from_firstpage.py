from time import sleep

import yaml
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddUsersFromFirstPAge:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        f = Faker(locale="zh_CN")
        self.name = f.name()
        self.accid = f.ssn()
        self.phone_num = f.phone_number

    def tear_down(self):
        pass

    def teardown_class(self):
        pass

    def test_add_users(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("..\\data\\cookie.yml") as f:
            cookie_data = yaml.safe_load(f)
        for itm in cookie_data:
            self.driver.add_cookie(itm)
        self.driver.refresh()
        sleep(10)
        self.driver.find_element(By.XPATH, "//*[text()='通讯录']").click()
        self.driver.find_element(By.ID, "username").send_keys(self.name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(self.accid)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(self.phone_num)
        self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar .js_btn_save").click()
        save_text = self.driver.find_element(By.ID, "js_tips").text
        assert "保存成功" in save_text

    def test_add_partment(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("..\\data\\cookie.yml") as f:
            cookie_data = yaml.safe_load(f)
        for itm in cookie_data:
            self.driver.add_cookie(itm)
        self.driver.refresh()
        sleep(10)
        self.driver.find_element(By.XPATH, "//*[text()='通讯录']").click()
        self.driver.find_element(By.CLASS_NAME, "member_colLeft_top_addBtn").click()
        self.driver.find_element(By.CLASS_NAME, "js_create_party").click()
        self.driver.find_element(By.XPATH,
                                 "//label[text()='部门名称']/..//input[@class='qui_inputText ww_inputText']").send_keys("产品部")
        self.driver.find_element(By.XPATH, "//span[@class='js_parent_party_name']").click()
        self.driver.find_element(By.XPATH,
                                 "//a[@class='jstree-anchor' and contains(text(),'上海集勇企业管理中心')]").click()
        self.driver.find_element(By.XPATH, "//a[@class='qui_btn ww_btn ww_btn_Blue']").click()
        assert_text = self.driver.find_element(By.XPATH, "//div[@id='js_tips']").text
        assert "成功" in assert_text
