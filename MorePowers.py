import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,20)
#plt.ylim([-15,1000000])
y = x**2
plt.plot(x, y, '-r', label='y=x^2')

y = x**3
plt.plot(x, y, '-b', label='y=x^3')

y = x**4
plt.plot(x, y, '-g', label='y=x^4')

#y = x**(1/2)
#plt.plot(x, y, '-y', label='y=x^0.5')

#y = x**(1/3)
#plt.plot(x, y, '-b', label='y=x^(1/3)')

y = x
plt.plot(x, y, '-b', label='y=x')

y = 2**x
plt.plot(x, y, '-m', label='y=2^x')

plt.legend(loc='upper left')
plt.grid()
plt.show()
