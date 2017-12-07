# encoding=utf-8
'''
任务：每次处理一个字符的方式处理字符串
'''
the_string = "12233445555555555"

# 方案1：创建一个列表，再进行操作
the_list = list(the_string)
for c in the_list:
    pass


# 方案2：列表推导式
results = [int(c) for c in the_string]


# 方案3：利用 map 函数
results = map(int, the_string)


# 获得该字符串的所有字符的集合
import sets

magic_chars = sets.Set('abeieidjjdjjd')
popins_chars = sets.Set('supercelireanfejeidjieedkdkdkkdkerueiie')
print ''.join(magic_chars & popins_chars)
