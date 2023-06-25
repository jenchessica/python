import matplotlib.pyplot as plt
import math

def DrawLine(x1,y1,x2,y2):
    plt.plot([x1,x2], [y1,y2], 'black', linestyle="-")

DrawLine(-400,0,400,0)
DrawLine(0,1.5,0,-1.5)

degree=-360
while degree <= 360:
    sindegree=math.sin(math.radians(degree))
    cosdegree=math.cos(math.radians(degree))
    if degree%90 == 0:
        plt.scatter(degree, sindegree, s=50, color = 'blue')
        plt.scatter(degree, cosdegree, s=50, color = 'red')
    else:
        plt.scatter(degree, sindegree, s=2, color = 'blue')
        plt.scatter(degree, cosdegree, s=2, color = 'red')
    degree=degree+1

plt.xlim([-420, 420])
plt.ylim([-2, 2])

plt.grid()
plt.show()
