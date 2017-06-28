import numpy as np
import numpy.random as nprandom
import matplotlib.pyplot as plt

#define linspace for the given intervall
x = np.linspace(0.001, 1, 100)
#define function for pi calculation
f = lambda x: np.sqrt(1 - x**2)
fx = f(x)

#define fuction for rejection sampling
def approx(number_sample):
    M = 1                               #scaling factor can be one for this function
    u1 = nprandom.rand(number_sample)   #uniform random samples in [0, 1)
    u2 = nprandom.rand(number_sample)   #uniform random samples in [0, 1)
    idx = np.where(u2 <= f(u1) / M)[0]  #rejection criterion
    v = u1[idx]

    #approximation of pi
    #due to symmetry we only need to sample from the upper right corner of the box
    #(one quarter of the circle). In this case the formula to determine pi can be
    #explicitly written as: pointsInCircle / totalPoints = pi * L^2 / (4 * L^2)
    approximation = len(v) / number_sample * 4

    return [v, idx, u1, u2, approximation]


w = approx(100000)
#plot histogram
fig, ax = plt.subplots()
ax.hist(w[0], normed = 1, bins = 40, alpha = 0.7)
ax.plot(x, fx, 'r')
ax.set_title('estimated efficency = %3.1f%%'%(100 * len(w[0]) / len(w[2])) +
                '\n approximation of pi = ' + str(w[4]))
plt.savefig('pi.png')

#plot accepted and rejected areas
fig, ax = plt.subplots()
ax.plot(w[2], w[3], '.', c = 'r', label = 'rejected', alpha = 0.2)
ax.plot(w[2][w[1]], w[3][w[1]], '.', c = 'g', label = 'accepted', alpha = 0.4)
ax.legend(fontsize = 14)
plt.savefig('accepted_rejected_pi.png')

#error calculation of the approximated pi to the pi of numpy
#in dependence of the magnitude of random numbers
sample_numbers = np.logspace(1, 6, num = 100)
pi_approximations = [approx(int(i))[4] for i in sample_numbers]
error = [(np.abs(i - np.pi) / np.pi) for i in pi_approximations]
fig, ax = plt.subplots()
ax.semilogx(sample_numbers, error)
ax.set_xlabel('magnitude random number')
ax.set_ylabel('error')
plt.savefig('error_calculation_pi.png')

plt.show()
