#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''字符串操作总结'''

__author__ = 'AJ Kipper'


'''
********************
基本操作
********************
'''

'''创建字符串变量'''

str_one = 'Hey,I\'m AJ Kipper.This is a Test!'

'''删除字符串变量'''
str_test = 'Test.'
del str_test

'''获取字符串长度'''
print 'Length: %d' % len(str_one)

'''字符串相加'''

print '* ' + str_one + ' *'

'''字符串累加'''

print '*' * 50
print str_one * 2
print '*' * 50


'''
********************
字母大小写处理
********************
'''
#全部大写
print '全部大写：',str_one.upper()
#全部小写
print '全部小写：',str_one.lower()
#大小写互换
print '大小写互换：',str_one.swapcase()
#每个单词首字母大写
print '每个单词首字母大写：',str_one.lower().title()
#首字母大写，其余小写
print '首字母大写，其余小写：',str_one.capitalize()


'''
********************
搜索，索引相关
********************
'''
#从左搜索指定的字符串首字母所在的索引位置，如果匹配不成功返回-1
#用到string.find('string',start,end)这个内置方法
#其中start和end指定搜索范围，默认start = 0，end = -1
print 'A字母所在位置：%d' % str_one.find('AJ')

#从右搜索指定的字符串首字母所在的索引位置，如果匹配不成功返回-1
#用到string.rfind('string',start,end)这个内置方法
#其中start和end指定搜索范围，默认start = 0，end = -1
#体验find()和rfind()的区别
print '右边开始，i字母所在位置：%d' % str_one.rfind('i')
print '左边开始，i字母所在位置：%d' % str_one.find('i')

#对匹配的字符串进行统计
print '字符串中i字母有：%d 个' % str_one.count('i')

#上面的方法可以用str_one.index('str')替代，区别是index找不到会抛出异常，而find()返回-1
#自己写一个异常处理即可
def Handle(string,index_str):
	try:
		return string.index(index_str)
	except:
		return -1
print Handle(str_one,'0')


'''
********************
替换相关
********************
'''
#replace(old,new,max_replace_times)
#把指定old字符串换成new字符串，max_replace_times是从左开始替换的次数，默认是全部替换
print '把叹号改成句号',str_one.replace('!','.')
#把第一个i替换成*
print '第一个i替换成*',str_one.replace('i','*',1)
#把前两个i替换成*
print '前两个i替换成*',str_one.replace('i','*',2)


'''
********************
去空格，去指定字符
********************
'''
str_tow = ' ' + str_one + ' '
#strip(str_index)
#指定字符参数，去掉两边的第一个匹配字符，不给参数默认为空格
#只去掉左边用lstrip(),只去掉右边用rstrip()
print '两边有空格：',str_tow
print '去掉两边空格：',str_tow.strip()
print '去掉左边空格：',str_tow.lstrip()
print '去掉右边空格：',str_tow.rstrip()
print '去掉!符号：',str_one.strip('!')

#以指定的字符分割原来字符串，生成一个list对象
list_type = str_one.split('.')
print '类型：',type(list_type)
for i in list_type:
	print i

'''
********************
格式化相关
********************
'''
#给定长度参数，增加字符串长度，可以指定左右居中对齐，不够就用指定字符填充，默认是空格字符
#如果参数小于字符串本身长度，则输出以本身长度
#ljust(width,fillchar)，左对齐，不够数在右边填充指定字符
print str_one.ljust(2,'$')
print '左对齐',str_one.ljust(len(str_one) + 10,'*')

#rjust(width,fillchar)，右对齐，不够数在左边填充指定字符
print '右对齐',str_one.rjust(len(str_one) + 10,'#')

#center(width,fillchar)居中对齐，用法跟上一样
print '居中对齐',str_one.center(len(str_one) + 10,'-')

#zfill(width)，原字符串右对齐，在左边用0填充，不能自己指定填充字符
print '右对齐',str_one.zfill(len(str_one) + 10)

'''
********************
字符串判断相关
********************
'''
#判断是否以指定字符开始，返回布尔类型True或者Flase
print '以空格开始吗？',str_one.startswith(' ')

#判断是否以指定字符结束，返回布尔类型True或者Flase
print '以!结束的吗？',str_one.endswith('!')

#判断是否全是字母，isalpha(),其中alpha是一个单词，意为希腊字母第一个字母，表示最初，开端。
#返回布尔类型True或者Flase
print '全是字母吗？',str_one.isalpha()

#判断是否全是字母，isdigit(),英文单词digit是数字的意思
#返回布尔类型True或者Flase
print '全是数字吗？：',str_one.isdigit()

#判断是否全是小写，返回布尔类型True或者Flase
print '全是小写吗？：',str_one.islower()

#判断是否全是大写，返回布尔类型True或者Flase
print '全是大写吗？：',str_one.isupper()