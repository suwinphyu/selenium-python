'''
Created on Nov 22, 2017

@author: nex-user001
'''
import unittest
from common.driverCreation import DriverStart
from common.checkExpectedURL import CheckURL
import time


class EmailLogin_By_Input(DriverStart,CheckURL,unittest.TestCase):


    def testLoginInput(self):
        driver=self.driver
        #Tapping MyAccount    
        myaccount_xpath="//*[@id='header']/div[2]/div/div/div[5]/div[2]"
        driver.find_element_by_xpath(myaccount_xpath).click()
        driver.find_element_by_link_text("My Account").click()
        
        #In Login Account
        driver.implicitly_wait(10)
        
        txtEmail_id="input-email"
        txtPassword_id="input-password"
        btnLoginSubmit_xpath="//*[@id='content']/div/div[2]/div/form/input[1]"
        
        email=raw_input("Enter email address--> ")        
        driver.find_element_by_id(txtEmail_id).send_keys(email)
        
        password=raw_input("Enter password -->")
        driver.find_element_by_id(txtPassword_id).send_keys(password)
        
        driver.find_element_by_xpath(btnLoginSubmit_xpath).submit()
        
        
        expected_url="http://anymart.nexlabs.co/index.php?route=account/account"
        actual_url=driver.current_url
        if(expected_url is actual_url):
            print "Login with email is successful" 
        else:
            warning_mesg_xpath="//*[@id='wrapper']/div[6]/div[1]"
            warning_mesg = self.driver.find_element_by_xpath(warning_mesg_xpath).get_attribute('textContent')
            time.sleep(3)
            print warning_mesg       
            self.verify_url(actual_url,expected_url )



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()