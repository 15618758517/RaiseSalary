#coding:UTF-8
'''
Created on 2018年3月15日

@author: vn0umhp
'''
class BaseInfo:
 
    def __init__(self):
        print 'I am a Initialization method of the BaseInfo'
    
    def logInfo(self):
        print 'I am a Class method of  the BaseInfo'
    
    @property
    def score(self):
        return self.score

info = BaseInfo()
info.logInfo()
info.score=50  # 实际转化为 info.set_score(60) 
print info.score # 实际转化为 info.get_score

# class Info(BaseInfo):
#     def __init__(self):
#         print "I am a Initialization method of the Info"
# 
# T = Info()
# T.logInfo() #继承父类

