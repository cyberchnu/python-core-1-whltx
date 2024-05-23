def int_within_bounds(number, lower_bound, upper_bound):
  if type(number) != int:
         return False
  elif upper_bound > number >= lower_bound:
         return True
  else:
         return False
print(int_within_bounds(1, 1, 3))