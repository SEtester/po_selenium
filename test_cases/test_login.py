import unittest

from pages.home_page import HomePage
from common.setting import INDEX_PATH


class TestLogin(unittest.TestCase):

    # def test_login_success(self):
    #     index_page = HomePage(path=INDEX_PATH)
    #     username = '13286993500'
    #     password = '123456'
    #     index_page.login(username, password)
    #     index_page.driver.delete_all_cookies()

    def test_go_to_account_center_page(self):
        index_page = HomePage(path=INDEX_PATH)
        username = '13286993500'
        password = '123456'
        index_page.login(username, password)
        index_page.go_to_account_center_page()
        index_page.driver.quit()
