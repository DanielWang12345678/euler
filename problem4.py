def palindromic():
  list1 = []
  for a in range(100,999):
    for b in range(100,999):
      c = a*b 
      c = str(c)
      c_reverse = c[::-1]
      if c_reverse == c:
        list1.append(c)
  print(list1)
print(palindromic())
