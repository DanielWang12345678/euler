import math
def prime_checker(n):
  if n <= 1:
    return False
  else:
    for i in range(2,math.isqrt(n)+1):
      if n%i == 0:
        return False 
    return True
  
def prime_sum():
  b = 0
  for i in range(2000000+1):
    if prime_checker(i) == True:
      b += i
  print(b)
prime_sum()
