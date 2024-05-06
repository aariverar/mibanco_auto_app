from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os
import time

class UTIL_MOBILE:

    @staticmethod
    def capture_screenshot(xdriver, filename, directory='screenshots'):
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, filename)
        xdriver.save_screenshot(filepath)
             