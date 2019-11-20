from v4 import page
from v4.base.base import Base


class PageLogin(Base):
    # click the login link
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # input username
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # input password
    def page_input_password(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # input verification code
    def page_input_verify_code(self, code):
        self.base_input(page.login_verify_code, code)

    # click login button
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # get error info
    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)

    # click button
    def page_click_err_btn_ok(self):
        self.base_click(page.login_err_btn_ok)

    # get screen shot
    def page_get_img(self):
        self.base_get_image()

    # combine
    def page_login(self, username, pwd, code):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()