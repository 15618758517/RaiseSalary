#coding:UTF-8
'''
Created on 2018年7月12日

@author: vn0umhp
'''
import xlrd

book = xlrd.open_workbook('E:\RobotF\TestUpload\Event.xlsx')
sheet_name = book.sheet_names()
print sheet_name

sheet = book.sheets()[0]
print sheet.nrows #获取行数
print sheet.ncols #获取列数

print sheet.row(1)

print sheet.col(1)

