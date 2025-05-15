import math
def prime_checker(n):
  for i in range(2,math.isqrt(n)+1):
    if n%i == 0:
      return False 
  return True
print(prime_checker(2))
def prime_finder(c):
  list1 = []
  counter = 1
  while len(list1)<c:
    counter+=1 
    if prime_checker(counter) == True:
      list1.append(counter)
  print(list1[-1])
prime_finder(10001)
