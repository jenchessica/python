import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,10)

y = 2*x
plt.plot(x, y, '-r', label='y=2x')
plt.scatter(0, 0, color = 'hotpink')

y = 2*(x-1)+1
plt.plot(x, y, '-g', label='y-1=2(x-1)')
plt.scatter(1, 1, color = 'green')

y = 2*(x-4)+3
plt.plot(x, y, '-b', label='y-3=2(x-4)')
plt.scatter(4, 3, color = 'blue')

y = 2*(x+2)-1
plt.plot(x, y, '-', color='black', label='y+1=2(x+2)')
plt.scatter(-2, -1, color = 'black')

plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.legend(loc='upper left')
plt.grid()
plt.show()
