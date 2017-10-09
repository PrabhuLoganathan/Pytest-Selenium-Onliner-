from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.resources import config


class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, config.Main.explicitly_wait_delay).until(
            EC.url_to_be(self.url), "Couldn't load page " + self.url)

    def did_page_change(self):
        WebDriverWait(self.driver, config.Main.explicitly_wait_delay).until(
            EC.url_changes(self.url), "Page didn't load in enough time.")
