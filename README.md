# ansi-to-utf8
ANSI编码文件转换为UTF-8

# 功能和介绍
由于「.java」文件在Windows一般采用ANSI编码，而在macOS用的是UTF-8，这就导致了在Windows上写的Java文件，中文在macOS无法正常显示。现在利用Python完美转换。

# 源代码
~~~
#!/usr/bin/env python3
import codecs
import os

print("一个将ANSI编码转换为UTF-8的小工具")
filename = input('请输入需要转换为UTF-8文件的绝对路径:')
try:
	f = codecs.open(filename, 'r', 'gbk') # 由于macOS无法以ANSI读取，所以采用GBK来读
	ff = f.read()
	file_object = codecs.open(filename, 'w', 'utf-8')
	file_object.write(ff)
	print("转换完成！已覆盖源文件！")
except Exception as e:
	print('发生未知错误',e)
~~~
