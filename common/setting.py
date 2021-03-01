import os
import sys

from selenium import webdriver

SE_DRIVERS = {
    'chrome': webdriver.Chrome,
    'safari': webdriver.Safari,
    'firefox': webdriver.Firefox,
    'edge': webdriver.Edge,
}

COMMON_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.dirname(COMMON_PATH)
DRIVER_SERVER_PATH = os.path.join(ROOT_PATH, 'driver_server')
CHROME_DRIVER_FOR_MAC = os.path.join(DRIVER_SERVER_PATH, 'chromedriver_for_mac')
