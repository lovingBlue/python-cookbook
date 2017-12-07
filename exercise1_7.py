# encoding=utf-8


# 任务：把字符串逐字符或逐词反转

# 解决方案一：切片方法
astring = 'amazing'
revchars = astring[::-1]

# 解决方案二：单词反转，先创建一个单词的列表，将这个列表反转，最后用join合并
astring = 'I am Chinese'
revwords = astring.split()
revwords.reverse()
revwords = ' '.join(revwords)		# Chinese am I

# 也可以一行解决
revwords = ' '.join(astring.split()[::-1])

# 如果想逐词反转但又同时不改变原先的空格，可以用正则分隔原字符串
import re
revwords = re.split(r'(\s+)', astring)
revwords.reverse()
revwords = ''.join(revwords)
