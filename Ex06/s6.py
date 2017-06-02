#! /usr/bin/python3

import numpy as np

Q4l = []
for NP in np.arange(15, 31):

    # creating Q
    Q = np.diagflat([1.]*NP)
    for n in np.arange(NP):
        for m in np.arange(NP):
            if n==m-1:
                #print (n,m)
                Q[n,m] = np.sqrt(float(m))
            if n==m+1:
                #print (n,m)
                Q[n,m] = np.sqrt(float(m))

    # creating Q2 and Q4
    Q2 = np.dot(Q,Q)
    Q4 = np.dot(Q2,Q2)

    h0 = np.diagflat(np.arange(.5, NP+.5, 1))
    h = h0 + .1*Q4

    Q4l.append(Q4)

import pandas as pd

Q41 = pd.DataFrame(Q4l[0])

f = open("q.tex", 'w')
f.write(
    pd.DataFrame(Q41).transpose().to_latex(escape=False, formatters=[lambda x: "{:.0f}".format(x)]*15)
)
f.close()


Q42 = pd.DataFrame(Q4l[15])

f = open("q2.tex", 'w')
f.write(
    pd.DataFrame(Q42).transpose().to_latex(escape=False, formatters=[lambda x: "{:.0f}".format(x)]*30)
)
f.close()
