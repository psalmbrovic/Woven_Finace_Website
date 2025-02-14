import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import Config


from Action_Page.ActionPage import LoginPage
from Action_Page.ActionPage import Payout

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(50)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://business.woven.finance/login")
    return login_page

def test_login_page_woven_website(login):
    login.enter_email("gammaspark@yahoo.com")
    login.enter_password("Password12$")
    login.click_login()

def test_payout_transaction(login):
    test_payout_transaction = Payout(login.driver)
    test_payout_transaction.Click_Payout_button
    test_payout_transaction.Initiate_payout
    test_payout_transaction.From_reserved_account
    test_payout_transaction.Click_Flex
    test_payout_transaction.Amount_button(config.PayoutAmount)
