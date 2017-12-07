# encoding=utf-8

'''
任务：测试一个对象是否为字符串
'''

# 解决方案：利用內建的 isinstance 和 basestring


def is_string(anobj):
    return isinstance(anobj, basestring)


# 这个方案对Python标准库中的Userstring模块提供的UserString类的实例，完全
# 无能无力。如果想支持这种类型，可以直接检查一个对象的行为是否真的像字符串一
# 样。比如


def is_string_like(anobj):
    try:
        anobj + ''
    except:
        return False
    else:
        return True

