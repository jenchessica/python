def SingleLine(n):
    for i in range(1, n + 1):
      print('*', end='')
    print('')
    return

#SingleLine(6)
#SingleLine(5)
#SingleLine(4)

def Rectangle(m, n):
    for row in range (1, m+1):
        for col in range (1, n+1):
            print('*', end='')
        print('')
    return

#Rectangle(3, 4)

def RectangleWithFunctionCalling(m, n):
    for row in range (1, m+1):
        SingleLine(n)
    return

#RectangleWithFunctionCalling(5, 4)

def TimeTable(m, n):
    for row in range (1, m+1):
        for col in range (1, n+1):
           print(str(row) + 'x' + str(col) + '=' + str(row*col) + ' ', end='')
        print('')
    return

#TimeTable(9, 9)

def TriangleA(n):
    for row in range (1, n+1):
        for col in range (1, row+1):
            print('*', end='')
        print('')
    return

#TriangleA(4)

def TriangleB(n):
    for row in range (1, n+1):
        for col in range (-(n-1), n):
            if abs(col)<row:
                print('*', end='')
            else:
                print(' ', end='')
        print('')
    return

#TriangleB(3)

def Diamond(n):
    for row in range (-n, n+1):
        for col in range (-n, n+1):
            if abs(col)<=n-abs(row):
                print('*', end='')
            else:
                print(' ', end='')
        print('')
    return

#Diamond(3)

def ReverseDiamond(n):
    for row in range (-n, n+1):
        for col in range (-n, n+1):
            if abs(col)>n-abs(row):
                print('*', end='')
            else:
                print(' ', end='')
        print('')
    return

#ReverseDiamond(3)

def HollowDiamond(n):
    for row in range (-n, n+1):
        for col in range (-n, n+1):
            if abs(col)==n-abs(row):
                print('*', end='')
            else:
                print(' ', end='')
        print('')
    return

#HollowDiamond(3)

def Diamond3D(n):
    for z in range (-n, n+1):
        for y in range (-n, n+1):
            for x in range (-n, n+1):
                if abs(x)+abs(y)+abs(z)<=n:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('')
    return

Diamond3D(3)
