from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    _BASE_URL = ""

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        if not self.driver.current_url.startswith("https:"):
            _BASE_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
            self.driver.get(self._BASE_URL)
        faker = Faker("zh_CN")
        self.name = faker.name()
        self.accid = faker.ssn()
        self.phone_num = faker.phone_number()

    def do_find_element(self, by, value=None):
        if value:
            return self.driver.find_element(by, value)
        else:
            return self.driver.find_element(*by)

    def do_find_elements(self, by, value=None):
        if value:
            return self.driver.find_elements(by, value)
        else:
            return self.driver.find_elements(*by)

    def do_send_key(self, text, by, value=None):
        if value:
            self.do_find_element(by, value).send_keys(text)
        else:
            return self.driver.find_element(*by).send_keys(text)

    def do_click(self, by, value=None):
        if value:
            self.do_find_element(by, value).click()
        else:
            return self.driver.find_element(*by).click()


