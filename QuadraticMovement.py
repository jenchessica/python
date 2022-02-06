import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5)
plt.ylim([-2,5])
y = x**2
plt.plot(x, y, '-r', label='y=x^2')

y = (x-1)**2
plt.plot(x, y, '-b', label='y=(x-1)^2')

y = (x-3)**2
plt.plot(x, y, '-m', label='y=(x-3)^2')

y = (x+2)**2
plt.plot(x, y, '-y', label='y=(x+2)^2')

y = x**2+1
plt.plot(x, y, '-g', label='y=x^2+1')

y = (x+3)**2-2
plt.plot(x, y, '-o', label='y=(x+3)^2-2')

plt.legend(loc='upper left')
plt.grid()
plt.show()
