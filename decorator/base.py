#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'decorator module'

__author__ = 'AJ Kipper'

#func函数作为一个参数传给decorator函数
def decorator(func):
    print 'Hello!'
    return func

@decorator
def foo():
    print 'This is a test!'

#调用foo()函数
foo()

#Output:
#Hello! 
#This is a test!
##
