import random
import math
m = 0
n = 1000000
for i in range (n):
  x = random.random()
  y = random.random()
  d = math.sqrt(x**2 + y**2)
  if d <= 1:
    m = m + 1
  #print(str(i) + "   (" + str(x) + "," + str(y) + ") : d=" + str(d) + "  m=" + str(m))
pi = m*4/n
print("Pi = " + str(pi))