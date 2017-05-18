#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
# determine figure seize for plots
plt.figure(figsize=(8,6))

# N Number of iterations -4?
#N = 10000
# n as current iteration step
#n = -1 * N + 2
# h Stepsize
#h = 0.0001
# list for x results
#x_results = []
# list for y results
#y_results = []


N = 60000 # iterations

h = 0.0001
h2 = pow(h,2)

epsilon = 2.5 # n+1/2

y = 0.0
k = 0.0
x = -1*(N-2)*h

k_minus_2 = epsilon + x-2*h # k_0
k_minus_1 = epsilon + x-h # k_1
a = 0.1
y_minus_2 = 0 # y_0
y_minus_1 = a # y_1

x_out = []
y_out = []

n=-1*N+2

while n<N-2:
  n+=1
  x += h;
  k = 2*epsilon - pow(x, 2)
  b = h2/12
  y = ( 2*(1-5*b*k_minus_1) * y_minus_1 - (1+b*k_minus_2) * y_minus_2 ) / (1 + b * k)

  # Save for plotting
  x_out.append(x)
  y_out.append(y)

  # Shift for next iteration
  y_minus_2 = y_minus_1
  y_minus_1 = y
  k_minus_2 = k_minus_1
  k_minus_1 = k


# Plot
plt.figure(1)
plt.plot(x_out, y_out, label="$\epsilon = "+repr(epsilon)+"$")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Schroedinger Eqn in Harmonic Potential")
plt.legend(loc=1)
plt.show()
