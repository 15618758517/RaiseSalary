#coding:UTF-8
'''
Created on 2018年5月16日
@author: vn0umhp
@os是对操作系统进行操作的模块。

'''
import os
# 
# print os.name #获取系统环境
# 
# print os.path
# 
# print os.path.abspath("\RF\TryExcept") #获取绝对路径
# 
# print os.getcwd() #获取当前工作目录(当前工作目录默认都是当前文件所在的文件夹)
# 
# path = os.environ.get('JAVA_HOME') #根据Key值获取环境变量里边的路径
# print path
# print path.upper() #upper()将字符串的小写字母转化为大写字母

path1 = os.environ.get('ROBOT_SYSLOG_FILE', 'NONE')
print path1

path2 = os.environ.get('ROBOT_SYSLOG_FILE')
print path2

level = os.environ.get('ROBOT_SYSLOG_LEVEL', 'level')
print level