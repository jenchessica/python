import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5)
plt.ylim([-5,5])
y = x**2
plt.plot(x, y, '-r', label='y=x^2')

y = -(x**2)
plt.plot(x, y, '-b', label='y=-x^2')

y = -(x**2)+2
plt.plot(x, y, '-y', label='y=-x^2+2')

y = -0.1*((x+3)**2)+2
plt.plot(x, y, '-m', label='y=-0.1(x+3)^2+2')

plt.legend(loc='upper left')
plt.grid()
plt.show()
