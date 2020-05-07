'''
Created on Nov 22, 2017

@author: nex-user001
'''
import unittest


class CheckURL(unittest.TestCase):


    def verify_url(self, actual_url, expected_url):
        unittest.TestCase.assertEquals(self, actual_url, expected_url, "Actual url: " + actual_url + " is not equal to expected url: " + expected_url)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()