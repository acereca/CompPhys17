#! /usr/bin/python3

from typing import List, Callable
import matplotlib.pyplot as plt
import numpy as np

def rKN(x: np.ndarray, fx: List[Callable], hs: float):
    k1 = np.array(x)
    k2 = np.array(x)
    k3 = np.array(x)
    k4 = np.array(x)

    l = len(fx)

    for i in range(l):
        k1[i] = fx[i](x)*hs

    for i in range(l):
        k2[i] = fx[i](x + k1*.5)*hs

    for i in range(l):
        k3[i] = fx[i](x + k2*.5)*hs

    for i in range(l):
        k4[i] = fx[i](x + k3)*hs

    return x + (k1 + 2*(k2 + k3) + k4)/6

if __name__ == '__main__':

    def diffeq(x: np.ndarray):
        return -1*x

    nsteps = 10
    maxx = 10.
    ndata = np.linspace(0, maxx, nsteps+1)
    xlist = np.array(ndata, ndmin=2).T
    xlist[0][0] = 1

    for i in range(0,xlist.shape[0]-1):
        out = rKN(xlist[i], [diffeq], maxx/nsteps)
        xlist[i+1] = out

    plt.yscale('log')
    plt.plot(ndata, np.array(xlist))
    plt.savefig('rk4-test.png')
