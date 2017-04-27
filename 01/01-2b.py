import numpy as np
import sys
import pandas as pd

def get_nset(n0,n1):
    if n0 > n1:
        n = np.arange(n1, n0+1)
    elif n1 > n0:
        n = np.arange(n0, n1+1)
    else:
        n = []
        print('no iteration possible')

    return n

def iteration(a, y0, n):

    y = [y0]
    for i in n:
        y1 = 1/(i+1) - a * y[-1]
        y.append(y1)

    return y


if __name__ == '__main__':

    # accepting args as: a, n0, y0, n1

    print(sys.argv)

    a = float(sys.argv[1])
    n0 = int(sys.argv[2])
    n1 = int(sys.argv[4])
    y0 = float(sys.argv[3])

    ndata = get_nset(n0,n1)
    ydata = np.array(iteration(a, y0, ndata))

    ndata = np.append([0],ndata)
    print(ydata.__class__)


    f = open("01-2b.tex", 'w')
    f.write(
        pd.DataFrame([ndata, ydata],
        index=['n',"$y_n(" +str(a)+ ")$"]
        ).transpose().to_latex(escape=False))
    f.close()
