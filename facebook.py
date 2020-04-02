import os
import unittest
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Chrome(executable_path='./chromedriver')


    def test_facebook_login(self):
        self.driver.get("https://www.facebook.com/")
        assert "Facebook" in self.driver.title
        email = self.driver.find_element_by_name('email')
        password = self.driver.find_element_by_name('pass')
        login = self.driver.find_element_by_id('u_0_b')
        email.clear()
        password.clear()
        email.send_keys('')
        password.send_keys('')
        login.click()
        assert "Esraa" in self.driver.page_source

 



if __name__ == '__main__':
    unittest.main()





