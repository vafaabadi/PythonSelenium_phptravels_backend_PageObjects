from selenium.webdriver.common.by import By


class ReservationPage:

    def __init__(self, driver):
        self.driver = driver

    confirmname = (By.XPATH, "//span[contains(text(),'Charlie Chaplin')]")
    confirmhotel = (By.XPATH, "//h6[contains(text(),'Hyatt Regency Perth')]")
    correcttotal = (By.XPATH, "//span[contains(text(),'USD $2,483.25')]")
    payonarrivalbutton = (By.XPATH, "//button[contains(text(),'Pay on Arrival')]")
    reservedmessage = (By.XPATH, "//h4[contains(text(),'Your booking status is Reserved')]")

    def getconfirmname(self):
        return self.driver.find_element(*ReservationPage.confirmname)

    def getconfirmhotel(self):
        return self.driver.find_element(*ReservationPage.confirmhotel)

    def getcorrecttotal(self):
        return self.driver.find_element(*ReservationPage.correcttotal)

    def getpayonarrivalbutton(self):
        return self.driver.find_element(*ReservationPage.payonarrivalbutton)

    def getreservedmessage(self):
        return self.driver.find_element(*ReservationPage.reservedmessage)

    def getswitchtoalert(self):
        return self.driver.switch_to.alert
