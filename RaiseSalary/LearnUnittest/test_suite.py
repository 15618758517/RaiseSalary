#coding:UTF-8
'''
Created on 2018年5月17日
@author: vn0umhp
==================================
@怎么控制用例执行的顺序（用例可能会有先后关系，需要先执行方法A，再执行方法B）
    @添加到TestSuite中的case是会按照添加的顺序执行的
    @使用addtest()方法添加testcase
@使用addtests() + TestLoader 不按顺序执行
    @loadTestsFromName()，传入'模块名.TestCase名'
    @loadTestsFromTestCase(),传入TestCase
'''
import unittest
from test_mathfunc import TestMathFunc

 
if __name__ == '__main__':
    suite = unittest.TestSuite()
 
    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), 
             TestMathFunc("test_divide"),TestMathFunc("test_multi")]
    
    '''
    @使用addtest()方法添加testcase
    @使用addtests() + TestLoader
        @loadTestsFromName()，传入'模块名.TestCase名'
        @loadTestsFromTestCase(),传入TestCase
    '''
    #suite.addTests(tests)
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
 
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    
   

