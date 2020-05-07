'''
Created on Nov 22, 2017

@author: nex-user001
'''
import unittest
from common.driverCreation import DriverStart
from common.checkExpectedURL import CheckURL
import time


class ViewOrderHistory(DriverStart,CheckURL,unittest.TestCase):


    def testOrderHistory(self):
        driver=self.driver
        #Tapping MyAccount    
        myaccount_xpath="//*[@id='header']/div[2]/div/div/div[5]/div[2]"
        driver.find_element_by_xpath(myaccount_xpath).click()
        driver.find_element_by_link_text("My Orders").click()
        time.sleep(5)
       
        
        #driver.find_element_by_xpath('//*[@title="Havai 30"]').click()
        
        #login
        txtEmail_id="input-email"
        txtPassword_id="input-password"
        btnLoginSubmit_xpath="//*[@id='content']/div/div[2]/div/form/input[1]"
        
        email=raw_input("Enter email address--> ")        
        driver.find_element_by_id(txtEmail_id).send_keys(email)
        
        password=raw_input("Enter password -->")
        driver.find_element_by_id(txtPassword_id).send_keys(password)
        
        driver.find_element_by_xpath(btnLoginSubmit_xpath).submit()
        
        self.save_screenshot()
        
        #Check Result
        expected_url="http://anymart.nexlabs.co/index.php?route=account/order"
        actual_url=driver.current_url
        if(expected_url is actual_url):
            print "You are in Order History" 
        else:
            self.verify_url(actual_url,expected_url )
        
    def save_screenshot(self):
        name = "order_history"
        self.driver.get_screenshot_as_file(name + ".png")  

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()