from selenium.webdriver.common.by import By

class SignIn:
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[1]/div/input')
    PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[2]/div/input')
    RESET_PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[3]/a')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[4]/button/div')
    CREATE_ACCOUNT = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/form/div[5]/a')
    
# class GetStarted:
#     EMAIL_ADDRESS = (By.ID, "")
#     PASSWORD = (By.ID, "")

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


