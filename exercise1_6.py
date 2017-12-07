# encoding=utf-8

# 任务：将小的字符串合并成一个大字符串

# 解决方案：用字符串操作符 join

pieces = ['djd', 'aejej', 'eieii']
large_string = ''.join(pieces)

# 如果把存储在一些变量中的字符串片段拼接起来，使用字符串格式化操作符 %s

small1 = 'a'
small2 = 'b'
small3 = 'c'
large_string = '%s%s something %s yet more' % (small1, small2, small3)

# 最好不要用 + 拼接字符串
