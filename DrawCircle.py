import matplotlib.pyplot as plt
import math

def DrawLine(x1,y1,x2,y2):
    plt.plot([x1,x2], [y1,y2], 'r.', linestyle="--")


print (math.pi)
print (math.radians(90))
print (math.sin(math.radians(90)))


# plt.scatter(x, y, s=10, color = 'blue')

r=1
x=r*(math.cos(math.radians(30)))
y=r*(math.sin(math.radians(30)))

DrawLine(0,0,x,0)
DrawLine(x,0,x,y)
DrawLine(x,y,0,0)

degree=1

while degree <= 90:
    x=r*(math.cos(math.radians(degree)))
    y=r*(math.sin(math.radians(degree)))
    plt.scatter(x, y, s=10, color = 'blue')
    plt.scatter(-x, y, s=10, color = 'blue')
    plt.scatter(-x, -y, s=10, color = 'blue')
    plt.scatter(x, -y, s=10, color = 'blue')
    degree=degree+5

plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

plt.grid()
plt.show()
