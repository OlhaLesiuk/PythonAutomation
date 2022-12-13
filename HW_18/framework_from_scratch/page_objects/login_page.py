from selenium.webdriver.common.by import By
from HW_18.framework_from_scratch.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _login_button = (By.CSS_SELECTOR, '.header-top [data-popup-handler]')
    _email_input_locator = (By.XPATH, '//input[@name="user_login"]')
    _password_input_locator = (By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
    _enter_button = (By.XPATH, '//button[contains(text(),"Увійти")]')
    _forget_password_button = (By.XPATH, '/html//form[@id="form-auth"]//div[@class="auth-link"]')
    _registration_button = (By.XPATH, '/html//form[@id="form-auth"]//a[@href="/ua/register/"]')

    def click_login_button(self):
        self._click(self._login_button)
        return self

    def is_email_field_displayed(self):
        return self.is_displayed(self._email_input_locator)

    def is_password_field_displayed(self):
        return self.is_displayed(self._password_input_locator)

    def set_email(self, email_value):
        self._send_keys(self._email_input_locator, email_value)
        return self

    def set_password(self, password_value):
        self._send_keys(self._password_input_locator, password_value)
        return self

    def login(self, email_value, password_value):
        self.click_login_button().set_email(email_value).set_password(password_value)
        return self

    def is_enter_button_displayed(self):
        return self.is_displayed(self._enter_button)

    def is_forget_password_link_displayed(self):
        return self.is_displayed(self._forget_password_button)

    def is_registration_button_displayed(self):
        return self.is_displayed(self._registration_button)


