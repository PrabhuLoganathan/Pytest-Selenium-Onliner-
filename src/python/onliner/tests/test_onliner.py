from src.python.onliner.forms.login_page import LoginPage
from src.python.onliner.forms.main_page import MainPage
from src.python.onliner.forms.profile_page import ProfilePage
from src.python.onliner.forms.theme_page import ThemePage
from src.python.framework.browser import Browser
from src.resources import config
import pytest


@pytest.fixture(scope="module")
def setup_driver():
    browser = Browser(config.Main.webBrowser)
    browser.driver.implicitly_wait(config.Main.implicitly_wait_delay)
    yield browser.driver
    browser.driver.quit()


class TestOnliner():
    def test_onliner(self, setup_driver):
        # Go to Onliner main page
        main_page = MainPage(setup_driver, config.Onliner.mainPageUrl)
        main_page.go()

        # Try log in
        login_page = LoginPage(setup_driver, config.Onliner.loginUrl)
        login_page.go()
        login_page.log_in(config.Onliner.login, config.Onliner.password)

        # Try log out
        profile_page = ProfilePage(setup_driver, setup_driver.current_url)
        profile_page.log_out()

        # Go to the main page again, try find one of the popular themes and click on it
        main_page.go()
        theme = main_page.find_and_click_theme()

        theme_page = ThemePage(setup_driver, setup_driver.current_url)
        theme_page.test_is_it_right_theme(theme)

        main_page.go()
        main_page.find_opinions()
