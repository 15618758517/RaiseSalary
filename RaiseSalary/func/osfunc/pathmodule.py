#coding:UTF-8
'''
Created on 2018年5月30日

@author: vn0umhp

os.path.isdir(path) 如果path是一个存在的目录,返回Ture,否则返回False。
'''
import os.path
print os.path.isdir('e:\work')
print os.path.isdir('e:\workk')

path = "e:\work"
print path.replace("\\", "\\\\") #第一个\为转义字符  将单斜杠转换成 \\
