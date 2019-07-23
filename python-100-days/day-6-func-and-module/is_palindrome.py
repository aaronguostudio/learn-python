import math
# 非常值得记住的算法
# def is_palindrome(num):
#   temp = num
#   total = 0

#   #
#   while temp > 0:
#     total = total * 10 + temp % 10
#     temp //= 10
#     print('>', total, temp)
#   return total == num

# print(is_palindrome(12321))


# self practice
# def is_palindrome(num):
#   temp = num
#   total = 0
#   while (temp > 0):
#     total = total * 10 + temp % 10
#     temp //= 10
#   return total == num


# 判断是否是回文素数
def is_palindrome(num):
  temp = num
  total = 0
  while temp > 0:
    total = total * 10 + temp % 10
    temp //= 10
  return total == num

def is_prime(num):
  end = int(math.sqrt(num))
  for factor in range(2, end):
    if num % factor == 0:
      return False
  return True if num != 1 else False

print('palindrome: ', is_palindrome(121))
print('prime: ', is_prime(121))
print(is_palindrome(121) and is_prime(121))
