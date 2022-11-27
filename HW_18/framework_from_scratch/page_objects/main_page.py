from selenium.webdriver.common.by import By

from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)
    __main_button = (By.CSS_SELECTOR, ".header-top [data-popup-handler]")

    def click_login_button(self):
        self.click(self.__main_button)
