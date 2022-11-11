from pageobject.page.login_page import LoginPage


class TestWatch:

    def test_add_user(self):
        text_tips = LoginPage().login().click_add_user().fill_content().text_tips()
        assert "保存成功" in text_tips

    def test_from_connact_page(self):
        text_tips = LoginPage().login().goto_connect_page().fill_user_details().text_tips()
        assert "保存成功" in text_tips
