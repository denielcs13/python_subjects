#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''元组操作总结'''
'''
Python的元组与列表类似，不同之处在于元组的元素不能修改,元组使用小括号,列表使用方括号。
'''

__author__ = 'AJ Kipper'

'''
********************
基本操作
********************
'''

'''
创建一个Tuple对象
以逗号分割元素，可以不加括号
'''
#等同于tuple_obj = (1,'Hey!',3,'AJ')
tuple_obj = 1,'Hey!',3,'AJ'

'''如果创建时候只有一个元素，也要加,号表示区分'''
test = 1,
print type(test)

'''删除元组对象'''
del test

'''*******输出*********'''
'''Tuple跟List一样，都可以用下标索引访问输出(但这种做法不推荐)'''
for i in range(len(tuple_obj)):
	print 'tuple_obj[%d]:' % i,tuple_obj[i]

'''最好的做法是直接输出'''
for i in tuple_obj:
	print i

'''Tuple跟List一样，都可以用下标索引访问，也可以进行切片操作'''

print 'First element in tuple_obj:',tuple_obj[0]
print 'tuple_obj[0] ~ tuple_obj[1]:',tuple_obj[0:2]


'''
********************
元素操作
********************
'''
'''
元组是不可变类型
所以不能给元素重新赋值,不能删除单个元素
'''

'''+号操作符连接2个元组对象'''
Tobj1 = 1,2,
Tobj2 = 3,4,
New = Tobj1 + Tobj2
print 'New Tuple:',New

'''*号操作符重复元组对象'''
print 'Double:',New*2