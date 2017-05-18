import numpy as np
import matplotlib.pyplot as plt


def k(x):
    return epsilon - x

h = 0.001
epsilon = 0.0
n = 0               #starting point
x = 15

y_n = 0             #seed values
y_plus_1 = 0.1

x_out = []
y_out = []

while(n < x):
    y_minus_1 = y_n
    y_n = y_plus_1

    y_first_part = 2 * (1 - (5 / 12) * (h**2) * k(n)) * y_n
    y_sec_part = (1 + ((h**2) * k(n - h)) / 12) * y_minus_1
    y_third_part = 1 + ((h**2) * k(n + h)) / 12
    y_plus_1 = (y_first_part - y_sec_part) / y_third_part

    x_out.append(n)
    y_out.append(y_plus_1)

    n += h


plt.plot(x_out, y_out)
plt.xlabel('x')
plt.ylabel('$\psi(x)$')
plt.title('$\epsilon=$' + str(epsilon))
plt.xlim(0.0, x * 1.2)
plt.savefig('plot_' + str(epsilon) + '.png', dpi = 300)
plt.show()
