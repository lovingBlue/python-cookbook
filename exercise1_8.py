# encoding=utf-8

# 任务：检查字符换中是否出现了某字符集合中的字符

# 解决方案一：


def contains_any(seq, aset):
    '''检查序列 seq 是否含有 aset 中的项'''
    for c in seq:
        if c in aset:
            return True
    return False


# 解决方案二：
import itertools


def contains_any(seq, aset):
    for item in itertools.ifilter(aset.__contains__, seq):
        return True
    return False


def contains_only(seq, aset):
    '''检查序列 seq 是否含有 aset 的项'''
    for c in seq:
        if c not in aset:
            return False
    return True

def contains_all(seq, aset):
	'''检查序列 seq 是否含有 aset 的所有项'''
	return not set(aset).difference(seq)

# set(a).difference(b) 返回 a 集合中所有不属于 b 的元素

L1 = [1, 2, 3, 3]
L2 = [1, 2, 3, 4]
set(L1).difference(L2)		# set([])
set(L2).difference(L1)		# set([4])
contains_all(L1, L2)		# False
contains_all(L2, L1)		# True




















