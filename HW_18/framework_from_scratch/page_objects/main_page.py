from selenium.webdriver.common.by import By
from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_button = (By.CSS_SELECTOR, '.header-top [data-popup-handler]')

    def click_login_button(self):
        self._click(self.__login_button)

    def is_login_button_displayed(self):
        return self.is_displayed(self.__login_button)
