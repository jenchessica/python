import matplotlib.pyplot as plt

# How to Adjust Marker Size in Matplotlib?
#   https://www.geeksforgeeks.org/how-to-adjust-marker-size-in-matplotlib/
# Insert a dot at a certain point on a line with matplotlib
#    https://stackoverflow.com/questions/31502456/insert-a-dot-at-a-certain-point-on-a-line-with-matplotlib
# matplotlib.pyplot.plot reference
#    https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

class Position:
   def __init__(self, x, y):
    self.x = x
    self.y = y

r = 0.01

romeo = Position(0, 0)
juliet = Position(100, 0)
habibi = Position(100, 100)
shurik = Position(0, 100)

epsilon = 0.00001

def CalculateNewPosition(petA, petB):
    # newX = petA.x + r*(petB.x-petA.x)
    # newY = petA.y + r*(petB.y-petA.y)
    # newPosition = Position(newX, newY)
    # return newPosition
    return Position(petA.x + r*(petB.x-petA.x), petA.y + r*(petB.y-petA.y))

while not (abs(romeo.x-50)<epsilon and abs(romeo.y-50)<epsilon):
    plt.plot(romeo.x,  romeo.y, 'g.', markersize=5)
    plt.plot(juliet.x, juliet.y, 'y.', markersize=5)
    plt.plot(habibi.x, habibi.y, 'r.', markersize=5)
    plt.plot(shurik.x, shurik.y, 'b.', markersize=5)

    newRomeo = CalculateNewPosition(romeo, juliet)
    newJuliet = CalculateNewPosition(juliet, habibi)
    newHabibi = CalculateNewPosition(habibi, shurik)
    newShurik = CalculateNewPosition(shurik, romeo)

    romeo = newRomeo
    juliet = newJuliet
    habibi = newHabibi
    shurik = newShurik

plt.axis([-10, 110, -10, 110])        # Modified axis
plt.show()
