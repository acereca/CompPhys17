import numpy as np
import matplotlib.pyplot as plt


#function that integrates the 2 - body - problem using the forward
#euler algorithm. The initial velocity needs to be two dimensional
#vector, the step size h can be choosen. The program breaks when the
#orbit is complete.
def euler(v_0, h, s_0 = np.array([0, 1])):
    S = [s_0]   #list for spatial coordinate
    V = [v_0]   #list for relative velocity
    E = []      #list for the Energy
    test = 0    #variable to check if the orbit is complete
    step = 0
    maxstep = 1000000

    while((test < 2) and (step < maxstep)):
        S.append(S[-1] + h * V[-1])
        V.append(V[-1] - h * S[-1] / (np.sqrt(S[-2][0]**2 + S[-2][1]**2)**3))
        E.append((0.5 * (V[-1]**2)[0] + (V[-1]**2)[1]) - (1/((S[-1]**2)[0] + (S[-1]**2)[1])**0.5))

        if((S[-1])[0] < 0):
            test = 1
        if(test == 1 and (S[-1])[0] > 0):
            test = 2

    return np.array(S), np.array(V), np.array(E)


#for the given initial values the eccentricity is zero,
#therefore the orbit is circular
S, V, E = euler(np.array([1, 0]), 0.0001)

plt.figure(figsize = (6.5, 10))
plt.plot(S[:, 0], S[:, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

energyerror = []
H = [0.01, 0.001, 0.0001, 0.0001, 0.00001]
for h in H:
    S, V, E = euler(np.array([1, 0]), h)
    energyerror.append((abs(E[-1] - E[0])) / (abs(E[0])))

plt.plot(H, energyerror)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Stepsize h')
plt.ylabel('error in energy')
plt.show()


#use different initial velocity to achieve another orbit
S, V, E = euler(np.array([1.3, 0]), 0.0001)

plt.figure(figsize = (6.5, 10))
plt.plot(S[:, 0], S[:, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

energyerror = []
H = [0.01, 0.001, 0.0001, 0.0001, 0.00001]
for h in H:
    S, V, E = euler(np.array([1.3, 0]), h)
    energyerror.append((abs(E[-1] - E[0])) / (abs(E[0])))

plt.plot(H, energyerror)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('stepsize h')
plt.ylabel('error in energy')
plt.show()


#do the same for the third orbit with again another initial velocity
S, V, E = euler(np.array([0.8, 0]), 0.001)

plt.figure(figsize = (6.5, 10))
plt.plot(S[:, 0], S[:, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

energyerror = []
H = [0.01, 0.001, 0.0001, 0.0001, 0.00001]
for h in H:
    S, V, E = euler(np.array([0.8, 0]), h)
    energyerror.append((abs(E[-1] - E[0])) / (abs(E[0])))

plt.plot(H, energyerror)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('stepsize h')
plt.ylabel('error in energy')
plt.show()
