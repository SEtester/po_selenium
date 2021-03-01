from selenium.common.exceptions import WebDriverException
from selenium import webdriver



class DriverNotFoundException(WebDriverException):
    """找不到driver"""
    pass


def head_less_of_chrome():
    """
        #chrome_options.add_argument("--disable-gpu") # Temporarily needed if running on Windows.
        #chrome_options.add_argument("--no-sandbox") # linux only
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    return options


if __name__ == '__main__':
    from setting import CHROME_DRIVER_FOR_MAC
    driver = webdriver.Chrome(chrome_options=head_less_of_chrome(), executable_path=CHROME_DRIVER_FOR_MAC)
