import unittest

import logging
import sys,getpass
class baseUnitTestCase(unittest.TestCase):
	
	logger=None
	def setUp(self):
		logFileName=self.__class__.__name__
		# create logger with 'spam_application'
		self.logger = logging.getLogger(getpass.getuser())
		self.logger.setLevel(logging.DEBUG)
		# create file handler which logs even debug messages
		fh = logging.FileHandler('/home/ingkrishna/GK/python/selenium/%s.log'%(logFileName))
		fh.setLevel(logging.DEBUG)
		# create console handler with a higher log level
		ch = logging.StreamHandler()
		ch.setLevel(logging.INFO)
		# create formatter and add it to the handlers
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)
		# add the handlers to the logger
		self.logger.addHandler(fh)
		self.logger.addHandler(ch)
		
	def tearDown(self):
		pass

if __name__ == "__main__":
	unittest.main()
