#coding:UTF-8
'''
Created on 2018年3月22日

@author: vn0umhp
'''
'''
eval(),将字符串表达式返回一个计算结果
'''
# reg = '(2+8)*2'
# print eval(reg)

#------------列表----------
# l=['a','b','c','d','e']
# print 'l[-1]:',l[-1]     # e
# print 'l[1:]',l[1:]      #['b', 'c', 'd', 'e']
# print 'l[:-1]:',l[:-1]    #['a', 'b', 'c', 'd']
# print 'l[:-2]:',l[:-2]  #['a', 'b', 'c']
# print 'l[1]:',l[1] # b

'''
zip(): 对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
最后返回的时列表
'''
# print 'zip(l):',zip(l) #[('a',), ('b',), ('c',), ('d',), ('e',)]
# print 'zip(l,l):',zip(l,l) #[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')]
# print 'zip(l[:-1],l):',zip(l[:-1],l) #[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')]
# print 'zip(l[:-1],l[1:])',zip(l[:-1],l[1:]) #[('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]

# list1=['a','b','c']
# list2=['one','two','three']
# print zip(list1,list2)
# [('a', 'one'), ('b', 'two'), ('c', 'three')]

#---------lambda-------
'''
lambda 匿名函数
'''
# g = lambda x,y:x+y
# l = g(2,3)
# print l
# #上边等同于下边fun函数的作用
# def fun(x,y):
#     return x+y
# print fun(2, 3) 

#------------filter------
'''
filter(fun,list)
过滤掉不符合条件的元素，返回符合条件的元素组成的新列表
第一个参数是过滤条件函数，第二个参数是列表
'''
# def yuFunction(xx):
#     return xx % 2 == 0
# listyu=[1,2,3,4,5,6,7,8]
# print filter(yuFunction, listyu)
#  
# listla=[-1,-2,1,5]
# print filter(lambda x : x >0 , listla)


