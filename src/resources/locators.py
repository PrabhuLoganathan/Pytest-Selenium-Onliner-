from selenium.webdriver.common.by import By


class MainPageLocators():
    themes = (By.XPATH, "//ul[contains(@class, \"project-navigation__list\")]/li/a")


class LoginPageLocators():
    # Locators for log in
    username = (By.XPATH, "//div[@id=\"auth-container__forms\"]//input[@type=\"text\"]")
    password = (By.XPATH, "//div[@id=\"auth-container__forms\"]//input[@type=\"password\"]")
    submit_button = (By.CSS_SELECTOR, "button.auth__btn")

    captcha = (By.ID, "rc-imageselect")


class ProfilePageLocators():
    # Locators for log out
    dropdown_list = (By.XPATH, "//div[@id=\"userbar\"]//a")
    logout_btn = (By.XPATH, "//div[@class=\"b-top-profile__logout\"]/a")


class ThemePageLocators():
    header = (By.TAG_NAME, "h1")