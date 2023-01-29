class Ship:
   def __init__(self, isHorizontal, length, x, y):
    self.isHorizontal = isHorizontal
    self.length = length
    self.x = x
    self.y = y

def HitTest(guessX,guessY):
    return False

def DrawBoard(b):
      for i in range(0, len(b)):
            for j in range(0, len(b[i])):
                print(str(b[i][j]) + " ", end='')
            print()

n = 8
board =  [[0]*n for i in range(n)]

done=False

while not done:
    DrawBoard(board)
    guessX = int(input('Enter your x '))
    guessY = int(input('Enter your y '))
    isHit=HitTest(guessX,guessY)
    if isHit:
        board[guessY][guessX]=2
    else:
        board[guessY][guessX]=1
