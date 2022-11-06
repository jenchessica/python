import matplotlib.pyplot as plt

# How to Adjust Marker Size in Matplotlib?
#   https://www.geeksforgeeks.org/how-to-adjust-marker-size-in-matplotlib/
# Insert a dot at a certain point on a line with matplotlib
#    https://stackoverflow.com/questions/31502456/insert-a-dot-at-a-certain-point-on-a-line-with-matplotlib
# matplotlib.pyplot.plot reference
#    https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

r = 0.01

romeoX = 0
romeoY = 0
julietX = 100
julietY = 0
habibiX = 100
habibiY = 100
shurikX = 0
shurikY = 100

epsilon = 0.00001

while not (abs(romeoX-50)<epsilon and abs(romeoY-50)<epsilon):
    plt.plot(romeoX,  romeoY, 'g.', markersize=5)
    plt.plot(julietX, julietY, 'y.', markersize=5)
    plt.plot(habibiX, habibiY, 'r.', markersize=5)
    plt.plot(shurikX, shurikY, 'b.', markersize=5)

    newromeoX = romeoX + r*(julietX-romeoX)
    newromeoY = romeoY + r*(julietY-romeoY)
    newjulietX = julietX + r*(habibiX-julietX)
    newjulietY = julietY + r*(habibiY-julietY)
    newhabibiX = habibiX + r*(shurikX-habibiX)
    newhabibiY = habibiY + r*(shurikY-habibiY)
    newshurikX = shurikX + r*(romeoX-shurikX)
    newshurikY = shurikY + r*(romeoY-shurikY)

    romeoX = newromeoX
    romeoY = newromeoY
    julietX = newjulietX
    julietY = newjulietY
    habibiX = newhabibiX
    habibiY = newhabibiY
    shurikX = newshurikX
    shurikY = newshurikY

plt.axis([-10, 110, -10, 110])        # Modified axis
plt.show()
