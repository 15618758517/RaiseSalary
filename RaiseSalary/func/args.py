#coding:UTF-8
'''
Created on 2018年3月26日
*args 可变元素数量
**kwargs 可变的字典元素
enumerate()枚举函数
format()函数

@author: vn0umhp
'''

# def print_args(*args):
#     for count,thing in enumerate(args):
#         print '{1}:{0}'.format(count,thing) #{0} {1}分别是指format里边的参数顺序，即{0}代表元素count，{1}代表元素thing
# print_args('apple','banana','cabbage')


#------format（）---------------
'''
format(arg) arg: 参数，可以用{0}，{1}等根据位置来获取参数值
                                                 字典，字典前边加入**
                                                 列表，列表前边加*
'''
student_info = {'name':'Panny','age':18}
print 'student name is {name},age is {age}'.format(**student_info) #result: student name is Panny,age is 18
print 'student name is {age},age is {name}'.format(**student_info) #result: student name is 18,age is Panny
print 'student name is {},age is {}'.format('Panny',18)
print 'student name is {},age is {}'.format(18,'Panny')
print 'student name is {1},age is {0}{1}'.format(18,'Panny')
 
student_info01 = ['Panny',18]
print 'student01 name is {},age is {}'.format(*student_info01)
# 
# #------------enumerate（）---------------
# enumerateList = ['aaa','bbb','ccc']
# print enumerate(enumerateList) #result: <enumerate object at 0x0000000002EB1CF0>
# print type(enumerate(enumerateList)) #result: <type 'enumerate'>
# print list(enumerate(enumerateList)) #result: [(0, 'aaa'), (1, 'bbb'), (2, 'ccc')]
# 
# 
# seq =['one','two','three']
# for i in enumerate(seq):
#     print i
# '''
# result:
# (0, 'one')
# (1, 'two')
# (2, 'three')
# '''
# #------
# '''
# #i,element分别代表元组里边的0，one，然后，1，two
# '''
# for  i,element in enumerate(seq):
#     print i,element 
# '''
# result:
# 0 one
# 1 two
# 2 three
# '''
#     











