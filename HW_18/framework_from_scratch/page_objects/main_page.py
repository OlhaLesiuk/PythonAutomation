from selenium.webdriver.common.by import By
from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)
    __main_button_locator = (By.CSS_SELECTOR, ".header-top [data-popup-handler]")

    def click_login_button(self, locator):
        element = self.wait_until_clickable(locator)
        element.click()

    def is_main_page_button_displayed(self):
        return self.is_displayed(self.__main_button_locator)
