from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Configuration.ConfiTest import init_driver

class Test_Login(BaseTest):
    def test_forget_password(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.get_forgot_password_link()

    def test_company_logo(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.get_company_logo("LoginPageCompanyLogo")

    def test_valid_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()

    def test_invalid_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_invalid_login()

    def test_blank_username(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_blank_username()

    def test_blank_password(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_blank_password()