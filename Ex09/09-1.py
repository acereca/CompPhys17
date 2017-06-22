import numpy as np
from rk4 import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

sigma = 10
b = 8/3
nsteps = 1000
stepsize = .01

for u,r in enumerate([.5,1.15,1.3456,24,30]):

    a0 = np.sqrt(b*(r-1))

    fsys = [
        lambda x: -sigma*(x[0] - x[1]), # x
        lambda x: r*x[0] - x[1] - x[0]*x[2], # y
        lambda x: x[0]*x[1] - b*x[2] # z
    ]

    xlist = np.ndarray(shape=(nsteps+1,3), dtype=float)
    if r == .5:
        xlist[0] = np.array([[
            .1,.1,.1
        ]])
    else:
        xlist[0] = np.array([[
            a0+.1*r,
            a0-.5*r,
            r-1
        ]])

    for i in range(nsteps):
        xlist[i+1] = rKN(xlist[i],fsys, stepsize)

    fig = plt.figure(figsize=(15, 10))
    ax = fig.gca(projection='3d')
    ax.plot(xlist[:,0], xlist[:,1], xlist[:,2])
    ax.scatter([a0,-a0,0],[a0,-a0,0],[r-1,r-1,0], color='r')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.savefig('plot_{}.png'.format(u))
