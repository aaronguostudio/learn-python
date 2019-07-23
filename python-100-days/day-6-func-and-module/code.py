from module1 import foo as m1
from module2 import foo as m2

# function and module
# python 不支持重载，但是支持定义函数参数的默认值
# python 也支持可变参数

# 可变参数
def add(*args):
  total = 0
  for val in args:
    total += val
  return total

print(add(1,2,3,4,5,6))
print(add(1,2,3))

m1()
m2()
