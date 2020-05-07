'''
Created on Nov 22, 2017

@author: nex-user001
'''
import unittest
from common.driverCreation import DriverStart
from common.checkExpectedURL import CheckURL

class SearchProduct(DriverStart,CheckURL,unittest.TestCase):


    def testSearch(self):
        driver=self.driver
        
        #Search
             
        txtKeyword_xpath="//*[@id='search0']/input"
        btnSearchSubmit_xpath="//*[@id='search0']/span/button"
        
        keyword_value=raw_input("Enter search keyword --> ") 
        driver.find_element_by_xpath(txtKeyword_xpath).send_keys(keyword_value)
        driver.find_element_by_xpath(btnSearchSubmit_xpath).submit()
        driver.implicitly_wait(30)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()