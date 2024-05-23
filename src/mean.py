def mean(number):
  sum = 0
  count = 0
  str_number = str(number)
  for letter in str_number:
          d = int(letter)
          sum += d
          count += 1
          mean = sum / count
  return mean

print(mean(794))