from selenium.webdriver.common.by import By

from pageobject.base.base import Base


class UserListPage(Base):
    _TEXT_TIPS = (By.ID, "js_tips")

