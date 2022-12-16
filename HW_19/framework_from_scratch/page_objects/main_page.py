from selenium.webdriver.common.by import By
from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_button = (By.CSS_SELECTOR, '.header-top [data-popup-handler]')
    _search_field_locator = (By.CSS_SELECTOR, '#search-input')
    _ukrainian_language_locator = (By.CSS_SELECTOR, '.footer-lang li:nth-of-type(1) .footer-lang__link')

    def click_login_button(self):
        self._click(self.__login_button)

    def is_login_button_displayed(self):
        return self.is_displayed(self.__login_button)

    def is_search_field_clickable(self):
        return self.is_displayed(self._search_field_locator)

    def is_ukrainian_language_default(self):
        return self.is_displayed(self._ukrainian_language_locator)
