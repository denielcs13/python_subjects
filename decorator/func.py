#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'''
Know about functions in Python
functions are 'first-class' citizens in Python,meaning they can be assigned to variables, passed to other functions, etc., just like other values
'''

__author__ = 'AJ Kipper'

#Assigned to variables
def foo(name):
    return 'Hello,' + name

#You can just direct call
print foo('AJ Kipper')
#Output: Hello,AJ Kipper!

#Or you can assigned to variables
greet = foo
print greet('AJ Kipper')
#Output: Hello,World!

#As a parameter to another function
def morning(func):
    return func + ',morning'
print morning(greet('AJ Kipper'))

#Define another func in a func
def info():
    def base(name):
        return 'Hello,' + name
    return base('AJ Kipper')
print info()
#Output:Hello,AJ Kipper

#delete a func
del info


