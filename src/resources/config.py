import os


# Settings
class Main():
    webBrowser = 'Chrome'
    implicitly_wait_delay = 10
    explicitly_wait_delay = 15

    path_to_driver_gecko_linux = os.path.abspath("../../../resources/drivers/linux64_geckodriver")
    path_to_driver_chrome_linux = os.path.abspath("../../../resources/drivers/linux64_chromedriver")
    path_to_driver_gecko_win32 = os.path.abspath("../../../resources/drivers/win32_geckodriver.exe")
    path_to_driver_gecko_win64 = os.path.abspath("../../../resources/drivers/win64_geckodriver.exe")
    path_to_driver_chrome_win32 = os.path.abspath("../../../resources/drivers/win32_chromedriver.exe")


# This class contains settings of project Onliner.by
class Onliner():
    mainPageUrl = "https://www.onliner.by/"
    loginUrl = "https://profile.onliner.by/login"
    profileUrl = "https://profile.onliner.by"

    login = ""
    password = ""


