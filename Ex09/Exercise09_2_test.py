import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#runge kutta 4 for the functions of x, y and z with defined functions x, y, z
def rk4x(x_dot, x, y, sig, h):
    k1 = x_dot(x, y, sig)
    k2 = x_dot(x + (h / 2) * k1, y, sig)
    k3 = x_dot(x + (h / 2) * k2, y, sig)
    k4 = x_dot(x + h * k3, y, sig)

    return( 1 / 6 * (k1 + (2 * k2) + (2 * k3) + k4))

def x_dot(x = 1, y = 1, sig = 10):
    return(-sig * (x - y))

def rk4y(y_dot, x, y, z, r, h):
    k1 = y_dot(x, y, z, r)
    k2 = y_dot(x, y + (h / 2) * k1, z, r)
    k3 = y_dot(x, y + (h / 2) * k2, z, r)
    k4 = y_dot(x, y + h * k3, z, r)

    return( 1 / 6 * (k1 + (2 * k2) + (2 * k3) + k4))

def y_dot(x = 1, y = 1, z = 1, r = 1):
    return((r * x) - y - (x * z))

def rk4z(z_dot, x, y, z, b, h):
    k1 = z_dot(x, y, z, b)
    k2 = z_dot(x, y, z + (h / 2) * k1, b)
    k3 = z_dot(x, y, z + (h / 2) * k2, b)
    k4 = z_dot(x + h * k3, y, z, b)

    return( 1 / 6 * (k1 + (2 * k2) + (2 * k3) + k4))

def z_dot(x = 1, y = 1, z = 1, b = 8 / 3):
    return((x * y) - (b * z))

#function to find maximum of z
def maxfinder(l = []):
    zk = []
    for k in range(1, len(l) - 1):
        if(l[k] > l[k - 1] and l[k] > l[k + 1]):
            zk.append(l[k])
    return zk

x_list = []
y_list = []
z_list = []
t_list = []

#starting values
r = 26
sig = 10
b = 8 / 3
h = 0.01
a = np.sqrt(b * (r - 1))

#fix points
c_plus = [a - 0.5, a, r - 1]
c_minus = [-a, -a, r - 1]

#starting values in space of fix point
x_list.append(c_plus[0])
y_list.append(c_plus[1])
z_list.append(c_plus[2])
t_list.append(0)

#calculating values
for i in range(100000):
    x_list.append(x_list[i] + h * rk4x(x_dot, x_list[i], y_list[i], sig, h))
    y_list.append(y_list[i] + h * rk4y(y_dot, x_list[i], y_list[i], z_list[i], r, h))
    z_list.append(z_list[i] + h * rk4z(z_dot, x_list[i], y_list[i], z_list[i], b, h))
    t_list.append((i + 1) * h)

zk = maxfinder(z_list)
del zk[len(maxfinder(z_list)) - 1]
zk1 = maxfinder(z_list)
del zk1[0]

plt.plot(zk, zk1, '*b')
plt.plot(zk, zk, '-r')
plt.xlabel('z_k')
plt.ylabel('z_k+1')
plt.savefig('z_k.png', dpi=300)
plt.show()
