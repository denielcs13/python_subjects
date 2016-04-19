#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''列表操作总结'''
'''
列表是Python中最基本的数据结构，也很常用。而且列表中每一个元素不需要具有相同的类型。
列表中的每个元素都有一个索引，从 0 ~ len(list) - 1 。 
列表属于序列，序列都可以进行的操作包括索引，切片，加，乘，检查成员。
'''

__author__ = 'AJ Kipper'

'''
********************
基本操作
********************
'''

'''创建一个列表变量'''
list_one = [1,'2',3,'4']

'''获取链表长度'''

print 'Length of list_one:',len(list_one)

'''列表形式输出'''
print 'List: ',list_one

'''循环输出每个元素'''
for i in range(len(list_one)):
	print 'list_one[%d]:' % i,list_one[i]

#或者
for i in list_one:
	print i

'''删除一个列表'''
list_test = []
del list_test

'''
********************
通过索引访问元素值
********************
'''
'''输出索引为0的值'''
print list_one[0:2]
