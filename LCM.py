def LCM(a, b):
  max=Max(a, b)
  min=Min(a, b)
  lcm=max
  while lcm % min != 0:
      lcm=lcm+max
  return lcm

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
