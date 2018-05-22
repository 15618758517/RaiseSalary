#coding:UTF-8
'''
Created on 2018年3月20日

@author: vn0umhp
'''
#-----Counter-----

'''
Counter 计数器
将元素进行数量统计、计数后返回一个字典,键值为元素：值为元素个数
'''
from collections import Counter 

str_a = 'abdbcdabdce'
list_a = ['a','b','a','c','a','c']
dic_a = {'a':3,'b':4,'c':5}

# print Counter(str_a) #将元素进行数量统计、计数后返回一个字典,键值为元素：值为元素个数
# #result:Counter({'b': 3, 'd': 3, 'a': 2, 'c': 2})
# print Counter(list_a)
# #result:Counter({'a': 3, 'c': 2, 'b': 1})
# print Counter(dic_a)
# #result:Counter({'c': 5, 'b': 4, 'a': 3})

#------------Counter.most_common()-----
'''
Counter.most_common() 列出前三个出现次数最多的元素及其个数的字典 
'''
m1 = Counter(str_a)
print m1.most_common(3) #列出前三个出现次数最多的元素及其个数的字典 
#Result：  [('b', 3), ('d', 3), ('a', 2)]



