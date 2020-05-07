'''
Created on Nov 10, 2017

@author: NEX
'''
import unittest
from HTMLTestRunner import HTMLTestRunner
from testcase import TC_001_checkLinkHome, TC_002_register, TC_003_emailLoginByInput, TC_004_checkLinkAccount, TC_005_search, TC_006_addToCart, TC_009_addToWishList
from testcase import TC_011_orderHistory
from testcase import TC_008_checkOut

suite1=unittest.loader.findTestCases(TC_001_checkLinkHome)
suite2=unittest.loader.findTestCases(TC_002_register)
suite3=unittest.loader.findTestCases(TC_003_emailLoginByInput)
suite4=unittest.loader.findTestCases(TC_004_checkLinkAccount)
suite5=unittest.loader.findTestCases(TC_005_search)
suite6=unittest.loader.findTestCases(TC_006_addToCart)
suite7=unittest.loader.findTestCases(TC_008_checkOut)
suite8=unittest.loader.findTestCases(TC_011_orderHistory)
suite9=unittest.loader.findTestCases(TC_009_addToWishList)

suite1.addTest(suite2)
suite1.addTest(suite3)
suite1.addTest(suite4)
suite1.addTest(suite5)
suite1.addTest(suite6)
suite1.addTest(suite7)
suite1.addTest(suite8)
suite1.addTest(suite9)

outfile=open("TestSuite_Result.html","w")
testrunner=HTMLTestRunner(stream=outfile,verbosity=2,title='AnyMart Report',description='Automation report')
testrunner.run(suite1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()