# encoding=utf-8

# 任务：实现字符串对齐（左对齐、居中对齐或右对齐）

# 解决方案：利用 string 对象的 ljust、rjust 和 center 方法

print '|', 'hej'.ljust(20), '|', 'hej'.rjust(20), '|', 'hej'.center(20), '|'
# | hej                  |                  hej |         hej          |

# 默认用空格填充，也可以指定填充字符
print 'hej'.center(20, '+')
# ++++++++hej+++++++++