import numpy as np
import numpy.random as nprandom
import matplotlib.pyplot as plt

#maximal point for plotting invervall as given in the sheet
a = 0.5

#define linspace for the given intervall
x = np.linspace(0.001, a, 100)
#define function with normalization factor, therfore b = 2 / a^2
f = lambda x: (2 / a**2) * x
fx = f(x)

M = 2 / a                           #scale factor for rejection sampling g(x)
u1 = nprandom.rand(10000) * a       #uniform random samples scaled out in [0, 1)
u2 = nprandom.rand(10000)           #uniform random samples in [0, 1)
idx = np.where(u2 <= f(u1) / M)[0]  #rejection criterion
v = u1[idx]

#plot histogram
fig, ax = plt.subplots()
ax.hist(v, normed = 1, bins = 40, alpha = 0.7)
ax.plot(x, fx, 'r')
ax.set_title('estimated efficency = %3.1f%%'%(100 * len(v) / len(u1)))
plt.savefig('pdf.png')

#plot accepted and rejected areas
fig, ax = plt.subplots()
ax.plot(u1, u2, '.', c = 'r', label = 'rejected', alpha = 0.2)
ax.plot(u1[idx], u2[idx], '.', c = 'g', label = 'accepted', alpha = 0.4)
ax.legend(fontsize = 14)
plt.savefig('accepted_rejected.png')

plt.show()
