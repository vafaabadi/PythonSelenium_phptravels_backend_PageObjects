from selenium.webdriver.common.by import By



class DashboardPage:

    def __init__(self, driver):
        self.driver = driver


    quickbooking = (By.XPATH, "//button[@class='btn btn-danger btn-block']")
    applytaxbar = (By.NAME, "applytax")
    applytaxyes = (By.XPATH, "//option[contains(text(),'Yes')]")
    servicetypebar = (By.ID, "servicetype")
    servicetypehotels = (By.XPATH, "//option[contains(text(),'Hotels')]")
    continuetobooking = (By.XPATH, "//button[@class='btn btn-primary']")

    def getquickbooking(self):
        return self.driver.find_element(*DashboardPage.quickbooking)

    def getapplytaxbar(self):
        return self.driver.find_element(*DashboardPage.applytaxbar)

    def getapplytaxyes(self):
        return self.driver.find_element(*DashboardPage.applytaxyes)

    def getservicetypebar(self):
        return self.driver.find_element(*DashboardPage.servicetypebar)

    def getservicetypehotels(self):
        return self.driver.find_element(*DashboardPage.servicetypehotels)

    def getcontinuetobooking(self):
        return self.driver.find_element(*DashboardPage.continuetobooking)


