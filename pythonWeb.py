import unittest
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class TestPythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')

    def test_search_in_python(self):
        self.driver.get("http://www.python.org")
        self.assertIn("Python" , self.driver.title)
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()