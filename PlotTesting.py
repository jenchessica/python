import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,10)
y = -x+7
plt.plot(x, y, '-r', label='heads: y=-x+7')

y = -0.5*x+5.5
plt.plot(x, y, '-b', label='legs: y=-0.5x+5.5')
plt.legend(loc='upper left')
plt.grid()
plt.show()
