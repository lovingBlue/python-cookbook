# encoding=utf-8

'''

任务：将一个字符转化为相应的 ASCII 或者 Unicode 码，或者反其道而行之

'''

# 方案：利用內建的 ord 和 chr 函数
print ord('a')  	# 97
print chr(97)		# a

'''
注：內建函数 ord 同样也接收长度为 1 的 Unicode 字符串作为参数，此时
它返回一个 Unicode 的码值，最大到65535。如果想把一个数字的 Unicode
码值转化为一个长度为 1 的 Unicode 字符串，可以用內建函数 unichr
'''

print ord(u'\u2020')		# 8224
print repr(unichr(8224))		# u'\u2020'

