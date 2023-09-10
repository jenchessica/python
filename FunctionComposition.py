import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/2.0.2/api/colors_api.html

def f(x):
    return x+1

def g(x):
    return x*2

def h(x):
    return x**2

def p(x):
    return g(f(x))

def q(x):
    return f(g(x))

def u(x):
    return f(h(x))

def v(x):
    return h(f(x))

x = np.linspace(-5,5)
#plt.ylim([-15,1000000])

y = f(x)
plt.plot(x, y, '-r', label='y=f(x)=x+1')

y = g(x)
plt.plot(x, y, '-b', label='y=g(x)=x*2')

y=h(x)
plt.plot(x, y, '-g', label='y=h(x)=x^2')

y=p(x)
plt.plot(x, y, '-m', label='y=p(x)=g(f(x))=2x+2')

y=q(x)
plt.plot(x, y, '-y', label='y=q(x)=f(g(x))=2x+1')

y=u(x)
plt.plot(x, y, '-c', label='y=u(x)=f(h(x))=x^2+1')

y=v(x)
plt.plot(x, y, '-k', label='y=v(x)=h(f(x))=(x+1)^2')

plt.legend(loc='upper left')
plt.grid()
plt.show()
