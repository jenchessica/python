def calculate_sum():
    #preallocate an array of eleven elements with initial value zeroes
    sum = [0]*11

    #put in the seed value, which is sum[1]
    sum[1] = 1

    #now start the induction to calculate sum[n]
    for n in range(2, 11):
        #below is the induction formula
        sum[n]=sum[n-1]+n
        print("sum(" + str(n) + ")=" + str(sum[n]))

calculate_sum()

def calculate_factorial():
    #preallocate an array of seven elements with initial value zeroes
    factorial = [0]*7

    #put in the seed value, which is factorial[1]
    factorial[1] = 1

    #now start the induction to calculate factorial[n]
    for n in range(2, 7):
        #below is the induction formula
        factorial[n]=factorial[n-1]*n
        print("factorial(" + str(n) + ")=" + str(factorial[n]))

calculate_factorial()

def calculate_squares():
    #preallocate an array of eleven elements with initial value zeroes
    f = [0]*11

    #put in the seed value, which is f[1]
    f[1] = 1

    #now start the induction to calculate f[n]
    for n in range(2, 11):
        #below is the induction formula
        f[n]=f[n-1]+2*n-1
        print("square(" + str(n) + ")=" + str(f[n]))

calculate_squares()

def calculate_cubes():
    #preallocate an array of eleven elements with initial value zeroes
    c = [0]*11

    #put in the seed value, which is c[1]
    c[1] = 1

    #now start the induction to calculate c[n]
    for n in range(2, 11):
        #below is the induction formula
        c[n]=c[n-1]+3*(n-1)**2+3*(n-1)+1
        print("cube(" + str(n) + ")=" + str(c[n]))

calculate_cubes()
