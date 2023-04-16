class Ship:
   def __init__(self, isHorizontal, length, x, y):
    self.isHorizontal = isHorizontal
    self.length = length
    self.x = x
    self.y = y

def DrawFront(b):
      for i in range(0, len(b)):
            for j in range(0, len(b[i])):
                print(symbols[b[i][j]] + " ", end='')
            print()

def DrawBack(b):
      for i in range(0, len(b)):
            for j in range(0, len(b[i])):
                print(str(b[i][j]) + " ", end='')
            print()

def PlaceShips(ships):
    totalLength=0
    for i in range(0,len(ships)):
        ship=ships[i]
        totalLength=totalLength+ship.length
        if ship.isHorizontal:
            for j in range (0,ship.length):
                back[ship.y][ship.x+j]=1
        else:
            for j in range(0,ship.length):
                back[ship.y+j][ship.x]=1
    return totalLength

symbols = [".", "M", "H"]

n = 8
front =  [[0]*n for i in range(n)]
back =  [[0]*n for i in range(n)]

ship1=Ship(False,2,3,4)
ship2=Ship(True,3,1,6)

remainingLength=PlaceShips([ship1,ship2])
DrawBack(back)

while remainingLength>0:
    DrawFront(front)
    guessX = int(input('Enter your x '))
    guessY = int(input('Enter your y '))
    if not front[guessY][guessX] ==0:
        print("Already placed here")
    else:
        if back[guessY][guessX]==1:
            front[guessY][guessX]=2
            remainingLength=remainingLength-1
        else:
            front[guessY][guessX]=1
            
print("You win!")
