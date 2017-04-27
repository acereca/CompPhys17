import numpy as np
import matplotlib.pyplot as plt

a = 5
n = np.array([1,5,10,20,30,50])
xdata = np.linspace(0,1, 1000)

y = lambda x, a, n: x**n/(x+a)


plt.figure(figsize=(10,5))

plt.xlabel('x')
plt.ylabel('y')

for it in n:
    plt.plot(xdata, y(xdata, a, it), label="n={}".format(it))

plt.legend()

plt.savefig('01-2a.png')
