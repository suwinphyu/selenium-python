'''
Created on Nov 22, 2017

@author: nex-user001
'''
import unittest
from common.driverCreation import DriverStart
from common.checkExpectedURL import CheckURL
#from selenium.webdriver.support.select import Select


class AddToCart(DriverStart,CheckURL,unittest.TestCase):

    def testAddToCart(self):
        driver=self.driver
        
        #Search
        txtKeyword_xpath="//*[@id='search0']/input"
        btnSearchSubmit_xpath="//*[@id='search0']/span/button"
        
        keyword_value=raw_input("Enter search keyword --> ") 
        driver.find_element_by_xpath(txtKeyword_xpath).send_keys(keyword_value)
        driver.find_element_by_xpath(btnSearchSubmit_xpath).submit()       
              
             
        #Add to Cart
        img_xpath="//*[@id='content']/div[2]/div/div[1]/div/button[2]"  
        #dropcolor_id="input-option1"
        #radio_finalcatpro_xpath="//*[@id='input-option2']/div[2]/label/span/span"
        btnSubmitaddtocart_xpath="//*[@id='content']/div[3]/div/div/div/div[2]/div[4]/button[1]"
        driver.find_element_by_xpath(img_xpath).click()  
        #driver.implicitly_wait(100)   
             
        
        #detail add to cart page_test
        #=======================================================================
        # color=Select(self.driver.find_element_by_id(dropcolor_id))
        # color.select_by_value("1")        
        # driver.find_element_by_xpath(radio_finalcatpro_xpath).click()        
        #=======================================================================
        driver.find_element_by_xpath(btnSubmitaddtocart_xpath).click()  
              
       
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()