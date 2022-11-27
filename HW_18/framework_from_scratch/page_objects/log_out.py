from selenium.webdriver.common.by import By

from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class Logout(BasePage):
    def __int__(self, driver):
        super().__init__(driver)
    __logout2_button_locator = (By.XPATH, "//a[contains(text(),'Вихід'')]")

    def click_login_button(self):
        self.click(self.__logout2_button_locator)
