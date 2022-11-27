from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    CHROME = 1
    FIREFOX = 2

    @staticmethod
    def create_driver(driver_id: int, is_headless=True):
        if int(driver_id) == 1:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument('--headless')
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif int(driver_id) == 2:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver
