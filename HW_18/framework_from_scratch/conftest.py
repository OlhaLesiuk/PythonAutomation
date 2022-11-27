import pytest
from HW_18.framework_from_scratch.page_objects.log_out import Logout
from HW_18.framework_from_scratch.page_objects.login_page import LoginPage
from HW_18.framework_from_scratch.page_objects.main_page import MainPage
from HW_18.framework_from_scratch.utilities.config_parser import ReadConfig
from HW_18.framework_from_scratch.utilities.driver_factory import DriverFactory


@pytest.fixture(scope='session')
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(create_driver):
    return MainPage(create_driver)


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def log_out_from_cabinet(create_driver):
    return Logout(create_driver)
