
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locator_Page.LoacatorPage import Payout
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.save_screenshot = driver

    def login_url(self, url):
        self.driver.get(url)

    def Click_Payout(self):
        Click_Payout = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Payout_button))
        Click_Payout.click

    def Click_Initiate_payout(self):
        Click_Initiate_payout = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Click_Payout_button))
        Click_Initiate_payout.click
        
    def Click_Reserved_account(self):
        Click_Reserved_account = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.From_reserved_account))
        Click_Reserved_account.click()

    def Click_Flex(self):
        Click_Flex = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Click_Flex))
        Click_Flex.click()

    def enter_amount(self, amount):
        enter_amount = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Amount_button))
        enter_amount.send_keys(amount)

    def enter_naration(self, naration):
        enter_naration = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Naration))
        enter_naration.send_keys(naration)

    def click_Select_bank(self):
        click_Select_bank = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Select_bank))
        click_Select_bank.click()

    def enter_Beneficiary_account_no(self, Beneficiary):
        enter_Beneficiary_account_no = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Beneficiary_account_no))
        enter_Beneficiary_account_no.send_keys(Beneficiary)

    def click_Initiate_payout(self):
        click_Initiate_payout = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Initiate_payout))
        click_Initiate_payout.click()

    def enter_pin(self, Pin):
        enter_pin = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Pin))
        enter_pin.click()

    def click_confirm(self):
        click_confirm = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Payout.Confirm_button))
        click_confirm.click()


    def verify_url(self,expected_url):
         WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
         assert self.driver.current_url == expected_url, \
            f"Expected URL after login was not met. Current URL: {self.driver.current_url}"
         print("Login Successful and URL Verification Passed!")