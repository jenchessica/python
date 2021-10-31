import LCM

def kat(a,b,c,d,e,f,captain):
    m = a*c+b
    n = d*f+e
    isNegative = False

    if captain == "*":
       p = m*n
       q = c*f
    elif captain == "+":
       q = LCM.LCM(c,f)
       p = m*q//c+n*q//f
    elif captain == "/":
       p = m*f
       q = c*n
    elif captain == "-":
       q = LCM.LCM(c,f)
       p = m*q//c-n*q//f
       if p < 0:
          isNegative = True
          q = -q

    lcm = LCM.GCD(p,q)
    cat = p//lcm
    dog = q//lcm
    hamster = cat//dog
    rat = cat%dog
    if isNegative:
       print("-" + str(hamster) + " " + str(rat) + "/" + str(dog))
    else:
       print(str(hamster) + " " + str(rat) + "/" + str(dog))


kat(1,2,3,4,5,6,"-")
