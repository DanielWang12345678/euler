list1 = []
for a in range(500):        #500 was an educated guess
  for b in range(500):
    c = 1000-a-b
    if a**2+b**2 == c**2:
      print(a*b*c)
      break
