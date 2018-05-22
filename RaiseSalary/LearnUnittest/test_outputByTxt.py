#coding:UTF-8
'''
Created on 2018年5月18日
@author: vn0umhp

@生成测试文件
@unittest.TextTestRunner 生成测试文件
'''
import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    
    with open("test_math_TxtReport",'a') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)