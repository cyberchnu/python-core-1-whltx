def sum_even_nums_in_range(start, stop):
  l = 0
  for i in range(start, stop + 1):
           if i % 2 == 0:
               l += i
  return l


print(sum_even_nums_in_range(2, 5))