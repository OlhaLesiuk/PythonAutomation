from selenium.webdriver.common.by import By
from HW_18.framework_from_scratch.page_objects.cabinet_page import CabinetPage
from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input_locator = (By.XPATH, '//input[@name="user_login"]')
    __password_input_locator = (By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
    __login_button_locator = (By.XPATH, '//button[contains(text(),"Увійти")]')

    def set_email(self, email_value):
        self._send_keys(self.__email_input_locator, email_value)
        return self

    def set_password(self, password_value):
        self._send_keys(self.__password_input_locator, password_value)
        return self

    def click_login_button(self):
        self._click(self.__login_button_locator)

    def login(self, email_value, password_value):
        self.set_email(email_value).set_password(password_value).click_login_button()
        return CabinetPage(self._driver)

    def is_enter_button_displayed(self):
        return self._is_displayed(self.__login_button_locator)
