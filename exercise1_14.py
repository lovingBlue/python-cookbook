# encoding=utf-8

'''
 任务：有个包含多行文本的字符串，需要创建该字符串的一个拷贝，并在每行行首添加
 或者删除一些空格，以保证每行的缩进都是指定数目的空格数
'''

# 解决方案如下：


def reindent(s, num_spaces):
    leading_space = num_spaces * ' '
    lines = [leading_space + line.strip() for line in s.splitlines()]
    return '\n'.join(lines)


x = ''' line one
        line two
        and line three
    '''
print reindent(x, 4)


# 只在每行行首加空格
def add_spaces(s, num_add):
    white = " " * num_add
    return white + white.join(s.splitlines(True))

# 统计每行空格数


def num_spaces(s):
    return [len(line) - len(line.lstrip()) for line in s.splitlines()]


# 删除每行的空格
def del_spaces(s, num_del):
    if num_del > min(num_spaces(s)):
        raise ValueError, 'removing more spaces than there are'
    return '\n'.join([line[num_del:] for line in s.splitlines()])
