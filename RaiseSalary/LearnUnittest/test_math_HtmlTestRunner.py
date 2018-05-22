#coding:UTF-8
import unittest
# from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    deaultsuite = unittest.defaultTestLoader.discover("E:\work\RF\RaiseSalary\LearnUnittest", pattern="test_mathfunc.py")
    
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(deaultsuite)
    with open('test_math_HTMLTestReport.html',mode='wb') as f:
        runner = HTMLTestRunner(stream=f,title = "Test Math Report",description="by HTMLTestRunner",verbosity=2)
        runner.run(deaultsuite)    