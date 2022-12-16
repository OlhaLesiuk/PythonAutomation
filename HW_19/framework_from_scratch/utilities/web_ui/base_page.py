from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 5)

    def _wait_until_element_located(self, locator):
        return self.__wait.until(ec.presence_of_element_located(locator))

    def _wait_until_clickable(self, locator):
        return self.__wait.until(ec.element_to_be_clickable(locator))

    def _wait_until_element_visible(self, locator):
        return self.__wait.until(ec.visibility_of_element_located(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
            element.send_keys(value)

    def _click(self, locator):
        element = self._wait_until_clickable(locator)
        element.click()

    def is_displayed(self, locator):
        try:
            self._wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False
