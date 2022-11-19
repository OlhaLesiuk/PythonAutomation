import time
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By


def test_01():
    chrome_driver = Chrome('chromedriver.exe')
    # chrome_driver.maximize_window()
    chrome_driver.get('https://makeup.com.ua/ua/')
    # time.sleep(5)
    actual_title = chrome_driver.title
    assert actual_title == 'MAKEUP - косметика і парфумерія в інтернет-магазині №1'
    # chrome_driver.close()


def test_02():
    # Config file
    user_login = 'selo6est@gmail.com'
    password = 'qwerty123'
    # Fixture
    chrome_driver = Chrome('chromedriver.exe')
    chrome_driver.maximize_window()
    chrome_driver.get('https://makeup.com.ua/ua/')

    # Page object

    cabinet_button_locator = '.header-top [data-popup-handler]'
    cabinet_button_element = chrome_driver.find_element(By.CSS_SELECTOR, cabinet_button_locator)
    cabinet_button_element.click()

    # Page object
    email_input_locator = '//input[@name="user_login"]'
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_login)

    # Page object
    password_input_locator = 'input[placeholder="Пароль"]'
    password_input_element = chrome_driver.find_element(By.CSS_SELECTOR, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    password_input_element.send_keys(Keys.ENTER)

    # Page object
    login_button_locator = '//button[contains(text(),"Увійти")]'
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    time.sleep(5)

    '''
    I tried to user relative XPath for logout!_button_locator and 
    it didn't want to interact '//a[contains(text(),'Вихід')]'
    So I used absolute Xpath instead 
    '''

    logout1_button_locator = ".header-top [href='\/ua\/user\/']"
    logout1_button_element = chrome_driver.find_element(By.CSS_SELECTOR, logout1_button_locator)
    logout1_button_element.click()

    logout2_button_locator = '//a[contains(text(),"Вихід")]'
    logout2_button_element = chrome_driver.find_element(By.XPATH, logout2_button_locator)
    logout2_button_element.click()
    chrome_driver.quit()
