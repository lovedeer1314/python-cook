# Part:一.可迭代的
# 1. 元组
元组 = (4, 5)
x, y = 元组  # unpacking解包

# 2.列表
data = ["ACME", 50, (2022, 10, 6)]
name, shares, (年, 月, 日) = data

# 3. 字符串
s = "Jane"
s1, s2, s3, s4 = s

# 4. 文件对象


# 5. 迭代器/生成器
# Part:二.占位符
data = ["ACME", 50, (2022, 10, 6)]
_, _, (_, _, day) = data
