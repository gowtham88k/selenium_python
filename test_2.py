import unittest
from baseUnitTestCase import baseUnitTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_2(baseUnitTestCase):

	def setUp(self):
		super(test_2,self).setUp()
		print 'started'
		self.logger.info('retreiving firefox webdriver.')
		self.driver = webdriver.Firefox()
		self.logger.info('Successfull launched the browser')
		
	def test_2(self):
		driver = self.driver
		self.logger.info('setting the url')
		driver.get("http://www.python.org")
		self.logger.info('verifying the title')
		self.assertIn("Python", driver.title)
		self.logger.info('searching for the texbox')
		elem = driver.find_element_by_name("q")
		self.logger.info('entering value into the textbox')
		elem.send_keys("pycon")
		self.logger.info('entering return key')
		elem.send_keys(Keys.RETURN)
		self.logger.info('verifying the result')
		assert "No results found." not in driver.page_source

	def tearDown(self):
		self.logger.info('closing the browser')
		self.driver.close()
		super(test_2,self).tearDown()

if __name__ == "__main__":
	unittest.main()
