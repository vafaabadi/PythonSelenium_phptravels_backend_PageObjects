from selenium.webdriver.common.by import By


class BookingPage:

    def __init__(self, driver):
        self.driver = driver

    customertype = (By.ID, "selusertype")
    selectcustomerguest = (By.XPATH, "//option[contains(text(),'Guest')]")
    firstname = (By.ID, "fname")
    lastname = (By.NAME, "lastname")
    mobilenumber = (By.ID, "mobile")
    emailaddress = (By.XPATH, "//input[@id='email']")
    checkin = (By.XPATH, "//input[@id='Hotels']")
    selectcheckin = (By.XPATH, "//td[contains(@class,'active')][contains(text(),'12')]")
    checkout = (By.XPATH, "//div[5]//tr[4]//td[7]")
    hotelname = (By.XPATH, "//div[4]//div[1]//div[1]//a[1]//span[1]")
    selecthotel = (By.XPATH, "//div[contains(text(),'Hyatt Regency Perth')]")
    roomname = (By.XPATH, "//span[contains(text(),'Select Room')]")
    selectroom = (By.XPATH, "//div[contains(text(),'Standard Room')]")
    roomquantity = (By.XPATH, "//option[contains(text(),'1')]")
    romanticbox = (By.XPATH, "//input[@id='extras_4']")
    flowerbox = (By.XPATH, "//input[@id='extras_3']")
    champagne = (By.XPATH, "//input[@id='extras_2']")
    bathbox = (By.XPATH, "//input[@id='extras_1']")
    paymenttype = (By.XPATH, "//div[@class='panel panel-default rprice paytype']//div[@class='col-md-4']")
    selectpaymenttype = (By.XPATH, "//div[@class='panel panel-default rprice paytype']//option[6]")
    booknow = (By.XPATH, "//input[@class='btn btn-primary btn-lg']")
    confirmfname = (By.XPATH, "//td[contains(text(),'Charlie')]")
    confirmtotal = (By.XPATH, "//tr[1]//td[8]")
    viewinvoicebutton = (By.XPATH, "//tr[1]//td[12]//a[1]")

    def getcustomertype(self):
        return self.driver.find_element(*BookingPage.customertype)

    def getselectcustomerguest(self):
        return self.driver.find_element(*BookingPage.selectcustomerguest)

    def getfirstname(self):
        return self.driver.find_element(*BookingPage.firstname)

    def getlastname(self):
        return self.driver.find_element(*BookingPage.lastname)

    def getmobilenumber(self):
        return self.driver.find_element(*BookingPage.mobilenumber)

    def getemailaddress(self):
        return self.driver.find_element(*BookingPage.emailaddress)

    def getcheckin(self):
        return self.driver.find_element(*BookingPage.checkin)

    def getselectcheckin(self):
        return self.driver.find_element(*BookingPage.selectcheckin)

    def getcheckout(self):
        return self.driver.find_element(*BookingPage.checkout)

    def gethotelname(self):
        return self.driver.find_element(*BookingPage.hotelname)

    def getselecthotel(self):
        return self.driver.find_element(*BookingPage.selecthotel)

    def getroomname(self):
        return self.driver.find_element(*BookingPage.roomname)

    def getselectroom(self):
        return self.driver.find_element(*BookingPage.selectroom)

    def getroomquantity(self):
        return self.driver.find_element(*BookingPage.roomquantity)

    def getromanticbox(self):
        return self.driver.find_element(*BookingPage.romanticbox)

    def getflowerbox(self):
        return self.driver.find_element(*BookingPage.flowerbox)

    def getchampagne(self):
        return self.driver.find_element(*BookingPage.champagne)

    def getbathbox(self):
        return self.driver.find_element(*BookingPage.bathbox)

    def getpaymenttype(self):
        return self.driver.find_element(*BookingPage.paymenttype)

    def getselectpaymenttype(self):
        return self.driver.find_element(*BookingPage.selectpaymenttype)

    def getbooknow(self):
        return self.driver.find_element(*BookingPage.booknow)

    def getconfirmfname(self):
        return self.driver.find_element(*BookingPage.confirmfname)

    def getconfirmtotal(self):
        return self.driver.find_element(*BookingPage.confirmtotal)

    def getviewinvoicebutton(self):
        return self.driver.find_element(*BookingPage.viewinvoicebutton)

    def getmiximizewindow(self):
        return self.driver.maximize_window()

    def getwindowhandles(self):
        return self.driver.window_handles[1]

    def getswitchtowindow(self):
        child_window = self.getwindowhandles()
        return self.driver.switch_to.window(child_window)
