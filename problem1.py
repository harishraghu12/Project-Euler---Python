totalSum = 0

# For every number below 1000,
# if the number is a multiple
# of 3 or 5, add it to totalSum

for x in range(0, 1000):
  if x % 3 == 0 or x % 5 == 0:
    totalSum += x

# Returns 233168

print(totalSum)
