# Creates two variables,
# firstNum and secondNum
# and adds them to list fibonacci

firstNum = 1
secondNum = 2

fibonacci = [firstNum, secondNum]

# Uses tempSum to store
# sum of two for a while.
# Shift numbers across and
# assign tempSum to secondSum
# and add secondSum to fibonacci

while secondNum < 4000000:
  tempNum = firstNum + secondNum
  firstNum = secondNum
  secondNum = tempNum
  fibonacci.append(secondNum)

totalSum = 0

# If number is even, then
# add to totalSum

for x in fibonacci:
  if x <= 4000000 and x % 2 == 0:
    totalSum += x

print(totalSum)
