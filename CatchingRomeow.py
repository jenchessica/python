import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,10)
y = 3*x+10
plt.plot(x, y, '-r', label='Romeo: y=3x+10')

y = 5*x
plt.plot(x, y, '-b', label='Jessica: y=5x')
plt.legend(loc='upper left')
plt.grid()
plt.show()
