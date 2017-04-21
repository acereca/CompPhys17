import numpy as np
import sys
import pandas as pd

def y(a, n, y0):
    if n == 0:
        return y0
    else:
        return 1/n - a* y(a, n-1, y0)

if __name__ == '__main__':
    
    # accepting args as: a, n0, y0, n1
    
    print(sys.argv)

    a = int(sys.argv[1])
    n0 = int(sys.argv[2])
    n1 = int(sys.argv[4])
    y0 = int(sys.argv[3])

    ndata = range(min(n0,n1),max(n0,n1)+1)
    print(ndata)
    ydata = [y(a, i, y0) for i in ndata] 
    print(ydata)
    
    f = open("01-2b.tex", 'w')
    f.write(pd.DataFrame(np.array([ndata, ydata]).T, columns=['n',"$y_n(" +str(a)+ ")$"]).to_latex(escape=False))
    f.close()
