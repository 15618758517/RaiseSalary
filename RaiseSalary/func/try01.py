#coding:utf-8
'''
Created on 2018年3月9日

@author: vn0umhp
'''

#----------------split----------------
'''
splitlines()打印元素值，默认为False,不显示换行#[0],当参数为True时，打印的元素值包含换行符
split(str,num) str代表分割符，num代表分割次数
strip() 移除字符串头尾指定的字符（默认为空格）
'''

strUsage='''  RebortFramework    ---
Version = 'Version'
'''
name = None
nameVar = None
if  not strUsage:
    print "strUsage is NONE" 
else:
    nameVar = name or strUsage.splitlines() #splitlines()打印元素值，默认为False,不显示换行#[0],当参数为True时，打印的元素值包含换行符
    print nameVar
    print strUsage.splitlines()[0]
    print strUsage.splitlines()[0].split('---') # split(str,num) str代表分割符，num代表分割次数
    print strUsage.splitlines()[0].split('---')[0]
    print strUsage.splitlines(False)[0].split('---')[0].strip() #strip() 移除字符串头尾指定的字符（默认为空格）

#--------------元组 -------------------
'''
Python的元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号，列表使用方括号。

元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
'''
# min_str,max_str = ('physics', 'chemistry', 1997, 2000),('physics', 'chemistry', 1997, 2000)
# print min_str,max_str
# print min_str[0]
# print max_str[1]
# 
# m=2
# print is_integer(m) #判断类型
# print is_string(m)

#----------------try--------------------

# try:
#     ft0 = open("try.txt","w")
#     ft0.write("这是一个可以写的文件")
# except IOError:
#     print "没有找到文件或者文件读取失败"
# else:
#     print "文件内容写入成功"
#     ft0.close()
# 
# try: 
#     ft1 = open("try2.txt","r")
#     ft1.write("测试写入文件")
# except IOError:
#     print "没有找到文件或者文件读取失败"
# else:
#     print "文件内容写入成功"
#     ft1.close()
#     
# try:
#     1/0
# except:
#     print "错误： 0不能被除"
# else:
#     print "成功"





