#coding:UTF-8
'''
Created on 2018年5月29日

@author: vn0umhp

sys.argv 是一个数组，argv[0]是文件目录，之后的是 外部命令，需要在命令行输入命令才能输出结果，否则运行会报错。
Sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，关键就是要明白这参数是从程序外部输入的，
                            而非代码本身的什么地方，要想看到它的效果就应该将程序保存了，从外部来运行程序并给出参数。
'''
import sys

# print sys.argv
print 'sys.argv[0]: ',sys.argv[0] #文件目录
print 'sys.argv[1]: ',sys.argv[1] #外部命令 即命令行执行时 输入的命令 如命令行输入 python sysargev what,则输出的是 what
print 'sys.argv[2]: ',sys.argv[2] #命令行输入 python sysargv.py nihao woshi lxf 则命令行输出的如下
'''
命令行执行结果如下
E:\work\RF\RaiseSalary\RaiseSalary\func\sysfunc>python2 sysargv.py
sys.argv[0]:  sysargev.py

E:\work\RF\RaiseSalary\RaiseSalary\func\sysfunc>python2 sysargv.py what
sys.argv[0]:  sysargev.py
sys.argv[1]:  what

E:\work\RF\RaiseSalary\RaiseSalary\func\sysfunc>python2 sysargv.py nihao woshi
lxf
sys.argv[0]:  sysargev.py
sys.argv[1]:  nihao
sys.argv[2]:  woshi
'''