import matplotlib.pyplot as plt
import math

def DrawCircle(x0, y0, r):
    degree=0
    while degree <= 360:
        x=x0+(r*(math.cos(math.radians(degree))))
        y=y0+(r*(math.sin(math.radians(degree))))
        plt.scatter(x, y, s=10, color = 'blue')
        degree=degree+1

DrawCircle(3, 4, 1)
DrawCircle(0, 0, 1)
DrawCircle(1, 2, 3)
DrawCircle(-2, 1, 3)

plt.xlim([-10, 10])
plt.ylim([-10, 10])

plt.grid()
plt.show()
