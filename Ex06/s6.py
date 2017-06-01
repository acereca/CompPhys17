#! /usr/bin/python3

import numpy as np
import scipy.linalg as la

def qr_decomp(mat: np.matrix):
    mat_c = np.triu(mat)
    i = 0

    while not (mat_c == mat).all():
        i += 1
        q, r = np.linalg.qr(mat)
        mat = np.dot(r,q)
        mat_c = np.triu(mat)
        #print('.')
        if i%1000 == 0:
            print(i)

    print(i)
    return mat

for NP in np.arange(5, 16):

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

    # solving h for eigenvalues
    h = qr_decomp(h)
    print(NP, np.diagonal(h))
