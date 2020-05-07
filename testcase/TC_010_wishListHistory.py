'''
Created on Nov 22, 2017

@author: nex-user001
'''
import unittest
from common.driverCreation import DriverStart
from common.checkExpectedURL import CheckURL

class ViewCheckOutHistory(DriverStart,CheckURL,unittest.TestCase):


    def testWishListHistory(self):
        driver=self.driver        
        
        #refresh the page
        driver.refresh()
        
  
        #Tapping MyWishList    
        mywishlist_xpath="//*[@id='header']/div[2]/div/div/div[5]/div[2]"
        driver.find_element_by_xpath(mywishlist_xpath).click() 
        
        #login
        txtEmail_id="input-email"
        txtPassword_id="input-password"
        btnLoginSubmit_xpath="//*[@id='content']/div/div[2]/div/form/input[1]"
        
        email=raw_input("Enter email address--> ")        
        driver.find_element_by_id(txtEmail_id).send_keys(email)
        
        password=raw_input("Enter password -->")
        driver.find_element_by_id(txtPassword_id).send_keys(password)
        
        driver.find_element_by_xpath(btnLoginSubmit_xpath).submit()
        
        #Check Result
        expected_url="http://anymart.nexlabs.co/index.php?route=account/wishlist"
        actual_url=driver.current_url
        if(expected_url is actual_url):
            print "You are in Wish List" 
        else:
            self.verify_url(actual_url,expected_url )
            
        
       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()