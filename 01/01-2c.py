#! /usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b = __import__('01-2b')

if __name__ == '__main__':

    a = 5
    n0 = 0
    n1 = 30
    y0 = np.log((1+a)/a)

    ndata = b.get_nset(n0,n1)
    ydata = np.array(b.iteration(a,y0,ndata))

    ndata = np.append([0],ndata)
    f = open("01-2c.tex", 'w')
    f.write(pd.DataFrame(
        [ndata, ydata],
        index=['n',"$y_n(" +str(a)+ ")$"]
    ).transpose().to_latex(escape=False))
    f.close()

    n0 = 50
    n1 = 30
    y0 = np.linspace(0,3,7)


    ndata = b.get_nset(n0,n1)
    print(ndata)

    plt.style.use('bmh')
    plt.figure(figsize=(10,5))
    for y in y0:
        ydata = np.array(b.iteration(a,y0,ndata))[1:]
        plt.plot(ndata,ydata,label="$y_0=${}".format(y))


    plt.title("experiment for $y_0\in \{0,0.5,1,1.5,2,2.5,3\}$ and $n \in [30,50]$")
    plt.ylabel('y')
    plt.xlabel('n')
    plt.savefig('01-2c.png')
