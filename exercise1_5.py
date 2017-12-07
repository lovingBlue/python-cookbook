# encoding=utf-8

# 任务：获得一个开头和末尾没有多余空格的字符串

# 解决方案：利用字符串对象的 lstrip、rstrip 和 strip 方法


x = '    hej  '
print '|' + x.lstrip() + '|'		# |hej  |
print '|' + x.rstrip() + '|'		# |    hej|
print '|' + x.strip() + '|'		# |hej|


x = 'xyxxyy hejyx  yyx'
print '|' + x.strip('xy') + '|'		# | hejyx  |