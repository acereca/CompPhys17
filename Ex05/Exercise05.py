import numpy as np


def solve_tridiagonal(a, b, c, r):
    #define length of a as equations we need to calcualte
    numberEquation = len(a)

    #loop for gaussian elimination
    for i in range(1, numberEquation):
        a[i] = a[i] / b[i - 1]
        b[i] = b[i] - a[i] * c[i - 1]
        r[i] = r[i] - a[i] * r[i - 1]

    x = np.zeros(len(b))

    #backward substitution
    x[numberEquation - 1] = r[numberEquation - 1] / b[numberEquation - 1]
    for i in range(numberEquation - 2, -1, -1):
        x[i] = (r[i] - c[i] * x[i + 1]) / b[i]

    return x


#define the matrix as give in the sheet
a = np.zeros(9)
b = np.zeros(10)
c = np.zeros(9)
r = np.zeros(10)

for i in range(10):
    b[i] = 2
    r[i] = 0.1
for i in range(9):
    a[i] = -1
    c[i] = -1

aa = np.append([0], [a])
ca = np.append([c], [0])

#copy array values
ac, bc, cc, rc = map(np.array, (aa, b, ca, r))

x = solve_tridiagonal(ac, bc, cc, rc)
print(x)

#check if the solution is correct
R = np.zeros(10)
R[0] = b[0] * x[0] + c[0] * x[1]
R[9] = a[-1] * x[-2] + b[9] * x[9]

for i in range(1, 9):
    R[i] = a[i] * x[i - 1] + b[i] * x[i] + c[i] * x[i + 1]
print(R)
