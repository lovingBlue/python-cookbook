# encoding=utf-8

'''
任务：用字符串的 translate 方法来进行快速编码，但却发现很难记住这个
方法和 string.maketrans 函数的应用细节，所以需要对它们做个简单
的封装，以简化其使用流程
'''

# 解决方案：一个返回闭包的工厂函数可以很好地完成这种任务


import string


def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans('', '')
        delete = allchars.translate(allchars, keep.translate(allchars, delete))

    def translate(s):
        return s.translate(trans, delete)
    return translate

# 选出属于指定集合的字符
digits_only = translator(keep=string.digits)
digits_only('Chris Perkins: 224-7992')		# 2247992


# 移除属于某字符集合的元素
no_digits = translator(delete=string.digits)
no_digits('Chris Perkins: 224-7992')		# 'Chris Perkins: -'

# 某个字符替换属于某指定集合的字符
digits_to_hash = translator(frm=string.digits, to='#')
print digits_to_hash('Chris Perkins: 224-7992')










