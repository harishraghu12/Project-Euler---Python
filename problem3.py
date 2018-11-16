primes = []

for x in range(1, 600851475144):
  if 600851475143 % x == 0:
    primes.append(x)

largestPrime = 0

for prime in primes:
  primeFactors = []
  for x in range(1, prime + 1):
    if prime % x == 0:
      primeFactors.append(x)
  if len(primeFactors) == 2:
    if prime > largestPrime:
      largestPrime = prime

print(largestPrime)
