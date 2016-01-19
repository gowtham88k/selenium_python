import unittest
import HTMLTestRunner
import glob
#from testscripts import *
def suite():

	testSuitList=[]
	sp='/home/ingkrishna/GK/python/selenium/'
	for i in glob.glob(sp+'test_*.py'):
		testSuitList.append(i.split('/')[-1].split('.')[0])

	#scriptpath='testscripts.'
	scriptpath=''
	suitCaseSuit=[]
	for testSuit in testSuitList:
		
		#var=unittest.TestLoader().loadTestsFromTestCase(testSuit)
		var= unittest.defaultTestLoader.loadTestsFromName(scriptpath+testSuit)
		suitCaseSuit.append(var)
	return unittest.TestSuite(suitCaseSuit)
		

	#s1 = unittest.TestLoader().loadTestsFromTestCase(test_Suit_1)
	#s2 = unittest.TestLoader().loadTestsFromTestCase(test_Suit_2)
	#return unittest.TestSuite([s1,s2])

	'''

	with open(report, "a") as f:
		HTMLTestRunner.HTMLTestRunner(
					stream = f,
					title = 'Sample report',
					verbosity = 2,
					description = 'Sample test for HTMLTestRunner usage'
					).run(suite)
					

	for i in suite:
		with open(report, "w") as f:
			HTMLTestRunner.HTMLTestRunner(
						stream = f,
						title = 'Sample report',
						verbosity = 2,
						description = 'Sample test for HTMLTestRunner usage'
						).run(i)
						

					

						

	'''
def run(suite, report = "report.html"):

	with open(report, "wr") as f:
		HTMLTestRunner.HTMLTestRunner(
					stream = f,
					title = 'Sample report',
					verbosity = 2,
					description = 'Sample test for HTMLTestRunner usage'
					).run(suite)
						
if __name__ == "__main__":  
	run(suite())
	import shutil
	shutil.copy('report.html','/home/ingkrishna/report.html')
