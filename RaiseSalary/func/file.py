#coding:utf_8
'''
Created on 2018年3月9日

@author: vn0umhp
'''

fo_write = open("foo.txt","w+") # W写，r读，w+，r+读写 ，a 追加内容
print"文件名：",fo_write.name
print"是否打开：",fo_write.closed
print"访问模式：",fo_write.mode
print"末尾是否强制加空格：",fo_write.softspace  #    如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

fo_write.write("写入第一句话") #写入一句话
fo_write.close()

fo_read = open("foo.txt","r") 
filestr = fo_read.read() #读取文件内容
print "读取的文件内容为：",filestr
fo_read.close()

'''
报错：中文乱码  
修改： 添加#coding:utf-8

报错： AttributeError: type object 'file' has no attribute 'open'，file没有open属性 
修改： file.open 改为open

报错：TypeError: 'str' object is not callable 列表的STR的对象不可赎回     
修改： fo.name() 改成 fo.name，该类错误有可能时覆盖或调用了内置函数

报错： IOError: File not open for reading
修改： 读写方式  W 改成  W+

'''