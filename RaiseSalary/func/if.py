#coding:UTF-8
'''
Created on 2018年3月26日

@author: vn0umhp
'''
alist = [1,50,18,12,48]
length = len(alist)
'''
冒泡排序：
列表有N个数字，相邻的两个数进行比较，第一个数跟第二个数进行比较 ，第一个数大于第二个数，则进行位置转换，
接着第二个数和第三个数进行比较，大的放后边 。以此类推，循环一轮后得出最大的数排在最后边 ，
第二轮从列表第一个开始，以此比较剩下的n-1个， 第一个跟第二个比较，第二个跟第三个比较。。得出第二个最大的数
'''
# #--------------maopaopaixu-----
# for i in range(length-1):
#     #print '1111',i,alist
#     for j in range(length-i-1):
#         #print '2222',i,j,alist
#         if alist[j]>alist[j+1]:
#             temp=alist[j]
#             alist[j]=alist[j+1]
#             alist[j+1]=temp
#             #print alist
#              
# print alist

#--------选择排序-----------
'''
选择排序：一个排序区和一个记录区 
先先定第一个数为最小值，拿着这个数跟后边的数进行第一轮比较，出现最小值，则调换两个数的位置，一轮之后，排序区加一个数，无序区减一个数，
第二轮，拿着第二个数跟后边的值比较，找出最小值，跟第二个数替换位置，
以此类推
'''
# minIndex=0
# temp=0  
# for i in range(length-1):
#     minIndex=i
#     for j in range(i+1,length):
#         if alist[j] < alist[minIndex]:
#             minIndex = j
#     temp = alist[i]
#     alist[i] = alist[minIndex]
#     alist[minIndex] = temp
#     
# print alist

     
        
