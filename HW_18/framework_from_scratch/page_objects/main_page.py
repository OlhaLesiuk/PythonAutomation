from selenium.webdriver.common.by import By
from HW_18.framework_from_scratch.page_objects.cabinet_page import CabinetPage
from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    __main_button_locator = (By.CSS_SELECTOR, "///div[@innertext='Вхід до кабінету']")

    def click_login_button(self):
        self._click(self.__main_button_locator)

    def login(self):
        self.click_login_button()
        return CabinetPage(self._driver)

    def is_login_button_displayed(self):
        return self._is_displayed(self.__main_button_locator)
