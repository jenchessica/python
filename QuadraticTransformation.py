import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5)
plt.ylim([-2,5])
y = x**2
plt.plot(x, y, '-r', label='y=x^2')

y = 0.5*(x**2)
plt.plot(x, y, '-b', label='y=0.5x^2')

y = 0.2*(x**2)
plt.plot(x, y, '-g', label='y=0.2x^2')

y = 2*(x**2)
plt.plot(x, y, '-y', label='y=2x^2')

y = 0.1*((x+1)**2)-1
plt.plot(x, y, '-m', label='y=0.1(x+1)^2-1')

plt.legend(loc='upper left')
plt.grid()
plt.show()
