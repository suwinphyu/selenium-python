'''
Created on Nov 21, 2017

@author: nex-user001
'''
import unittest
from common.driverCreation import DriverStart
import time
import xlwt

class CheckLinkHome(DriverStart,unittest.TestCase):

    def test_check_link(self):
        driver=self.driver
        wb = xlwt.Workbook(encoding="utf-8")    
        list_links=driver.find_elements_by_tag_name('a')
        ws1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True)
        
        row_count=0
        column_count=0
        
        
        
        for link in list_links:
            link_name=link.text
            link_address=link.get_attribute('href')          
            ws1.write(row_count,column_count,link_name)
            column_count+=1
            ws1.write(row_count,column_count,link_address) 
            row_count+=1 
            column_count=0   
        
        path="link_result.xls"        
        wb.save(path)        
        time.sleep(4)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()