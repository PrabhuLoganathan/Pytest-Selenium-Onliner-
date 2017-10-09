from src.python.framework.base_page import BasePage
from src.resources import locators


class ThemePage(BasePage):
    def test_is_it_right_theme(self, should_theme):
        assert should_theme == self.driver.find_element(*locators.ThemePageLocators.header).text
