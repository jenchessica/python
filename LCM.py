def LCM(a, b):
  max=Max(a, b)
  min=Min(a, b)
  lcm=max
  while lcm % min != 0:
      lcm=lcm+max
  return lcm

def GCD(a, b):
    gcd=a*b/LCM(a, b)
    return int(gcd)

def EUCLID(a, b):
    c=a%b
    while c!=0:
          a=b
          b=c
          c=a%b
    return b

def Max(a, b):
    if a>b:
        return a
    else:
        return b

def Min(a, b):
    if a<b:
        return a
    else:
        return b

print(LCM(2, 3))
print(EUCLID(45, 30))
print(EUCLID(12652365, 234239835))
print(GCD(2, 3))

