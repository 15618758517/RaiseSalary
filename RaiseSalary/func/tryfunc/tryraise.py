#coding:UTF-8
'''
Created on 2018年6月4日
@author: vn0umhp

@raise语句自己触发异常
语法格式 
raise [Exception [, args [, traceback]]]
Exception 是异常的类型（例如，NameError）参数标准异常中任一种，
args 是自已提供的异常参数，
最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。

@异常类型
NameError 未声明/初始化对象 (没有属性)
SyntaxError 语法错误，无效语法
'''

'''
@自定义异常类
'''
class exceptionMyError(BaseException):
    def __init__(self, err):#parameter
        self.err = err
         
try:
    raise exceptionMyError("user-defined 自定义异常")
except exceptionMyError,e:
    print "exceptionMyError is ", e.err


#标准异常类
# def test(args):
#     if args < 1:
#         raise TypeError('Invalid args',args)
#  
# try:
#     test(0)
# except TypeError,err:
#     print 1
#     print "err: ",err
# else:
#     print 2 
    
    
    


# try:
#     s = None
#     if s is None:
#         print "S 是一个空对象"
#         raise NameError
#         print "Raise 后的语句 "
#     print len(s) 
# except NameError:
#     print "未声明/初始化对象 (没有属性)"
# else:
#     print "S 不是 NameError"
# 
# try:
#     1/0
# except SyntaxError:
#     print "0不能被除，所以报语法错误，无效语法 "
# except ZeroDivisionError:
#     print "除零错误"
# else:
#     print "成功"

# ZeroDivisionError: integer division or modulo by zero