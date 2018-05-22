#coding:utf-8
'''
Created on 2018年3月12日

@author: vn0umhp
'''
def runname():
    print"你好"

if __name__ == '__main__':
    print "打印name值： ",__name__  #__main__
    print "此处执行，说明执行本地代码"
else:
    print "打印name值：",__name__  #name_main
    print "此处执行，说明该模块被引用"