# encoding=utf-8

# 任务：检查一个字符串是文本还是二进制

# 解决方案：如果字符串中包含了空值或者其中有超过30%的字符的高位被置1（意味着
# 该字符的码值大于126）或是奇怪的控制码，我们就认为这段数据是二进制数据

from __future__ import division
import string
text_characters = ''.join(map(chr, range(32, 127))) + '\n\r\t\b'
_null_trans = string.maketrans('', '')


def istext(s, text_characters=text_characters, threshold=0.30):
    # 若 s 包含了空值，它不是文本
    if '\0' in s:
        return False
    # 一个“空”字符串是“文本”（这是一个主观但又合理的选择）
    if not s:
        return True
    # 获得 s 的由非文本字符构成的子串
    t = s.translate(_null_trans, text_characters)
    # 如果不超过30%的字符是非文本字符，s 是字符串
    return len(t) / len(s) <= threshold
