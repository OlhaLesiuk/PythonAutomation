from selenium.webdriver.common.by import By
from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class CabinetPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    __logout1_button_locator = (By.CSS_SELECTOR, ".header-top [href='\/ua\/user\/']")

    def is_logout_button_displayed(self):
        return self.is_displayed(self.__logout1_button_locator)
