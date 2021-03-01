from account_center_page import AccountCenterPage
from base_page import BasePage, By


class HomePage(BasePage):
    member_login_button_locator = (By.CSS_SELECTOR, '.user-login-box > span:nth-child(1)')
    username_locator = (By.CSS_SELECTOR, '.th-import.grey-border.th-margin-zero input[type="text"]')
    password_locator = (By.CSS_SELECTOR, '.th-import.grey-border.th-margin-zero input[type="password"]')
    verification_code_locator = (By.CSS_SELECTOR, '.el-col.el-col-15 input[type="text"]')
    login_button_locator = (By.CSS_SELECTOR, '.primary')
    account_center_locator = (By.CSS_SELECTOR, '.user-link-box a:nth-of-type(1)')

    @property
    def member_login_button(self):
        return self.find_element(self.member_login_button_locator)

    @property
    def username_input(self):
        return self.find_element(self.username_locator)

    @property
    def password_input(self):
        return self.find_element(self.password_locator)

    @property
    def verification_code_input(self):
        return self.find_element(self.verification_code_locator)

    @property
    def login_button(self):
        return self.find_element(self.login_button_locator)

    @property
    def account_center(self):
        return self.find_element(self.account_center_locator)

    def login(self, username, password, code='123456'):
        self.member_login_button.click()
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.verification_code_input.send_keys(code)
        self.login_button.click()

    def go_to_account_center_page(self):
        self.account_center.click()
        return AccountCenterPage()
