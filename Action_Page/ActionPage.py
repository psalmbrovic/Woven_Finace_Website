
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

from Locator_Page.LoacatorPage import SignIn
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.save_screenshot = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(SignIn.EMAIL_ADDRESS))
        enter_email.send_keys(email)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(SignIn.PASSWORD))
        enter_password.send_keys(password)
        
    def click_login(self):
        click_login = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(SignIn.LOGIN_BUTTON))
        click_login.click()
    
    def verify_url(self,expected_url):
         WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
         assert self.driver.current_url == expected_url, \
            f"Expected URL after login was not met. Current URL: {self.driver.current_url}"
         print("Login Successful and URL Verification Passed!")