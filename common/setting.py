import os
import sys

from selenium import webdriver

# driver config
SE_DRIVERS = {
    'chrome': webdriver.Chrome,
    'safari': webdriver.Safari,
    'firefox': webdriver.Firefox,
    'edge': webdriver.Edge,
}

PRESET_DRIVER = 'chrome'

# dir path
COMMON_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.dirname(COMMON_PATH)
DRIVER_SERVER_PATH = os.path.join(ROOT_PATH, 'driver_server')
CHROME_DRIVER_FOR_MAC = os.path.join(DRIVER_SERVER_PATH, 'chromedriver_for_mac')

# sys path
sys.path.extend(
    [COMMON_PATH, ROOT_PATH, DRIVER_SERVER_PATH]
)

# webdriver wait args
TIME_OUT = 10
POLL_FREQUENCY = 0.3

# web paths
INDEX_PATH = '/th_business_index'
