# encoding=utf-8

# 任务：获取字符串的某个部分

# 解决方案一：切片，缺点只能取得一个字段

theline = 'Youth is not a time of life; \
it is a state of mind; it is not a matter of rosy cheeks, \
red lips and supple knees; it is a matter of the will, \
a quality ofthe imagination, a vigor of the emotions; \
it is the freshness of the deep springs of life. '
afield = theline[3:8]

# 解决方案二：利用struct模块下的unpack

import struct
# 得到一个5字节的字符串，跳过3字节，得到两个8字节字符串，以及其余部分：
baseformat = "5s 3x 8s 8s"
# theline超出的长度也由这个base-format确定
numremain = len(theline) - struct.calcsize(baseformat)
# 用合适的 s 或 x 字段完成格式，然后 unpack
format = "%s %ds" % (baseformat, numremain)
l, s1, s2, t = struct.unpack(format, theline)

# 如果想跳过“其余部分”，只需要给出正确的长度，拆解出theline的开头部分的数据即可
l, s1, s2 = struct.unpack(baseformat, theline[:struct.calcsize(baseformat)])

# 如果需要获取 5 字节一组的数据，可以利用带列表推导的切片方法
fivers = [theline[k: k + 5] for k in xrange(0, len(theline), 5)]

# 把字符切成一个个单独的字符更加容易
chars = list(theline)

# 如果想把数据切成指定长度的列， 用带LC的切片方法通常是最简单的
cuts = [8, 14, 20, 26, 30]
pieces = [theline[i: j] for i, j in zip([0] + cuts, cuts + [None])]

# 在LC中调用zip, 返回的是一个列表，其中每项都是形如（cuts[k],cuts[k+1]）这样的数对,
# 除了第一项和最后一项，这两项分别是（0，cuts[0]）和 （cuts[len(cuts)-1,None]）

