largestPalindrome = 0

for x in range(100, 1000):
  for y in range(100, 1000):
    productString = str(x*y)
    if productString == productString[::-1]:
      if int(productString) > largestPalindrome:
        largestPalindrome = int(productString)

print(largestPalindrome)
