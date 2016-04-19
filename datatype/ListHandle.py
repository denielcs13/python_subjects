#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''列表操作总结'''
'''
列表是Python中最基本的数据结构，也很常用。而且列表中每一个元素不需要具有相同的类型。
列表中的每个元素都有一个索引，从 0 ~ (len(list) - 1)。 
列表属于序列，序列都可以进行的操作包括索引，切片，加，乘，检查成员。
'''

__author__ = 'AJ Kipper'

'''
********************
基本操作
********************
'''

'''创建一个列表变量'''
list_one = [-1,2,'AJ','What\'s up']

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

'''两个列表相加，顺序取决于前后'''
list_1 = [1,2]
list_2 = [3,4]
print 'New list:',list_1 + list_2

'''用list*num进行重复'''

print 'One repetition:',list_one*2

'''删除列表，用逗号分隔，其实是创建了一个元组对象，元素是要删除的列表对象'''
del list_1,list_2

'''判断元素是否在列表，返回值是布尔类型True或者False'''
print 'AJ' in list_one
print 'AJ Kipper' in list_one

'''
********************
列表的查，用下标表索引index
********************
'''
'''通过下标索引访问元素'''
'''第一种'''
'''第一个索引是0，最后一个是(len(list_one) - 1)'''
for i in range(len(list_one)):
	print 'list_one[%d]:' % i,list_one[i]

'''第二种'''
'''第一个索引是- len(list_one) ，最后一个是 -1'''
for i in range(-len(list_one),0):
	print 'list_one[%d]' % i,list_one[i]

'''通过元素值访问对应的下标索引，如果元素不存在，报错提示'''
list_test = [1,2,3,4]
def Index(list_seq,element):
	try:
		print element,'is at index:',list_seq.index(element)
	except Exception,e:
		print Exception,':',e
Index(list_test,1)
Index(list_test,10)

'''通过索引截取列表'''
'''list_one[i:j]，其中范围是 >=i 和 <j，j>i'''
'''数值不能超过索引范围，会报错'''
print 'list_one[0] ~ list_one[1]:',list_one[0:2]
print 'list_one[-3] ~ list_one[-2]:',list_one[-3:-1]


'''
********************
列表的更和改，对元素进行修改，更新
********************
'''
'''用范围内下标索引直接赋值'''
'''超出列表范围内的不能直接赋值'''
list_one[0] = 'Hey!'
'''这样会报错'''
try:
	list_one[4] = 'Test'
except Exception,e:
	print Exception,':',e

'''用内置方法insert(index,new_element) + 下标索引来插入新元素'''
'''
------用法说明-------
如果index的值在索引范围内，则直接插入
如果index的值超出索引范围
1. 如果比索引的最大值大，则插在末尾
2. 如果比索引的最小值小，则插在开头

'''
list_one.insert(0,'Start')
print 'Inserted:',list_one

'''用内置方法append()添加元素'''
list_one.append('End!')
print 'Appended:',list_one

'''
********************
列表的删，对元素进行删除
********************
'''
'''用范围内下标索引删除'''
del list_one[2]
print 'Deleted:',list_one

'''用内置方法remove(element)移除元素，一次只能移除最先匹配到的元素'''
list_test = [1,2,2,3,5,3]
list_test.remove(2)
print 'Removed:',list_test
del list_test

'''用内置方法pop(index)移除元素，并返回弹出的值
弹出索引对应的元素，默认弹出最后一个，不能超出索引范围'''
list_test = [1,2,2,3,5,3]
list_test.pop(2)
print 'Poped index 2:',list_test
list_test.pop()
print 'Poped last one:',list_test
del list_test


'''
********************
其他内置函数对列表的操作支持
********************
'''
'''
----cmp(list1,list2)函数----
参数说明：
list1：要比较的第一个list
list2：要比较的第二个list
返回值说明：
list1 > list2 return 1
list1 < list2 return -1
list1 = list2 return 0
如果比较的两个元素是同种类型的,则比较其值,返回结果。
如果两个元素不是同一种类型,则检查它们是否是数字。
1. 如果是数字,执行必要的数字强制类型转换,然后比较。
2. 如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
3. 否则,通过类型名字的字母顺序进行比较。
如果有一个列表首先到达末尾,则另一个长一点的列表"大"。
如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。
'''
#list_one = ['A','B']
#list_tow = ['B','A']
#print cmp(list_one,list_tow)
