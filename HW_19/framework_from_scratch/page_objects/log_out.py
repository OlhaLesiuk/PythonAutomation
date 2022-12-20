from selenium.webdriver.common.by import By
from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class Logout(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    _login_button = (By.CSS_SELECTOR, '.header-top [data-popup-handler]')
    _email_input_locator = (By.XPATH, '//input[@name="user_login"]')
    _password_input_locator = (By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
    _enter_button = (By.XPATH, '//button[contains(text(),"Увійти")]')
    _cabinet_exit_button = (By.CSS_SELECTOR, ".header-top [href='\/ua\/user\/']")
    _logout_button_locator = (By.CSS_SELECTOR, "[href='\/ua\/user\/logout\/']")

    def click_login_button(self):
        self._click(self._login_button)
        return self

    def set_email(self, email_value):
        self._send_keys(self._email_input_locator, email_value)
        return self

    def set_password(self, password_value):
        self._send_keys(self._password_input_locator, password_value)
        return self

    def login(self, email_value, password_value):
        self.click_login_button().set_email(email_value).set_password(password_value).click_enter_button()
        return self

    def click_enter_button(self):
        self._click(self._enter_button)
        return self

    def click_cabinet_exit_button(self):
        self._click(self._cabinet_exit_button)
        return self

    def logout(self):
        self._click(self._logout_button_locator)
        return self

    def is_login_button_displayed(self):
        return self.is_displayed(self._login_button)
