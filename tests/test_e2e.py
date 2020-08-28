import time

from pageObjects.BookingPage import BookingPage
from pageObjects.DashboardPage import DashboardPage
from pageObjects.LogInPage import LogInPage
from pageObjects.ReservationPage import ReservationPage
from tests.baseclass import baseClass


#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work



class TestOne(baseClass):

    def test_e2e(self):

        loginpage = LogInPage(self.driver)
        loginpage.getusername().send_keys("admin@phptravels.com")
        loginpage.getpassword().send_keys("demoadmin")
        loginpage.getlogin().click()
        time.sleep(5)
        dashboardpage = DashboardPage(self.driver)
        dashboardpage.getquickbooking().click()
        time.sleep(2)
        dashboardpage.getapplytaxbar().click()
        dashboardpage.getapplytaxyes().click()
        time.sleep(2)
        dashboardpage.getservicetypebar().click()
        dashboardpage.getservicetypehotels().click()
        time.sleep(2)
        dashboardpage.getcontinuetobooking().click()
        bookingpage = BookingPage(self.driver)
        bookingpage.getcustomertype().click()
        bookingpage.getselectcustomerguest().click()
        bookingpage.getfirstname().send_keys("Charlie")
        bookingpage.getlastname().send_keys("Chaplin")
        bookingpage.getmobilenumber().send_keys("01234567890")
        bookingpage.getemailaddress().send_keys("charlie_chapling@automation.com")
        bookingpage.getcheckin().send_keys("12/12/2020")
        bookingpage.getselectcheckin().click()
        time.sleep(2)
        bookingpage.getcheckout().click()
        time.sleep(2)
        bookingpage.gethotelname().click()
        bookingpage.gethotelname().click()
        time.sleep(2)
        bookingpage.getselecthotel().click()
        time.sleep(2)
        bookingpage.getroomname().click()
        time.sleep(1)
        bookingpage.getselectroom().click()
        time.sleep(3)
        bookingpage.getromanticbox().click()
        bookingpage.getflowerbox().click()
        bookingpage.getchampagne().click()
        bookingpage.getbathbox().click()
        bookingpage.getpaymenttype().click()
        bookingpage.getselectpaymenttype().click()
        bookingpage.getbooknow().click()
        CustomerName = bookingpage.getconfirmfname().text
        assert "Charlie" in CustomerName
        Total = str(bookingpage.getconfirmtotal().text)
        assert "2483.25" in Total
        #click on view invoice button
        bookingpage.getmiximizewindow()
        time.sleep(2)
        bookingpage.getviewinvoicebutton().click()
        time.sleep(2)
        #child_window = bookingpage.getwindowhandles()         #driver.window_handles[1]
        time.sleep(1)
        bookingpage.getswitchtowindow()                         #driver.switch_to.window(child_window)
        time.sleep(4)
        #to confirm the name of the client for the reservation
        reservationpage = ReservationPage(self.driver)
        FirstNameConfirmation = str(reservationpage.getconfirmname().text)
        assert "Charlie Chaplin" in FirstNameConfirmation
        HotelConfirmation = str(reservationpage.getconfirmhotel().text)
        assert "Hyatt Regency Perth" in HotelConfirmation
        CorrectTotal = str(reservationpage.getcorrecttotal().text)
        assert "USD $2,483.25" in CorrectTotal
        reservationpage.getpayonarrivalbutton().click()
        alert = reservationpage.getswitchtoalert()                           #driver.switch_to.alert
        alertMessage = alert.text
        assert "to pay at arrival?" in alertMessage
        alert.accept()
        time.sleep(4)
        ReservationConfirmed = str(reservationpage.getreservedmessage().text)
        assert "is Reserved" in ReservationConfirmed
        #print("\nWell done! This automation test, phptravels_backend, successfully passed.")
