# encoding=utf-8

'''
任务：给定一个需要保留的字符的集合，构建一个过滤函数，并可将其应用
于任何字符串 s，函数返回一个 s 的拷贝，该拷贝只包含指定字符集合的元素
'''

# 解决方案：利用 string 对象的 translate 方法

import string
# 生成所有字符的可复用的字符串，它还可以作为一个翻译表，指明“无须翻译”

allchars = string.maketrans('', '')


def makefilter(keep):
    '''
    返回一个函数，此返回函数接受一个字符串为参数并返回字符串的一个部分拷贝，
    此拷贝只包含在 keep 中的字符，注意 keep 必须是一个普通字符串
    '''
    delchars = allchars.translate(allchars, keep)
    # 生成并返回需要的过滤函数（作为闭包）
    def thefilter(s):
        return s.translate(allchars, delchars)
    return thefilter

if __name__ == '__main__':
    just_vowels = makefilter('aeiouy')
    print just_vowels('four score and seven years ago')
# 输出：ouoeaeeyeaao
    print just_vowels('tiger, tiger burning bright')
# 输出：ieieuii


'''
技巧的关键对string模块 maketrans 函数以及字符串对象 translate 方法的理解
translate 的第一个参数为翻译表（指定的替换方式来替换），第二个参数指定的所有字符都被
删除。maketrans 是创建翻译表的一个工具函数。
'''
