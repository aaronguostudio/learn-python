# calulate triangle premeter and area
# 计算三角形面积的公式为海伦公式
import math

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))

# if a + b > c and a + c > b and c + b > a:
#   print('Premeter is %.2f' % (a + b + c))
#   p = (a + b + c) / 2
#   a = math.sqrt(p * (p - a)* (p - b)* (p - c))
#   print('Area is %.2f' % (a))
# else:
#   print('Can not construct a triangle')


# Loop
# range 产生的是

sum = 0
for x in range(101):
  sum += x

print("Sum is: %d" % (sum))


for x in range(1, 101, 2):
  print("X is: %d" % (x))
