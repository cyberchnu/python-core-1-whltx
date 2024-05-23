def squares_sum(n):
  k = 0
  for i in range(1, n + 1):
           k += i ** 2
  return k

print(squares_sum(4))