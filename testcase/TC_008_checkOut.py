'''
Created on Nov 22, 2017

@author: nex-user001
'''
import unittest
from common.driverCreation import DriverStart
from common.checkExpectedURL import CheckURL
import time


class CheckOut(DriverStart,CheckURL,unittest.TestCase):


    def checkOut(self):
        driver=self.driver
        #check add to cart list
        
        productname=raw_input("Enter your addtocart product name")
        print driver.find_element_by_tag_name(productname).read_lines()
        
        driver.find_element_by_tag_name("Checkout").click()
        time.sleep(5)
        
        expected_url="http://anymart.nexlabs.co/index.php?route=checkout/checkout"
        actual_url=driver.current_url
        if(expected_url is actual_url):
            print "Checkout is success" 
            
            #CheckOut detail page
            checkTC_xpath="//*[@id='content']/div/div[2]/div/section[3]/div[2]/div[2]/label/input"
            btnConfirmOrder_id="so-checkout-confirm-button"
            
            driver.find_element_by_xpath(checkTC_xpath)
            driver.find_element_by_id(btnConfirmOrder_id)
            
            self.verify_url(actual_url=actual_url, expected_url="http://anymart.nexlabs.co/index.php?route=checkout/success")
        else:
            self.verify_url(actual_url,expected_url)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()