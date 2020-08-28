from selenium.webdriver.common.by import By



class LogInPage:

    def __init__(self, driver):
        self.driver = driver


    username = (By.XPATH, "//form[@class='form-signin form-horizontal wow fadeIn animated animated']//input[@placeholder='Email']")
    password = (By.XPATH, "//input[@placeholder='Password']")
    loginbutton = (By.XPATH, "//button[@class='btn btn-primary btn-block ladda-button fadeIn animated btn-lg']")



    def getusername(self):
        return self.driver.find_element(*LogInPage.username)

    def getpassword(self):
        return self.driver.find_element(*LogInPage.password)

    def getlogin(self):
        return self.driver.find_element(*LogInPage.loginbutton)
