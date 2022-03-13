import math

def isPrimeNumber(x):
    max_i = int (math.sqrt(x))
    for i in range(2, max_i + 1):
      if x % i == 0:
        return False
    return True

for x in range (2, 101):
   if isPrimeNumber(x) == True:
       print(x)

