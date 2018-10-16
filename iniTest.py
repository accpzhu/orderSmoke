# -*- coding=utf-8 -*-
import ConfigParser
import  os
'''
print os.getcwd() #获取当前工作目录路径
print os.path.abspath('.') #获取当前工作目录路径
print os.path.abspath('test.txt') #获取当前目录文件下的工作目录路径
print os.path.abspath('..') #获取当前工作的父目录 ！注意是父目录路径
print os.path.abspath(os.curdir) #获取当前工作目录路径
print os.path.abspath('.')+'\\resource\\resource.ini'
print(os.path.exists(os.path.abspath('.')+'\\resource\\resource.ini'))
'''


def func():
    cp = ConfigParser.SafeConfigParser()
    cp.read(os.path.abspath('.')+'\\resource\\resource.ini')
    cp.get('users','username')
    cp.get('users', 'password')
    cp.get('driver','driverName')
    cp.get('url','url')

func()

