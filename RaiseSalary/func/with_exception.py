#coding:UTF-8
'''
Created on 2018年5月15日
@author: vn0umhp
@存在异常的with语句
'''
class number:
    def __enter__(self):
        print "执行__enter__()方法"
        return self
    def __exit__(self,a,b,c):
        print "执行__exit__()方法"
        print "a: ",a
        print "b: ",b
        print "c: ",c
    
    def do_number(self):
        num = 10/0
        print "执行do_number"
        return num+1


with number() as result:  
    print "result is :", result.do_number()