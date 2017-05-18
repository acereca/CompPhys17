import numpy as np
import matplotlib.pyplot as plt


def k(x):
    return epsilon - x

epsilon = 0         #start value of epsilon
stepsize = 0.0001    #stepsize to increas epsilon
signChanges = 3     #counts of sign changes (3 for the first 3 eigenvalues)

h = 0.001
n = 0               #starting point
x = 15

y_n = 0             #seed values
y_plus_1 = 0.1

while(n < x):
    y_minus_1 = y_n
    y_n = y_plus_1

    y_first_part = 2 * (1 - (5 / 12) * (h**2) * k(n)) * y_n
    y_sec_part = (1 + ((h**2) * k(n - h)) / 12) * y_minus_1
    y_third_part = 1 + ((h**2) * k(n + h)) / 12
    y_plus_1 = (y_first_part - y_sec_part) / y_third_part

    y_sign = y_plus_1
    n += h

if((y_sign * y_plus_1) > 0):
    i = 0
    while(i < signChanges):
        y_sign = y_plus_1
        y_plus_1 = 1
        y_n = 0
        n = 0
        n += h

        while(n < x):
            y_minus_1 = y_n
            y_n = y_plus_1

            y_first_part = 2 * (1 - (5 / 12) * (h**2) * k(n)) * y_n
            y_sec_part = (1 + ((h**2) * k(n - h)) / 12) * y_minus_1
            y_third_part = 1 + ((h**2) * k(n + h)) / 12
            y_plus_1 = (y_first_part - y_sec_part) / y_third_part

            n += h

        if((y_sign * y_plus_1) <= 0):
            print()
            print(epsilon - stepsize)
            print(epsilon)
            i += 1

        epsilon += stepsize


#2.338
#4.088
#5.521
