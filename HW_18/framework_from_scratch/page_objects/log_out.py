from selenium.webdriver.common.by import By

from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class Logout(BasePage):
    def __int__(self, driver):
        super().__init__(driver)
    __logout2_button_locator = (By.XPATH, "//a[contains(text(),'Вихід'')]")

    def click_logout_button(self):
        self._click(self.__logout2_button_locator)

    def is_logout2_button_displayed(self):
        return self._is_displayed(self.__logout2_button_locator)
