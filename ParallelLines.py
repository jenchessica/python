import matplotlib.pyplot as plt
import numpy as np

class Point:
   def __init__(self, x, y):
    self.x = x
    self.y = y

def DrawLine(p1, p2):
    m = (p2.y-p1.y)/(p2.x-p1.x)
    b = p1.y-(m*p1.x)
    x = np.linspace(-5,5,10)
    y = m*x+b
    plt.plot(x, y, '-r')
    plt.scatter(p1.x, p1.y, color = 'hotpink')
    plt.scatter(p2.x, p2.y, color = 'hotpink')
    return m

def ParallelLine(p1, p2, p3):
    m = DrawLine(p1, p2)
    b = p3.y-(m*p3.x)
    x = np.linspace(-5,5,10)
    y = m*x+b
    plt.plot(x, y, '-b')
    plt.scatter(p3.x, p3.y, color = 'blue')

p1 = Point(3, 4)
p2 = Point(5, 2)
p3 = Point(2,4)
ParallelLine(p1, p2, p3)

plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.legend(loc='upper left')
plt.grid()
plt.show()
