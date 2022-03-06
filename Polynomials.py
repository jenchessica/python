import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5)
#plt.ylim([-15,1000000])
y = x**2
plt.plot(x, y, '-r', label='y=x^2')

y = x**2+1
plt.plot(x, y, '-b', label='y=x^2+1')

y = x**2+x
plt.plot(x, y, '-g', label='y=x^2+x')

y = x**2+x+5
plt.plot(x, y, '-m', label='y=x^2+x+5')

plt.legend(loc='upper left')
plt.grid()
plt.show()
