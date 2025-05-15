import math
def prime_checker(n):
  list1 = []
  for i in range(1,math.isqrt(n)):
    if n%i == 0:
      list1.append(i)
  print(list1)
prime_checker(600851475143)
prime_checker(486847)
prime_checker(104441)
prime_checker(59569)
prime_checker(6857)
