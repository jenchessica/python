import random

class Ship:
   def __init__(self, isHorizontal, length, x, y):
    self.isHorizontal = isHorizontal
    self.length = length
    self.x = x
    self.y = y

def DrawFront(b):
      print("    0 1 2 3 4 5 6 7")
      print("-------------------")
      for i in range(0, len(b)):
            print(str(i) + " | ", end='')
            for j in range(0, len(b[i])):
                print(symbols[b[i][j]] + " ", end='')
            print()
      print()

def DrawBack(b):
      print("    0 1 2 3 4 5 6 7")
      print("-------------------")
      for i in range(0, len(b)):
            print(str(i) + " | ", end='')
            for j in range(0, len(b[i])):
                print(str(b[i][j]) + " ", end='')
            print()
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

#Randomly place a ship of length, return true if successful
def PlaceRandomShip(length):
    isHorizontal = random.randrange(0, 2)
    if isHorizontal == 0:
        #this is vertical ship
        x = random.randrange(0, n)
        y = random.randrange(0, n-length+1)
        #Check all spots to ensure you can put entire ship
        for j in range(0,length):
            if back[y+j][x] == 1:
                return False
        #Put in ship
        for j in range(0,length):
            back[y+j][x]=1
    else:
        #this is horizontal ship
        y = random.randrange(0, n)
        x = random.randrange(0, n-length+1)
        #Check all spots to ensure you can put entire ship
        for j in range(0,length):
            if back[y][x+j] == 1:
                return False
        #Put in ship
        for j in range(0,length):
            back[y][x+j]=1
    return True

def PlaceRandomShipwithRetry(length):
    isSuccessful = False
    while not isSuccessful:
        isSuccessful = PlaceRandomShip(length)

symbols = [".", "M", "H"]

n = 8
front =  [[0]*n for i in range(n)]
back =  [[0]*n for i in range(n)]

PlaceRandomShipwithRetry(2)
PlaceRandomShipwithRetry(3)
PlaceRandomShipwithRetry(4)

remainingLength=9
# DrawBack(back)

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
