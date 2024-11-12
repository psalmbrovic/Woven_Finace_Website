from selenium.webdriver.common.by import By

class SignIn:
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[1]/div/input')
    PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[2]/div/input')
    RESET_PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[3]/a')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[4]/button/div')
    CREATE_ACCOUNT = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[5]/a')
    

class CreateAnAccount:
    SIGNUP = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[5]/a')
    BUSINESS_NAME = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/form/div[1]/div/input')
    FULL_NAME = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/form/div[2]/div/input')
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/form/div[3]/div/input')
    PHONE_NUMBER = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/form/div[4]/div/input')
    PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/form/div[5]/div/input')
    TERMS_CONDITIONS = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/form/div[6]/a')
    CREATE_ACCOUNT_1 = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[3]/form/div[7]/button/div')

class GetStarted:
     GETSTARTED_BUTTON = (By.Xpath, '//*[@id="app"]/div[1]/div[1]/div[1]/div[1]')
     EDIT_BUSINESS_PROFILE = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/div[3]/div[1]/div/div[2]/button')

# class LoginLocator:
#     EMAIL_ADDRESS = (By.ID, "")
#     PASSWORD = (By.ID, "")

# class AboutUs:
#     EMAIL_ADDRESS = (By.ID, "")
#     PASSWORD = (By.ID, "")

# class Solution:
#     EMAIL_ADDRESS = (By.ID, "")
#     PASSWORD = (By.ID, "")

# class Princing:
#     EMAIL_ADDRESS = (By.ID, "")
#     PASSWORD = (By.ID, "")


