from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.drivers import Driver
from common.setting import TIME_OUT, POLL_FREQUENCY, PRESET_DRIVER, CHROME_DRIVER_FOR_MAC

URL = 'http://test-www.xxxx.net'


class BasePage:

    def __init__(self, path=None):
        # self.driver = Driver.driver_obj(PRESET_DRIVER)(executable_path=CHROME_DRIVER_FOR_MAC)
        self.driver = Driver.driver_obj(PRESET_DRIVER, CHROME_DRIVER_FOR_MAC)
        self.driver.maximize_window()
        self.get_url(path)

    # def __init__(self, driver, path=None):
    #     self.driver = driver
    #     self.driver.maximize_window()
    #     self.get_url(path)

    def get_url(self, path):
        if path is not None:
            url = URL + path
        else:
            url = None

        if url is not None:
            self.driver.get(url)

    def find_element(self, locator):
        element_obj = WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))

        return element_obj
