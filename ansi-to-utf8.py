#!/usr/bin/env python3
import codecs
import os

print("一个将ANSI编码转换为UTF-8的小工具")
filename = input('请输入需要转换为UTF-8文件的绝对路径:')
try:
	f = codecs.open(filename, 'r', 'gbk')
	ff = f.read()
	file_object = codecs.open(filename, 'w', 'utf-8')
	file_object.write(ff)
	print("转换完成！已覆盖源文件！")
except Exception as e:
	print(e)
