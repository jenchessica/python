# The function y=x^2 is quadratic, and the graph of this function represents a parabola.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5)
plt.ylim([-2,10])

y = x**2
plt.plot(x, y, '-r', label='y=x^2')
plt.scatter(0, 0, s=30, color = 'red')

y = (x-3)**2
plt.plot(x, y, '-b', label='y=(x-3)^2')
plt.scatter(3, 0, s=30, color = 'blue')

y = (x+2)**2
plt.plot(x, y, '-g', label='y=(x+2)^2')
plt.scatter(-2, 0, s=30, color = 'green')

y = x**2+1
plt.plot(x, y, '-m', label='y=x^2+1')
plt.scatter(0, 1, s=30, color = 'magenta')

y = (x+4)**2-2
plt.plot(x, y, '-r', label='y=(x+4)^2-2')
plt.scatter(-4, -2, s=30, color = 'red')

plt.legend(loc='upper left')
plt.grid()
plt.show()
