from selenium.webdriver.common.action_chains import ActionChains

from src.python.framework.base_page import BasePage
from src.resources import locators


class ProfilePage(BasePage):
    def log_out(self):
        dd_list = self.driver.find_element(*locators.ProfilePageLocators.dropdown_list)
        logout_btn = self.driver.find_element(*locators.ProfilePageLocators.logout_btn)

        action_logout = ActionChains(self.driver)
        action_logout.click(dd_list).move_to_element(logout_btn).click(logout_btn).perform()

        self.did_page_change()