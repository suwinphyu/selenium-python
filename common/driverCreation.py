'''
Created on Nov 21, 2017

@author: nex-user001
'''
import unittest
from selenium import webdriver


class DriverStart(unittest.TestCase):


    def setUp(self):
        chromedriver="D:/python/installer/chromedriver.exe"
        self.driver= webdriver.Chrome(executable_path=chromedriver)
        self.driver.get("http://anymart.nexlabs.co")
        self.driver.implicitly_wait(10)
     
    def tearDown(self):
        self.driver.quit()


   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()