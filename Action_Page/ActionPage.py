
from selenium.webdriver.support.ui import WebDriverWait
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.save_screenshot = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver 10).util(
            EC.presence_of_element_locator(SignIn.EMAIL_ADDRESS))
        enter_email.send_keys(email)
        