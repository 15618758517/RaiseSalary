#!/usr/bin/env python2
#coding:UTF-8
'''
Created on 2018年5月17日
@author: vn0umhp

==============================================

测试的执行顺序跟方法的顺序没有关系。

每个测试方法均以 test 开头，否则是不被unittest识别的。

在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，
如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果.

Python as 以 Python run 运行，不是 Python unit-test
'''
import unittest
from mathfunc  import *

class TestMathFunc(unittest.TestCase):
    
#     def setUp(self):
#         print "do some thing before test"
#         
#     def tearDown(self):
#         print "do some thing after test"
    
    def test_add(self):
        self.assertEqual(6, add(4,2), '验证add')
        self.assertNotEqual(2, add(4,2), '验证add')
    
    def test_minus(self):
        self.assertEqual(2, minus(4,2), '验证minus')
        self.assertNotEqual(0, minus(4,2), '验证minus')
    
    def test_multi(self):
        self.assertEqual(8, multi(4,2), '验证multi')
        self.assertNotEqual(10, multi(4,2), '验证multi')
    
    @unittest.skip("skip divide")
    def test_divide(self):
        self.assertEqual(2, divide(4,2), '验证divide')
        self.assertEqual(2, divide(4,2), '验证divide')

if __name__ == '__main__':
    unittest.main(verbosity=2)
        