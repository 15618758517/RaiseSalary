#coding:UTF-8
'''
Created on 2018年5月18日
@author: vn0umhp

@print obj 事实上是调用了sys.stdout.write(obj+'\n')，注意多了一个换行符
@标准输出和标准错误（通常缩写为 stdout 和 stderr）是建立在每个UNIX系统内的管道(pipe)。
@当你 print 某东西时，结果输出到 stdout 管道中；
@当你的程序崩溃并打印出调试信息时（象Python中的错误跟踪），结果输出到 stderr 管道中。

'''
import sys

print 'this error'

sys.stderr.write("this is a error message")
# sys.stdout.write("this is a out ")