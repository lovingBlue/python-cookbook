# encoding=utf-8

# 任务：将一个字符串转换大小写

# 解决方案：利用字符串对象的 upper 和 lower 方法

little = "one two three"

big = little.upper()           # 转换为大写
little = big.lower()           # 转换为小写
cap_string = little.capitalize()  # 第一个字母大写
title_string = little.title()    # 每个单词的第一个字母大写

