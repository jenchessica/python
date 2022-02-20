import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5)
plt.ylim([0,25])
y = x**2+14
plt.plot(x, y, '-r', label='Jessica: y=x^2+14')

y = x + 20
plt.plot(x, y, '-b', label='Daddy: y=x+20')

plt.legend(loc='upper left')
plt.grid()
plt.show()
