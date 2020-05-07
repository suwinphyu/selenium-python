'''
Created on Nov 21, 2017

@author: nex-user001
'''
import unittest
from common.driverCreation import DriverStart
from common.checkExpectedURL import CheckURL
from selenium.webdriver.support.select import Select
import time

class Register(DriverStart,CheckURL,unittest.TestCase):

         
    def test_Register(self):
        driver=self.driver
        #Tapping MyAccount    
        myaccount_xpath="//*[@id='header']/div[2]/div/div/div[5]/div[2]"
        driver.find_element_by_xpath(myaccount_xpath).click()
        driver.find_element_by_link_text("My Account").click()
        
        #In Register Account
        driver.implicitly_wait(10)
        btnContinue_xpath="//*[@id='wrapper']/div[6]/div/aside/div/div/ul/li[1]/a[2]"
        txtFirstName_id="input-firstname"
        txtLastName_id="input-lastname"
        txtEmail_id="input-email"
        txtTel_id="input-telephone"
        txtCompany_id="input-company"
        txtAddress_id="input-address-1"
        txtCity_id="input-city"
        dropCountry_id="input-country"
        dropZone_id="input-zone"
        txtPassword_id="input-password"
        txtConfirmPassword_id="input-confirm"
        radioNewsletter_xpath="//*[@id='content']/form/fieldset[4]/div/div/label[1]"
        checkTC_xpath="//*[@id='content']/form/div/div/input[1]"
        btnSubmit_Continue_xpath="//*[@id='content']/form/div/div/input[2]"
        
        driver.find_element_by_xpath(btnContinue_xpath).click()        
        driver.implicitly_wait(10)
        
        #Filling Data
        driver.find_element_by_id(txtFirstName_id).send_keys("First Name")
        driver.find_element_by_id(txtLastName_id).send_keys("Last Name")
        driver.find_element_by_id(txtEmail_id).send_keys("email1@mailinator.com")
        driver.find_element_by_id(txtTel_id).send_keys("0912345678")
        driver.find_element_by_id(txtCompany_id).send_keys("Nexlabs")
        driver.find_element_by_id(txtAddress_id).send_keys("Address of mine")
        driver.find_element_by_id(txtCity_id).send_keys("Yangon")
        
        #country dropdown
        country=Select(driver.find_element_by_id(dropCountry_id))
        country.select_by_value("36")
        
        #zone dropdown
        zone=Select(driver.find_element_by_id(dropZone_id))
        zone.select_by_visible_text("Battambang")
        
        driver.find_element_by_id(txtPassword_id).send_keys("password")
        driver.find_element_by_id(txtConfirmPassword_id).send_keys("password")
        
        driver.find_element_by_xpath(radioNewsletter_xpath).click()
        driver.find_element_by_xpath(checkTC_xpath).click() 
       
        #register submit
        driver.find_element_by_xpath(btnSubmit_Continue_xpath).submit()  
        
        expected_url="http://anymart.nexlabs.co/index.php?route=account/success"
        actual_url=driver.current_url
        if(expected_url is actual_url):
            print "Registration is successful" 
        else:
            warning_mesg_xpath="//*[@id='wrapper']/div[6]/div[1]"
            warning_mesg = self.driver.find_element_by_xpath(warning_mesg_xpath).get_attribute('textContent')
            time.sleep(3)
            print warning_mesg       
            self.verify_url(actual_url,expected_url )
        
        
    
        
        
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()