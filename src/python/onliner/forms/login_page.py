from selenium.webdriver.common.action_chains import ActionChains
from src.python.framework.base_page import BasePage
from src.resources import locators


class LoginPage(BasePage):
    def log_in(self, username, password):
        un = self.driver.find_element(*locators.LoginPageLocators.username)
        un.send_keys(username)

        psw = self.driver.find_element(*locators.LoginPageLocators.password)
        psw.send_keys(password)

        btn = self.driver.find_element(*locators.LoginPageLocators.submit_button)

        try:
            assert btn.get_attribute("class") == "auth-box__auth-submit auth__btn auth__btn--green"
            print("This is the button that I need. Let's click it!")
        except AssertionError:
            print("I think this is not the button that I need")

        action_login = ActionChains(self.driver)
        action_login.move_to_element(btn).click(btn).perform()

        self.did_page_change()