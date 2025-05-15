def sum_square_difference(n):
  list1 = []
  list2 = []
  for i in range(n+1):
    list1.append(i**2)
  sum_of_squares = sum(list1)
  for j in range(n+1):
    list2.append(j)
  square_of_sum = (sum(list2)**2)
  print(square_of_sum - sum_of_squares)
print(sum_square_difference(100))
