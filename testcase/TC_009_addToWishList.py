import unittest
from common.driverCreation import DriverStart
from common.checkExpectedURL import CheckURL

class AddToWishList(DriverStart,CheckURL,unittest.TestCase):  
    
    def testAddToWishList(self):
        driver=self.driver
        
        #Search
        txtKeyword_xpath="//*[@id='search0']/input"
        btnSearchSubmit_xpath="//*[@id='search0']/span/button"
        
        keyword_value=raw_input("Enter search keyword --> ") 
        driver.find_element_by_xpath(txtKeyword_xpath).send_keys(keyword_value)
        driver.find_element_by_xpath(btnSearchSubmit_xpath).submit()       
        
        
        #=======================================================================
        # #Add to Cart
        # driver.find_element_by_xpath("//*[@id='content']/div[3]/div/div/div/div[4]/button/span").click()
        # icon_wishList_xpath="//*[@id='product']/div[1]/div/div[3]/ul/li[1]/a"  
        # #WebDriverWait(driver,500).until(lambda driver:driver.find_element_by_xpath(icon_wishList_xpath))
        # driver.find_element_by_xpath(icon_wishList_xpath).click()  
        # driver.implicitly_wait(100)   
        #=======================================================================
             
        #Add to wishlistSS
        img_xpath="//*[@id='content']/div[2]/div/div[1]/div/button[2]"  
        #dropcolor_id="input-option1"
        #radio_finalcatpro_xpath="//*[@id='input-option2']/div[2]/label/span/span"
        btnWishlist_xpath="//*[@id='content']/div[3]/div/div/div/div[2]/div[4]/button[2]"
        
        driver.find_element_by_xpath(img_xpath).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(btnWishlist_xpath).click()
                
        #driver.implicitly_wait(100)   
        
       

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()