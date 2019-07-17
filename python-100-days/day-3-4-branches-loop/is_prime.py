# 素数，又称质数 prime number
from math import sqrt

num = int(input("请输入一个整数："))
end = int(sqrt(num))

is_prime = True

for i in range(2, end + 1):
  if num % i == 0:
    is_prime = False
    break
if is_prime and num != 1:
  print("%d is prime" % (num))
else:
  print("%d is not prime" % (num))

# start from here https://github.com/aaronguostudio/Python-100-Days/blob/master/Day01-15/04.%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9E%84.md
