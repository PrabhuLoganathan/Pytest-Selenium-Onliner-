from src.resources import config
from selenium import webdriver
import sys


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


# Class for working with browser
@singleton
class Browser():
    def __init__(self, brwsr_name):
        if brwsr_name == 'Firefox':
            if sys.platform == 'linux':
                self.driver = webdriver.Firefox(
                    executable_path=config.Main.path_to_driver_gecko_linux)
            elif sys.platform == 'win64':
                self.driver = webdriver.Firefox(
                    executable_path=config.Main.path_to_driver_gecko_win64)
            elif sys.platform == 'win32':
                self.driver = webdriver.Firefox(
                    executable_path=config.Main.path_to_driver_gecko_win32)
        elif brwsr_name == 'Chrome':
            if sys.platform == 'linux':
                self.driver = webdriver.Chrome(
                    executable_path=config.Main.path_to_driver_chrome_linux)
            elif sys.platform == 'win32':
                self.driver = webdriver.Chrome(
                    executable_path=config.Main.path_to_driver_chrome_win32)
        else:
            raise NameError('Not support this browser or wrong name. Please try another browser.')
