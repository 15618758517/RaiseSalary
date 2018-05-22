#coding:UTF-8
'''
Created on 2018年5月15日
@author: vn0umhp
@with的作用:　　
使用with后不管with中的代码出现什么错误，都会进行对当前对象进行清理工作。
例如file的file.close()方法，无论with中出现任何错误，都会执行file.close（）方法

@with只有特定场合下才能使用。这个特定场合只的是那些支持了上下文管理器的对象。
@什么是上下文管理器:
　　这个管理器就是在对象内实现了两个方法：__enter__() 和__exit__()

　　__enter__()方法会在with的代码块执行之前执行，__exit__（）会在代码块执行结束后执行。

　　__exit__()方法内会自带当前对象的清理方法。
'''


class my_name:
    def __enter__(self):
        '''
        @summary:使用with语句是调用，会话管理器在代码块开始前调用，返回值与as后的参数绑定 
        '''
        print("调用__enter__()方法")
        return "xiaofang"

    def __exit__(self, a, value, trace):
        '''
        @summary: 会话管理器在代码块执行完成好后调用(必须是4个参数) 
        '''
        print("调用__exit__()方法")
        print a
        print value
        print trace

def get_name():
    return my_name()

with get_name() as name:
    print "my name is ",name
    
    